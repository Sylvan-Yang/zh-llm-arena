# 中文 LLM 评测台 · zh-llm-arena

> 一个面向**中文大语言模型**的 A/B 盲测 + Elo 排行榜评测平台。
> Methodology inspired by [lmsys Chatbot Arena](https://chat.lmsys.org/) & [h2oai/h2o-LLM-eval](https://github.com/h2oai/h2o-LLM-eval) — 本地化重构并原创全部中文评测资产。

---

## 🎯 为什么做这个项目（Why）

市面上的 LLM 评测基准（MMLU、Chatbot Arena、H2O eval 等）**几乎全是英文**，且偏向研究导向。
但字节、百度、阿里、腾讯的核心业务都是**中文场景**，中文 LLM 缺少一个：

- **以真实用户体验为中心**（人盲测，而非纯 benchmark 跑分）
- **覆盖真实中文任务**（写作、翻译、长文、中文网络语境）
- **可复现、可演示、可参与** 的轻量评测平台。

本项目把业界成熟的 **Elo 评分 + A/B 盲测 + LLM-as-Judge** 方法论，**本地化落地到中国中文 LLM 场景**，
并用一套**原创中文 prompt 评测集**驱动真实投票，产出一份**可信的中文 LLM 体验排行榜**。

> 对产品岗的意义：这不是"复刻一个开源项目"，而是"把一套成熟评估方法论，迁移到一个真实但服务不足的市场"。

---

## 🧪 评测方法论（Methodology）

| 机制 | 说明 |
|---|---|
| **A/B 盲测** | 同一中文 prompt，并排展示两个匿名模型的回答，用户盲选更优者（可选"平手/都差"） |
| **Elo 评分** | 用国际象棋 Elo 算法聚合全部盲测投票，产出模型相对排名（参考 lmsys 的实现思路） |
| **LLM-as-Judge** | 可选：用强模型作为裁判，对回答按"正确性/有用性/表达/指令遵循"打分，作为人工票的补充 |
| **分类别榜单** | 总榜 + 6 个分类榜（写作/推理/编码/数学/翻译/长文），看模型"偏科"情况 |

> 设计取舍与辩护（面试可讲）：为什么用 Elo 而不是胜率？为什么保留"平手/都差"？裁判 prompt 怎么写才防偏见？——见 `docs/design-decisions.md`（TODO）

---

## ✨ 功能（Features）

- [x] 中文 prompt 评测集（6 类 × 5 条 = 30 题，持续扩充）—— 见 `prompts/zh-prompts-v1.md`
- [x] 匿名 A/B 盲测投票界面（4 模型随机对战，智能代码渲染）—— 见 `app.py`
- [x] Elo 实时排行榜（总榜 + 6 类分榜 + 能力雷达矩阵）—— 见 `app.py` + `elo.py`
- [x] 自动推荐总结（基于品类冠军，自然语言推荐"你该选哪个模型"）
- [ ] 接真实 LLM API 自动生成回答（替换 mock 数据）
- [ ] LLM-as-Judge 自动评分 + 裁判说明
- [ ] 胜率矩阵 / 趋势图
- [ ] 一键分享单次盲测结果

---

## 🗂 中文评测集（The Prompt Set）

**这是本项目的核心原创资产。** 6 大类别，覆盖中文真实使用场景：

| 类别 | 考察点 |
|---|---|
| 写作 Writing | 中文表达、风格迁移、文案/创作能力 |
| 推理 Reasoning | 逻辑链、常识与多步推理 |
| 编码 Coding | 代码正确性、边界处理、解释能力 |
| 数学 Math | 计算正确性、应用题建模、证明表达 |
| 翻译 Translation | 中英互译、意译、术语与文化负载词 |
| 长文理解 Long-context | 跨段落定位、摘要、信息抽取 |

完整题目与判分点 → [`prompts/zh-prompts-v1.md`](prompts/zh-prompts-v1.md)

---

## 🏗 技术栈（Tech Stack）

- 前端/应用：Streamlit（纯 Python 写界面，零基础也能跑）
- 数据存储：本地 `votes.csv`（MVP 阶段够用；多人后再换 Supabase）
- 评测模型：国产主流中文 LLM API（如 豆包 / 通义 / 文心 / DeepSeek / Kimi …），MVP 先用静态 mock 回答跑通闭环
- 评分：Elo 算法（自实现，见 `elo.py`）+ LLM-as-Judge（TODO）

---

## 🚀 快速开始（Quickstart）

> 详细零基础步骤见 [`SETUP.md`](SETUP.md)。

```bash
pip install -r requirements.txt
streamlit run app.py
# 浏览器打开 http://localhost:8501
```

---

## 📊 在线演示与排行榜（Demo & Leaderboard）

- 🚀 **在线体验**：[zh-llm-arena.streamlit.app](https://zh-llm-arena-cnhryluhqog2myjhxtt7id.streamlit.app)
- 中文 LLM 体验排行榜：(待收集真实盲测数据后发布)

---

## 🗺 路线图（Roadmap）

- [x] 中文评测集 v1（6 类 × 30 条）
- [x] A/B 盲测 MVP（投票 + Elo 排行榜，本地可跑）
- [x] 4 模型完整回答数据（豆包 / 文心一言 / DeepSeek / 通义千问）
- [x] 6 大类别分榜 + 能力雷达矩阵 + 自动推荐
- [ ] 接真实 LLM API 自动生成回答（替换 mock 数据）
- [ ] LLM-as-Judge
- [ ] 收集首批真实盲测数据并发布榜单
- [ ] 部署上线（Streamlit Community Cloud）

---

## 🙏 致谢与声明（Acknowledgements & Attribution）

本项目**方法论**参考并致敬以下公开工作，**代码与中文评测资产均为本人原创**：

- **lmsys Chatbot Arena** — Elo + A/B 盲测的开创性实践
- **h2oai/h2o-LLM-eval** — Elo 排行榜 + GPT 裁判的开源实现参考
- **Elo Rating System** — 国际象棋评分算法

> 说明：Elo / A/B 盲测 / LLM-as-Judge 均为业界公开方法论。本项目未复制上述仓库代码，
> 而是面向中文市场重新实现，并原创全部中文 prompt 评测集与产品化设计。

---

## 📄 License

MIT
