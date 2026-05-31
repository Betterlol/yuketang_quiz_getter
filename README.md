# 雨课堂 Quiz 题库自动收集工具

自动提取雨课堂课程中的所有 Quiz 题目，汇总导出为 Markdown。

## 功能

- 自动发现课程页面中的所有 Quiz 条目
- 逐个进入 Quiz 提取全部题目（题干 + 选项 + 题型）
- 支持单选、多选、判断、填空等常见题型
- Cookie 持久化：首次登录后自动保存，后续免登录
- 导出为结构化 Markdown

## 用法

```bash
# 安装依赖
pip install playwright
playwright install chromium

# 运行
python auto.py
```

首次运行会打开浏览器，请手动登录雨课堂并导航到目标课程页面，然后在终端按 Enter 继续。脚本自动扫描并提取所有 Quiz。

## 文件说明

| 文件 | 说明 |
|---|---|
| `auto.py` | 主程序 |
| `yuketang_questions.md` | 导出的题库 |
| `yuketang_cookies.json` | 登录 Cookie（自动生成，已 gitignore） |

## 输出示例

```markdown
### Q1 [1.单选题 (1分)]

Which principle suggests that catching a bug earlier in the development process is the most cost-effective?

- A. Scale
- B. No Silver Bullet
- C. Shift Left
- D. Hyrum's Law

---

### Q2 [2.判断题 (1分)]

Software engineering is defined solely as the act of writing code.

---
```
