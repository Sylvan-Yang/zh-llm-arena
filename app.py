# app.py
# =====================================================================
#  这是整个产品“跑起来”的地方——也就是用户打开网页看到的东西。
#  我们用 Streamlit：它让你用纯 Python 写网页，不用学 HTML/CSS/JS。
#  类比：prompts_data.py 是题库，elo.py 是算分裁判，app.py 是把它们
#        组装成一个“能打开、能点、能投票”的网页应用。
#
#  怎么跑起来？（详细见 SETUP.md）
#    1) 装好依赖：pip install -r requirements.txt
#    2) 启动：    streamlit run app.py
#    3) 浏览器会自动打开一个本地网页，就能玩了。
# =====================================================================

import os
import random
import streamlit as st
from datetime import datetime

import prompts_data
import elo

# 投票记录存到项目根目录的 votes.csv。用绝对路径，避免“找不到文件”。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOTES_FILE = os.path.join(BASE_DIR, "votes.csv")


# ---------- 1. 读写投票记录 ----------
def load_votes():
    """把 votes.csv 读进来，返回一堆 dict（每行是一条投票）。文件不存在就返回空列表。"""
    if not os.path.exists(VOTES_FILE):
        return []
    import pandas as pd
    return pd.read_csv(VOTES_FILE).to_dict("records")


def save_vote(row: dict):
    """把一票追加写进 votes.csv。"""
    import pandas as pd
    new_df = pd.DataFrame([row])
    if os.path.exists(VOTES_FILE):
        old = pd.read_csv(VOTES_FILE)
        new_df = pd.concat([old, new_df], ignore_index=True)
    new_df.to_csv(VOTES_FILE, index=False)


# ---------- 2. 盲测时给两个模型“随机左右”，避免位置偏见 ----------
def reshuffle(prompt_id: str):
    """随机决定这道题目的两个回答，哪个放左边(A)、哪个放右边(B)。
    类比：考试时把答卷 A/B 随机排位置，防止大家习惯性都选左边。
    """
    ans = prompts_data.SEED_ANSWERS.get(prompt_id, {})
    models = list(ans.keys())
    if len(models) < 2:
        st.session_state["assignment"] = None
        return
    a, b = models[0], models[1]
    if random.random() < 0.5:
        a, b = b, a
    st.session_state["assignment"] = {"prompt_id": prompt_id, "left": a, "right": b}


# ================= 页面开始 =================
st.set_page_config(page_title="中文 LLM 盲测擂台", page_icon="🥊")
st.title("🥊 中文 LLM 盲测擂台 · zh-llm-arena")
st.caption("同一道题，两个匿名模型作答，你盲投更优者 → 实时算出 Elo 排行榜。")

# 左侧导航：去投票 / 看排行榜
page = st.sidebar.radio("导航", ["去盲测投票", "看 Elo 排行榜"])

# ---------- 页面 A：盲测投票 ----------
if page == "去盲测投票":
    st.header("🗳 盲测投票")

    # 只列出“已经有模型回答”的题目，没回答的先不显示
    votable = [p for p in prompts_data.PROMPTS if p["id"] in prompts_data.SEED_ANSWERS]
    cats = sorted(set(p["category"] for p in votable))

    cat = st.selectbox("① 先选一个类别", cats)
    opts = [p for p in votable if p["category"] == cat]
    prompt_id = st.selectbox("② 再选一道题", [p["id"] for p in opts])

    # 题目变了就重新随机左右
    if st.session_state.get("current_prompt") != prompt_id:
        st.session_state["current_prompt"] = prompt_id
        reshuffle(prompt_id)

    # 找到这道题目的完整信息
    prompt = next(p for p in prompts_data.PROMPTS if p["id"] == prompt_id)
    st.markdown(f"**题目（{prompt['category']}）**：{prompt['text']}")

    assign = st.session_state.get("assignment")
    if not assign:
        st.warning("这道题还没有录入模型回答，换一道试试～")
    else:
        ans = prompts_data.SEED_ANSWERS[prompt_id]
        left, right = assign["left"], assign["right"]

        st.markdown("---")
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("模型 A")
            st.write(ans[left])
        with col_b:
            st.subheader("模型 B")
            st.write(ans[right])

        st.markdown("---")
        st.write("**你觉得哪个回答更好？**（不知道是谁，凭质量投）")
        c1, c2, c3 = st.columns(3)
        # 点了哪个按钮，就把那一票写进 csv，然后重新随机下一题的左右
        if c1.button("👈 A 更好", use_container_width=True):
            save_vote({"timestamp": datetime.now().isoformat(timespec="seconds"),
                       "prompt_id": prompt_id, "category": prompt["category"],
                       "model_a": left, "model_b": right, "winner": "A"})
            st.success("✅ 已记录：A 更好")
            reshuffle(prompt_id)
        if c2.button("🤝 平手 / 都差", use_container_width=True):
            save_vote({"timestamp": datetime.now().isoformat(timespec="seconds"),
                       "prompt_id": prompt_id, "category": prompt["category"],
                       "model_a": left, "model_b": right, "winner": "tie"})
            st.success("✅ 已记录：平手")
            reshuffle(prompt_id)
        if c3.button("B 更好 👉", use_container_width=True):
            save_vote({"timestamp": datetime.now().isoformat(timespec="seconds"),
                       "prompt_id": prompt_id, "category": prompt["category"],
                       "model_a": left, "model_b": right, "winner": "B"})
            st.success("✅ 已记录：B 更好")
            reshuffle(prompt_id)

        if st.button("🔀 重新随机左右（换种排法再看）"):
            reshuffle(prompt_id)

# ---------- 页面 B：Elo 排行榜 ----------
else:
    st.header("📊 Elo 排行榜")
    votes = load_votes()
    if not votes:
        st.info("还没有投票记录，去「去盲测投票」投几票，榜单就出来了～")
    else:
        lb = elo.compute_leaderboard(votes)
        st.caption(f"当前共 {len(votes)} 票。分数越高越强，初始均为 1500。")
        import pandas as pd
        df = pd.DataFrame(lb)
        df = df.rename(columns={
            "model": "模型", "rating": "Elo", "matches": "场次",
            "wins": "胜", "losses": "负", "ties": "平", "win_rate": "胜率",
        })
        df["胜率"] = (df["胜率"] * 100).round(1).astype(str) + "%"
        st.dataframe(df[["模型", "Elo", "场次", "胜", "负", "平", "胜率"]],
                     use_container_width=True)
        st.subheader("Elo 分数对比")
        chart_df = pd.DataFrame(lb).set_index("model")[["rating"]]
        st.bar_chart(chart_df)
