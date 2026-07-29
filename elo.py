# elo.py
# =====================================================================
#  Elo 评分算法。它原来是用来给国际象棋选手排名的，现在被搬到 LLM 擂台赛上。
#
#  核心思想（用打羽毛球积分赛来类比）：
#    - 每个模型开始都有 1500 分（同一起跑线）。
#    - 每场盲测就是一场“比赛”：赢了的加分，输了的减分，平手各不动。
#    - 关键：赢了“高分强者”涨得多，赢了“低分菜鸟”涨得少。
#      所以分数不是看你赢了几场，而是看你“赢了谁”。这比单纯算胜率更公平。
#
#  为什么不用“胜率”而用 Elo？（面试能讲的点）
#    胜率会被“对手强弱”影响——一直跟弱手打，胜率虚高。
#    Elo 把对手强度算进去了，所以两个模型分数可以直接比高低，跨题目也可比。
# =====================================================================

# 初始分数：所有模型从同一起跑线开始
INITIAL_RATING = 1500
# K 值：每场最多加减多少分。K 越大，分数变得越快（更敏感但也更抖）。
K_FACTOR = 32


def expected_score(rating_a: float, rating_b: float) -> float:
    """A 对 B 的“期望胜率”。返回 0~1 之间的数。

    公式：E_A = 1 / (1 + 10^((R_B - R_A) / 400))
    类比：你 1500 分，对手 1500 分 → 期望胜率 0.5（五五开）。
          你 1600 分，对手 1500 分 → 期望胜率约 0.64（你更被看好）。
    """
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update_ratings(rating_a: float, rating_b: float, score_a: float):
    """根据一场比赛结果，更新 A、B 两人的分数。

    参数 score_a：
        1.0  → A 赢
        0.0  → A 输（即 B 赢）
        0.5  → 平手
    """
    exp_a = expected_score(rating_a, rating_b)
    exp_b = expected_score(rating_b, rating_a)  # 等于 1 - exp_a

    new_a = rating_a + K_FACTOR * (score_a - exp_a)
    new_b = rating_b + K_FACTOR * ((1 - score_a) - exp_b)
    return round(new_a, 1), round(new_b, 1)


def compute_leaderboard(votes):
    """从一堆投票记录里，算出每个模型的 Elo 排行榜。

    参数 votes：列表，每个元素是 dict，形如
        {"model_a": "豆包", "model_b": "文心一言", "winner": "A"}
        winner 取值："A" 表示左侧模型赢、"B" 表示右侧赢、"tie" 表示平手。

    返回：按分数从高到低排好的列表，每项含
        model（名字）、rating（分数）、matches（比赛场数）、wins / losses / ties。
    """
    ratings = {}      # 模型名 -> 当前分数
    matches = {}      # 模型名 -> 比赛场数
    record = {}       # 模型名 -> {"wins":, "losses":, "ties":}

    def ensure(model):
        if model not in ratings:
            ratings[model] = INITIAL_RATING
            matches[model] = 0
            record[model] = {"wins": 0, "losses": 0, "ties": 0}

    # 先保证所有出现过的模型都在表里
    for v in votes:
        ensure(v["model_a"])
        ensure(v["model_b"])

    # 一场一场“打”过去，更新分数和战绩
    for v in votes:
        a, b = v["model_a"], v["model_b"]
        if v["winner"] == "A":
            score_a = 1.0
            record[a]["wins"] += 1
            record[b]["losses"] += 1
        elif v["winner"] == "B":
            score_a = 0.0
            record[b]["wins"] += 1
            record[a]["losses"] += 1
        else:  # tie
            score_a = 0.5
            record[a]["ties"] += 1
            record[b]["ties"] += 1

        new_a, new_b = update_ratings(ratings[a], ratings[b], score_a)
        ratings[a] = new_a
        ratings[b] = new_b
        matches[a] += 1
        matches[b] += 1

    # 拼成排行榜，按分数降序
    leaderboard = []
    for model in ratings:
        rec = record[model]
        total = matches[model]
        win_rate = (rec["wins"] / total) if total else 0.0
        leaderboard.append({
            "model": model,
            "rating": ratings[model],
            "matches": total,
            "wins": rec["wins"],
            "losses": rec["losses"],
            "ties": rec["ties"],
            "win_rate": round(win_rate, 3),
        })
    leaderboard.sort(key=lambda x: x["rating"], reverse=True)
    return leaderboard
