# 🤝 贡献指南（CONTRIBUTING）

欢迎来一起把「中文 LLM 盲测擂台」做得更好！这个项目刻意保持**轻量、零基础友好**，所以贡献门槛很低。

## 一、加一道评测题（最有价值）

1. 打开 [`prompts/zh-prompts-v1.md`](prompts/zh-prompts-v1.md)，在对应的类别表格里加一行。
2. 同时打开 [`prompts_data.py`](prompts_data.py)，在 `PROMPTS` 列表里加一条：
   ```python
   {"id": "W6", "category": "写作", "text": "你的题目……", "judge": "判分维度"}
   ```
3. 题目请遵循三原则：**区分度**（能拉开模型差距）、**可判分**（客观题给参考答案，主观题给维度）、**贴真实中文场景**。

## 二、给题目补“模型回答”

目前 `prompts_data.py` 里的 `SEED_ANSWERS` 只有 5 道题有回答。你有两个办法：

- **手动（零代码）**：去豆包 / 文心一言 / DeepSeek / Kimi 的网页版，把同一道题问一遍，把回答复制进 `SEED_ANSWERS[prompt_id]`。
- **自动（进阶）**：写几行代码调各家 API 生成，替换 mock 数据来源（结构不用动）。

## 三、本地跑起来

见 [`SETUP.md`](SETUP.md)，就三步：`pip install -r requirements.txt` → `streamlit run app.py` → 打开网址。

## 四、代码约定

- 注释用中文，面向“产品/零基础”读者，多用生活类比。
- 改动尽量小、可验证：改完跑一遍 `python -m py_compile app.py prompts_data.py elo.py`。
- 投票数据存在 `votes.csv`，**不要手改**，由应用自动写入。

## 五、提交规范

- 一个 PR 只做一件事（加题 / 修 bug / 加功能）。
- 标题用大白话，例如：`新增数学类 5 题的模型回答`、`修复平手时分数漂移`。
- 若是设计讨论，先在 `docs/design-decisions.md` 里补充你的取舍理由。

提 Issue、提 PR 都欢迎 🙌
