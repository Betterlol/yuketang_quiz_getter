"""
雨课堂 题库自动收集工具 v2
============================
基于实际页面结构重写，支持:
  1. 手动登录 + Cookie 持久化
  2. 从课程页发现所有 Quiz 条目 (icon--zuoye)
  3. 逐个进入 quiz，提取所有题目（题干 + 选项 + 类型）
  4. 导出 Markdown

用法:
  pip install playwright
  playwright install chromium
  python auto.py
"""

import asyncio
import json
import os
import re
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright

# ═══════════════════════════════════════════
#  配置
# ═══════════════════════════════════════════

COURSE_URL = "https://sustc.yuketang.cn/pro/lms/8MuSR5nESwE/29477711/studycontent"
COOKIE_FILE = "yuketang_cookies.json"
OUTPUT_FILE = "yuketang_questions.md"
HEADLESS = False
DELAY_AFTER_CLICK = 2.0       # 点击后的等待时间(秒)
DELAY_BETWEEN_QUIZ = 3.0      # 两个 quiz 之间的间隔

# ═══════════════════════════════════════════
#  工具函数
# ═══════════════════════════════════════════

def log(msg: str):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")


def clean_text(text: str) -> str:
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ═══════════════════════════════════════════
#  Cookie 管理
# ═══════════════════════════════════════════

async def load_cookies(context) -> bool:
    if not os.path.exists(COOKIE_FILE):
        return False
    try:
        with open(COOKIE_FILE, "r") as f:
            cookies = json.load(f)
        await context.add_cookies(cookies)
        log(f"已加载 {len(cookies)} 条 Cookie")
        return True
    except Exception as e:
        log(f"加载 Cookie 失败: {e}")
        return False


async def save_cookies(context):
    cookies = await context.cookies()
    with open(COOKIE_FILE, "w") as f:
        json.dump(cookies, f, indent=2)
    log(f"已保存 {len(cookies)} 条 Cookie")


# ═══════════════════════════════════════════
#  等待用户就绪
# ═══════════════════════════════════════════

async def wait_for_user_ready(page):
    """打开浏览器，让用户手动登录并导航到课程页，按 Enter 后继续"""
    log("→ 浏览器已打开，请手动完成以下操作：")
    log("  1. 如果未登录，请在页面中完成登录（扫码/账号）")
    log(f"  2. 导航到课程页面（如果还未自动跳转）")
    log("  3. 确认页面内容已完整加载")
    log("")
    input("  完成后请按 Enter 键继续...")
    log("用户确认，继续执行")


# ═══════════════════════════════════════════
#  发现所有 Quiz 条目
# ═══════════════════════════════════════════

async def find_quiz_items(page):
    """
    在课程页面上找到所有 quiz。
    根据实际 HTML: quiz 条目是 .leaf-detail，包含 i.icon--zuoye
    """
    quizzes = []

    leaf_details = page.locator(".leaf-detail")
    count = await leaf_details.count()
    log(f"共找到 {count} 个 .leaf-detail 条目")

    for i in range(count):
        ld = leaf_details.nth(i)
        inner = await ld.inner_html()
        if "icon--zuoye" in inner:
            title_el = ld.locator(".title").first
            title = clean_text(await title_el.inner_text()) if await title_el.count() else f"Quiz_{i}"
            quizzes.append((ld, title))
            log(f"  发现 Quiz: {title}")

    return quizzes


async def click_quiz_item(quiz_el) -> bool:
    """
    点击 quiz 条目。
    Vue SPA 拦截普通点击，直接用 JS dispatchEvent 模拟最可靠。
    """
    try:
        await quiz_el.scroll_into_view_if_needed(timeout=5000)
    except Exception:
        pass

    try:
        await quiz_el.dispatch_event("click")
        return True
    except Exception:
        pass

    # 备选: 原生 JS 点击
    try:
        await quiz_el.evaluate("(el) => el.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, view: window}))")
        return True
    except Exception:
        return False


# ═══════════════════════════════════════════
#  提取单个 quiz 页面中的所有题目
# ═══════════════════════════════════════════

async def extract_questions_from_quiz(page, quiz_title: str) -> list[dict]:
    """
    进入 quiz 页面后，提取所有题目。
    实际 HTML:
      - 侧边栏 subject-item 显示题号 (1/2/3/4)
      - 当前题目: .item-type (题型), .problem-body .custom_ueditor_cn_body p (题干)
      - 选项: .list-unstyled-radio .radioText .custom_ueditor_cn_body p
      - "下一题" 按钮进行翻页, 也可直接点侧边栏题号
    """
    questions = []
    log(f"  开始提取: {quiz_title}")

    # 等待侧边栏加载
    try:
        await page.wait_for_selector(".subject-item", timeout=15000)
    except PwTimeout:
        log(f"  未找到题目列表，可能不是 quiz 页面")
        return []

    # 获取总题数 (只统计侧边栏的题号, 排除主内容区 .container-problem .subject-item)
    sidebar_items = page.locator("[class*='aside'] .subject-item, .aside-body .subject-item, .list-inline .subject-item")
    total = await sidebar_items.count()
    if total == 0:
        # 兜底: 用全部 subject-item 减去主内容区那个
        has_main = await page.locator(".container-problem .subject-item").count()
        all_items = page.locator(".subject-item")
        total_all = await all_items.count()
        total = total_all - (1 if has_main else 0)
        # 只取前 total 个, 跳过末尾的主内容区
        subject_items = all_items
    else:
        subject_items = sidebar_items
    log(f"  共 {total} 题")

    for q_idx in range(total):
        # 点击侧边栏第 q_idx+1 题 (更可靠)
        si = subject_items.nth(q_idx)
        try:
            await si.click(timeout=5000)
            await page.wait_for_timeout(1500)
        except Exception:
            log(f"  第 {q_idx+1} 题点击失败，尝试 '下一题'")
            # 回退方案: 点击下一题
            next_btn = page.locator("button:has-text('下一题')").first
            if await next_btn.count():
                try:
                    await next_btn.click(timeout=5000)
                    await page.wait_for_timeout(1500)
                except Exception:
                    log(f"  翻页也失败，终止")
                    break
            else:
                break

        # 提取题目
        q = await extract_current_question(page, q_idx + 1)
        if q:
            questions.append(q)
            log(f"    第 {q_idx+1} 题 ✓ [{' '.join(q['type'])}] {q['stem'][:60]}...")
        else:
            log(f"    第 {q_idx+1} 题 ✗ 提取失败")
            # 截图 debug
            await page.screenshot(path=f"debug_q{quiz_title[:10]}_{q_idx+1}.png")

    log(f"  ✓ 完成: {quiz_title}: {len(questions)}/{total} 题")
    return questions


async def extract_current_question(page, q_num: int) -> dict | None:
    """提取当前显示的题目 (支持单选/多选/判断/填空/主观)"""
    try:
        # 题型: "1.单选题 (1分)" 或类似
        type_el = page.locator(".item-type").first
        q_type = clean_text(await type_el.inner_text()) if await type_el.count() else "未知"

        # 题干: .problem-body .custom_ueditor_cn_body p
        stem_el = page.locator(".problem-body .custom_ueditor_cn_body p").first
        stem = clean_text(await stem_el.inner_text()) if await stem_el.count() else ""

        # 备选: 直接用 .problem-body
        if not stem:
            stem_el = page.locator(".problem-body").first
            stem = clean_text(await stem_el.inner_text()) if await stem_el.count() else ""

        # ── 提取选项 ──
        options = []

        # 方案1: 单选题/判断题 → radio 选项
        option_texts = page.locator(".list-unstyled-radio .radioText .custom_ueditor_cn_body p")
        opt_count = await option_texts.count()
        if opt_count:
            label_inputs = page.locator(".list-unstyled-radio .radioInput")
            for i in range(opt_count):
                txt = clean_text(await option_texts.nth(i).inner_text())
                if txt:
                    prefix = clean_text(await label_inputs.nth(i).inner_text()) if await label_inputs.nth(i).count() else ""
                    options.append(f"{prefix}. {txt}" if prefix else txt)

        # 方案2: 多选题 → checkbox 选项
        if not options:
            option_texts = page.locator(".list-unstyled-checkbox .checkboxText .custom_ueditor_cn_body p")
            opt_count = await option_texts.count()
            if opt_count:
                label_inputs = page.locator(".list-unstyled-checkbox .checkboxInput")
                for i in range(opt_count):
                    txt = clean_text(await option_texts.nth(i).inner_text())
                    if txt:
                        prefix = clean_text(await label_inputs.nth(i).inner_text()) if await label_inputs.nth(i).count() else ""
                        options.append(f"{prefix}. {txt}" if prefix else txt)

        # 方案3: 任意 list-unstyled 内的 label 文本
        if not options:
            any_list = page.locator("[class*='list-unstyled'] label")
            cnt = await any_list.count()
            for i in range(cnt):
                txt = clean_text(await any_list.nth(i).inner_text())
                if txt and len(txt) > 1:
                    options.append(txt)

        # ── 填空题: 提取 input 占位/值 ──
        blanks = []
        if not options or "填空" in q_type:
            inputs = page.locator(".problem-body input, .problem-body textarea")
            ic = await inputs.count()
            for i in range(ic):
                val = await inputs.nth(i).get_attribute("value") or ""
                placeholder = await inputs.nth(i).get_attribute("placeholder") or ""
                blanks.append(placeholder or val or f"___空{i+1}___")
            if blanks:
                options = blanks

        return {
            "num": q_num,
            "type": q_type,
            "stem": stem or "(空题干)",
            "options": options,
        }
    except Exception as e:
        log(f"  提取错误: {e}")
        return None


# ═══════════════════════════════════════════
#  导出 Markdown
# ═══════════════════════════════════════════

def export_markdown(all_data: dict[str, list[dict]], output: str):
    total = sum(len(qs) for qs in all_data.values())
    lines = [
        f"# 雨课堂 题库汇总",
        f"",
        f"- 课程链接: {COURSE_URL}",
        f"- 导出时间: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"- Quiz 总数: {len(all_data)}",
        f"- 题目总数: {total}",
        f"",
        f"---",
        f"",
    ]

    for quiz_name, questions in all_data.items():
        if not questions:
            continue
        lines.append(f"## {quiz_name}")
        lines.append("")
        for q in questions:
            lines.append(f"### Q{q['num']} [{q['type']}]")
            lines.append("")
            lines.append(q["stem"])
            lines.append("")
            if q["options"]:
                for opt in q["options"]:
                    lines.append(f"- {opt}")
                lines.append("")
            lines.append("---")
            lines.append("")

    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log(f"✓ 已导出 {total} 题到 {output}")


# ═══════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════

async def main():
    log("=" * 50)
    log("雨课堂 题库自动收集工具 v2")
    log("=" * 50)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=HEADLESS,
            args=["--disable-blink-features=AutomationControlled"],
        )

        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            locale="zh-CN",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
        )

        cookie_loaded = await load_cookies(context)
        page = await context.new_page()
        page.set_default_timeout(30000)

        if cookie_loaded:
            await page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            """)

        # 打开课程页面，让用户手动处理登录和导航
        await page.goto(COURSE_URL, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(2000)

        await wait_for_user_ready(page)

        # 用户确认后保存 cookie 供下次复用
        await save_cookies(context)

        # 展开所有章节 — JS 直接操作 DOM，绕过 Vue 的点击拦截
        log("展开所有章节...")
        expanded = await page.evaluate("""
            () => {
                const contents = document.querySelectorAll('.chapter-list .content');
                let count = 0;
                contents.forEach(el => {
                    if (el.style.display === 'none') {
                        el.style.display = 'block';
                        count++;
                    }
                });
                return count;
            }
        """)
        log(f"已展开 {expanded} 个章节 (JS 强制)")
        await page.wait_for_timeout(1000)

        # 验证：检查第一个 leaf-detail 是否 visible
        visible_check = await page.evaluate("""
            () => {
                const ld = document.querySelector('.leaf-detail');
                if (!ld) return 'no leaf-detail found';
                const rect = ld.getBoundingClientRect();
                const style = window.getComputedStyle(ld);
                return {
                    display: style.display,
                    visibility: style.visibility,
                    rect_width: rect.width,
                    rect_height: rect.height,
                    in_viewport: rect.top < window.innerHeight && rect.bottom > 0
                };
            }
        """)
        log(f"  leaf-detail 可见性: {visible_check}")
        await page.screenshot(path="debug_root.png", full_page=True)

        # 发现 quiz
        log("扫描 Quiz 条目...")
        await page.screenshot(path="debug_root.png", full_page=True)
        quizzes = await find_quiz_items(page)

        if not quizzes:
            log("未找到任何 Quiz！请检查页面结构")
            await browser.close()
            return

        log(f"共发现 {len(quizzes)} 个 Quiz")

        # 逐个处理
        all_questions: dict[str, list[dict]] = {}
        for idx, (quiz_el, title) in enumerate(quizzes):
            log(f"\n[{idx+1}/{len(quizzes)}] {title}")

            ok = await click_quiz_item(quiz_el)
            if not ok:
                log(f"  点击失败: {title}")
                continue

            await page.wait_for_timeout(int(DELAY_AFTER_CLICK * 1000))

            # 判断是否进入 quiz 页面 (检测 .subject-item 或 .item-type)
            if await page.locator(".subject-item").first.count():
                questions = await extract_questions_from_quiz(page, title)
                all_questions[title] = questions
            elif len(context.pages) > 1:
                log(f"  在新标签页中打开")
                quiz_page = context.pages[-1]
                await quiz_page.wait_for_load_state("domcontentloaded")
                await quiz_page.wait_for_timeout(2000)
                questions = await extract_questions_from_quiz(quiz_page, title)
                all_questions[title] = questions
                await quiz_page.close()
            else:
                log(f"  未检测到 quiz 页面，保存截图")
                await page.screenshot(path=f"debug_quiz_{idx}.png")
                all_questions[title] = []

            # 回到课程页
            log("  返回课程页...")
            try:
                await page.goto(COURSE_URL, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_timeout(3000)
            except Exception as e:
                log(f"  返回失败: {e}")

            await asyncio.sleep(DELAY_BETWEEN_QUIZ)

        # 导出
        log("\n" + "=" * 50)
        export_markdown(all_questions, OUTPUT_FILE)

        total = sum(len(qs) for qs in all_questions.values())
        for name, qs in all_questions.items():
            log(f"  {name}: {len(qs)} 题")
        log(f"总计: {total} 题")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
