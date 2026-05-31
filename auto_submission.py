"""
雨课堂 Quiz 自动答题提交工具
==============================
读取 yuketang_answers.md 中的答案，自动在雨课堂网站中提交。

用法:
  pip install playwright
  playwright install chromium
  python auto_submission.py

答案文件格式:
  sustec/software/yuketang_answers.md
  单选题: "- C. Shift Left"  → 选择 C
  判断题: "- 正确 (True)"   → 选"正确"
          "- 错误 (False)"  → 选"错误"
"""

import asyncio
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright

# ═══════════════════════════════════════════
#  配置
# ═══════════════════════════════════════════

COURSE_URL = "https://sustc.yuketang.cn/pro/lms/8MuSR5nESwE/29477711/studycontent"
ANSWERS_FILE = Path(__file__).parent / "sustech" / "software" / "yuketang_answers.md"
COOKIE_FILE = "yuketang_cookies.json"
HEADLESS = False
DELAY = 1.0

# ═══════════════════════════════════════════
#  日志
# ═══════════════════════════════════════════

def log(msg: str):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")

def clean_text(text: str) -> str:
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ═══════════════════════════════════════════
#  答案解析
# ═══════════════════════════════════════════

def parse_answers(path: Path) -> dict[str, list[str]]:
    """
    解析 answers.md, 返回 { quiz_name: [answer1, answer2, ...] }
    单选题 answer 为字母 "C", 判断题 answer 为 "正确"/"错误"
    """
    text = path.read_text(encoding="utf-8")
    result = {}

    # 按 quiz 分割
    quiz_blocks = re.split(r'(?=^## )', text, flags=re.MULTILINE)
    for block in quiz_blocks:
        if not block.startswith("## "):
            continue
        name_match = re.search(r'^## (.+)', block, flags=re.MULTILINE)
        if not name_match:
            continue
        quiz_name = name_match.group(1).strip()

        # 提取该 quiz 下所有答案行
        answers = []
        for line in block.split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            content = line[2:]

            # 判断题: 正确 / 错误
            if content.startswith("正确"):
                answers.append("正确")
            elif content.startswith("错误"):
                answers.append("错误")
            else:
                # 单选题: 提取首字母 A/B/C/D
                m = re.match(r'^([A-D])\.', content)
                if m:
                    answers.append(m.group(1))

        if answers:
            result[quiz_name] = answers

    return result


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
#  发现 Quiz
# ═══════════════════════════════════════════

async def find_quiz_items(page):
    quizzes = []
    leaf_details = page.locator(".leaf-detail")
    count = await leaf_details.count()
    for i in range(count):
        ld = leaf_details.nth(i)
        inner = await ld.inner_html()
        if "icon--zuoye" in inner:
            title_el = ld.locator(".title").first
            title = clean_text(await title_el.inner_text()) if await title_el.count() else f"Quiz_{i}"
            quizzes.append((ld, title))
    return quizzes


async def click_quiz_item(quiz_el) -> bool:
    try:
        await quiz_el.scroll_into_view_if_needed(timeout=5000)
    except Exception:
        pass
    try:
        await quiz_el.dispatch_event("click")
        return True
    except Exception:
        pass
    try:
        await quiz_el.evaluate("(el) => el.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, view: window}))")
        return True
    except Exception:
        return False


# ═══════════════════════════════════════════
#  答题
# ═══════════════════════════════════════════

async def answer_question(page, answer: str, q_idx: int) -> bool:
    """
    为当前显示的题目选择答案。
    单选题: answer = "A"/"B"/"C"/"D"  → 匹配 radioInput
    判断题: answer = "正确"/"错误"    → 匹配 radioText
    """
    try:
        if answer in ("正确", "错误"):
            opt = page.locator(f".radioText").filter(has_text=answer).first
            if await opt.count():
                await opt.scroll_into_view_if_needed()
                await opt.click(timeout=3000, force=True)
                return True
            # 兜底: 直接点整行 label
            lbl = page.locator(f".el-radio:has-text('{answer}')").first
            if await lbl.count():
                await lbl.click(timeout=3000, force=True)
                return True
        else:
            opt = page.locator(f".radioInput:text-is('{answer}')").first
            if await opt.count():
                await opt.scroll_into_view_if_needed()
                await opt.click(timeout=3000, force=True)
                return True
            # 兜底: 点包含该字母的 label
            lbl = page.locator(f".radioInput").filter(has_text=answer).first
            if await lbl.count():
                await lbl.click(timeout=3000, force=True)
                return True
        return False
    except Exception as e:
        log(f"    选择答案 {answer} 失败: {e}")
        return False


async def submit_quiz(page) -> bool:
    """点击提交按钮"""
    try:
        btn = page.locator("button:has-text('提交')").first
        if await btn.count():
            # 检查是否可用
            disabled = await btn.is_disabled()
            if disabled:
                log(f"    提交按钮不可用 (可能还有未答的题)")
                return False
            await btn.scroll_into_view_if_needed()
            await btn.click(timeout=5000)
            await page.wait_for_timeout(2000)
            return True
    except Exception:
        pass
    return False


async def process_quiz(page, quiz_title: str, answers: list[str]) -> bool:
    """
    进入 quiz 后逐题答题并提交。
    answers: [ans1, ans2, ...] 每个元素是 "A"/"正确" 等
    """
    log(f"  开始答题: {quiz_title} ({len(answers)} 题)")

    # 等待侧边栏加载
    try:
        await page.wait_for_selector(".subject-item", timeout=15000)
    except Exception:
        log(f"  未检测到题目列表")
        return False

    # 获取题数
    sidebar = page.locator("[class*='aside'] .subject-item, .aside-body .subject-item, .list-inline .subject-item")
    total = await sidebar.count()
    log(f"  共 {total} 题, 准备 {len(answers)} 个答案")

    actual = min(total, len(answers))

    for q_idx in range(actual):
        # 点击侧边栏题号
        si = sidebar.nth(q_idx)
        try:
            await si.click(timeout=5000)
            await page.wait_for_timeout(1500)
        except Exception:
            log(f"  第 {q_idx+1} 题导航失败")
            continue

        ans = answers[q_idx]
        ok = await answer_question(page, ans, q_idx)
        status = "✓" if ok else "✗"
        log(f"    第 {q_idx+1} 题 → {ans} {status}")

    # 提交
    log(f"  提交中...")
    sub_ok = await submit_quiz(page)
    if sub_ok:
        log(f"  ✓ {quiz_title}: 已提交")
    else:
        # 可能是弹窗确认, 再试一次
        await page.wait_for_timeout(1000)
        sub_ok = await submit_quiz(page)
        if sub_ok:
            log(f"  ✓ {quiz_title}: 已提交")
        else:
            log(f"  ⚠ {quiz_title}: 需手动确认提交")

    return True


# ═══════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════

async def main():
    log("=" * 50)
    log("雨课堂 自动答题提交工具")
    log("=" * 50)

    # 加载答案
    if not ANSWERS_FILE.exists():
        log(f"答案文件不存在: {ANSWERS_FILE}")
        sys.exit(1)
    answers_map = parse_answers(ANSWERS_FILE)
    log(f"已加载 {len(answers_map)} 个 Quiz 的答案:")
    for name, ans in answers_map.items():
        log(f"  {name}: {len(ans)} 题")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=HEADLESS,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            locale="zh-CN",
        )

        cookie_loaded = await load_cookies(context)
        page = await context.new_page()
        page.set_default_timeout(30000)

        # 打开课程页, 让用户登录
        await page.goto(COURSE_URL, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(2000)

        log("→ 浏览器已打开, 请手动完成登录并确认课程页面已加载")
        input("  完成后请按 Enter 继续...")
        await save_cookies(context)

        # 展开所有章节
        log("展开所有章节...")
        await page.evaluate("""
            () => {
                document.querySelectorAll('.chapter-list .content').forEach(el => {
                    if (el.style.display === 'none') el.style.display = 'block';
                });
            }
        """)
        await page.wait_for_timeout(1500)

        # 发现 Quiz
        quizzes = await find_quiz_items(page)
        log(f"共发现 {len(quizzes)} 个 Quiz")

        if not quizzes:
            log("未找到 Quiz")
            await browser.close()
            return

        # 逐个答题
        for idx, (quiz_el, title) in enumerate(quizzes):
            answers = answers_map.get(title)
            if not answers:
                log(f"\n[{idx+1}/{len(quizzes)}] {title}: 无答案, 跳过")
                continue

            log(f"\n[{idx+1}/{len(quizzes)}] {title}")

            ok = await click_quiz_item(quiz_el)
            if not ok:
                log(f"  进入失败")
                continue

            await page.wait_for_timeout(2000)

            # 判断是否进入 quiz 页
            if await page.locator(".subject-item").first.count():
                await process_quiz(page, title, answers)
            elif len(context.pages) > 1:
                quiz_page = context.pages[-1]
                await quiz_page.wait_for_load_state("domcontentloaded")
                await quiz_page.wait_for_timeout(2000)
                await process_quiz(quiz_page, title, answers)
                await quiz_page.close()
            else:
                log(f"  进入 quiz 失败")

            # 返回课程页
            try:
                await page.goto(COURSE_URL, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_timeout(2000)
                # 重新展开
                await page.evaluate("""
                    () => {
                        document.querySelectorAll('.chapter-list .content').forEach(el => {
                            if (el.style.display === 'none') el.style.display = 'block';
                        });
                    }
                """)
            except Exception:
                pass

        log("\n" + "=" * 50)
        log("全部完成!")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
