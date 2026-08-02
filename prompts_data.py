# prompts_data.py
# =====================================================================
#  这个文件就是“题库”。把所有评测题目集中放这里，app.py 只管“发卷”和“收票”。
#  类比：就像老师出题，题目都写在题库里，考试系统不用关心题目怎么想出来的，
#        它只负责把题发给学生、把答案收回来。
#
#  每条题目是一个“字典”（dict，可以理解成一张填好格子的表格）：
#    id      题目的编号，比如 W1、R2（写作第1题、推理第2题）
#    category 属于哪一类：写作 / 推理 / 编码 / 数学 / 翻译 / 长文理解
#    text    题目内容（真正拿去问模型的那个问题）
#    judge   判分维度 / 参考答案（人工或裁判模型打分时用）
# =====================================================================

PROMPTS = [
    # ---------- 1. 写作 Writing ----------
    {"id": "W1", "category": "写作",
     "text": "用 200 字以内，为一款面向大学生的「AI 简历优化工具」写一段朋友圈推广文案，要求：开头有 hook、点出痛点、结尾有行动号召。",
     "judge": "hook吸引力 / 痛点共鸣 / CTA明确 / 字数控制"},
    {"id": "W2", "category": "写作",
     "text": "把这句口语化表达改写成正式的产品需求文档（PRD）风格的一句话：\"这玩意儿就是让老板能随时看到大家干活进度。\"",
     "judge": "术语准确 / 正式度 / 信息无损"},
    {"id": "W3", "category": "写作",
     "text": "以“凌晨三点的写字楼”为开头，写一段不超过 150 字、有画面感的都市小说开头。",
     "judge": "意象 / 氛围 / 语言张力 / 字数"},
    {"id": "W4", "category": "写作",
     "text": "给一位刚被裁员的朋友写一段安慰的话，要求真诚、不说教、不灌鸡汤。",
     "judge": "真诚度 / 不说教 / 不空洞"},
    {"id": "W5", "category": "写作",
     "text": "为「618 大促」写三个不同风格的电商标题：①理性参数党 ②冲动种草党 ③性价比比价党。",
     "judge": "风格区分度 / 卖点贴合 / 标题吸引力"},

    # ---------- 2. 推理 Reasoning ----------
    {"id": "R1", "category": "推理",
     "text": "甲、乙、丙三人排队，甲不在最前，乙不在最后，丙在中间。请推出三人的前后顺序，并说明推理过程。",
     "judge": "前→后：乙、丙、甲；需展示逐步排除"},
    {"id": "R2", "category": "推理",
     "text": "一个水池，进水管单独开 4 小时注满，排水管单独开 6 小时排空。两管同时打开，几小时能注满？",
     "judge": "12 小时（1/4 − 1/6 = 1/12）"},
    {"id": "R3", "category": "推理",
     "text": "\"所有会飞的动物都是鸟\"这句话是假的。据此能必然推出以下哪项？A. 所有会飞的都不是鸟 B. 存在会飞但不是鸟的动物 C. 蝙蝠会飞但不是鸟 D. 鸟都会飞",
     "judge": "B（全称命题的否定是特称否定）"},
    {"id": "R4", "category": "推理",
     "text": "三个人只有一人说了真话。甲说“是乙干的”，乙说“不是我干的”，丙说“不是我干的”。已知这件事是丙干的，请问谁说了真话？",
     "judge": "乙说真话（甲假、乙真、丙假，自洽）"},
    {"id": "R5", "category": "推理",
     "text": "阅读下面这段话，指出其中最关键的一处逻辑漏洞：「我们产品上线后 DAU 涨了 20%，而同期我们做了版本更新，所以 DAU 增长一定是这次版本更新带来的。」",
     "judge": "混淆相关与因果（可能有季节/投放等其他变量）"},

    # ---------- 3. 编码 Coding ----------
    {"id": "C1", "category": "编码",
     "text": "用 Python 写一个函数，判断一个字符串是否为回文，忽略大小写和非字母字符。并说明时间复杂度。",
     "judge": "逻辑正确 / 处理非字母 / O(n) / 有示例"},
    {"id": "C2", "category": "编码",
     "text": "有表 orders(id, user_id, amount, created_at)，写一条 SQL，查出每个用户最近一笔订单的 amount。",
     "judge": "用 ROW_NUMBER 或相关子查询、取每用户 max(created_at) 对应行"},
    {"id": "C3", "category": "编码",
     "text": "用 JavaScript 实现一个防抖（debounce）函数，并说明一个真实应用场景。",
     "judge": "正确使用闭包+定时器 / 场景合理(如搜索联想)"},
    {"id": "C4", "category": "编码",
     "text": "找出并修复下面代码的 bug：def avg(nums): return sum(nums)/len(nums)  当传入空列表时会发生什么？如何修复？",
     "judge": "识别除零异常、给出空值处理方案"},
    {"id": "C5", "category": "编码",
     "text": "用 Python 实现一个 LRU 缓存（put/get 均摊 O(1)），并解释为什么能达到 O(1)。",
     "judge": "哈希表+双向链表(或OrderedDict) / 能讲清O(1)原理"},

    # ---------- 4. 数学 Math ----------
    {"id": "M1", "category": "数学",
     "text": "某商品先涨价 10%，再降价 10%，现价是原价的百分之几？",
     "judge": "99%（1.1 × 0.9 = 0.99）"},
    {"id": "M2", "category": "数学",
     "text": "同时抛两枚均匀骰子，点数之和为 8 的概率是多少？",
     "judge": "5/36"},
    {"id": "M3", "category": "数学",
     "text": "一个班 40 人，会游泳的 25 人，会骑车的 30 人，两样都会的 18 人。两样都不会的有几人？",
     "judge": "3 人（25+30−18=37，40−37=3）"},
    {"id": "M4", "category": "数学",
     "text": "等差数列前 10 项和为 100，前 20 项和为 300，求前 30 项和。",
     "judge": "600（S10,S20−S10,S30−S20 成等差：100,200,300）"},
    {"id": "M5", "category": "数学",
     "text": "请证明：√2 是无理数。",
     "judge": "反证法（设√2=p/q 最简，推出 p、q 同为偶，矛盾）"},

    # ---------- 5. 翻译 Translation ----------
    {"id": "T1", "category": "翻译",
     "text": "把“知行合一”翻译成英文，并解释为什么不能简单直译。",
     "judge": "译法合理(如 Unity of knowledge and action) / 解释到位"},
    {"id": "T2", "category": "翻译",
     "text": "中译英：\"这个项目的关键不在于技术多先进，而在于能否真正解决用户的痛点。\"",
     "judge": "地道 / 保留强调结构 / not...but..."},
    {"id": "T3", "category": "翻译",
     "text": "英译中：\"The model tends to hallucinate when the retrieval context is insufficient.\"",
     "judge": "hallucinate译“幻觉”、retrieval context译“检索上下文”"},
    {"id": "T4", "category": "翻译",
     "text": "把网络流行语“我真的会谢”翻译成能让外国朋友理解的英文，并保留其“无奈又好笑”的语气。",
     "judge": "传达反讽语气 / 自然(如 \"Thanks a lot... (sarcastic)\")"},
    {"id": "T5", "category": "翻译",
     "text": "把“己所不欲，勿施于人”先翻译成现代汉语，再翻译成英文。",
     "judge": "现代汉语准确 / 英文达意(近似 Golden Rule)"},

    # ---------- 6. 长文理解 Long-context ----------
    {"id": "L1", "category": "长文理解",
     "text": "【附：一篇约 2000 字的产品复盘文章】请用不超过 3 点，总结这次失败“最核心”的原因，并按重要性排序。",
     "judge": "提炼准确 / 排序合理 / 不漏关键点"},
    {"id": "L2", "category": "长文理解",
     "text": "【附：一份虚构《员工手册》节选，含考勤/报销/请假规则】员工周二请假半天，是否需要“直属上级 + HR”双审批？请引用手册条款作答。",
     "judge": "定位正确条款 / 结论与条款一致"},
    {"id": "L3", "category": "长文理解",
     "text": "【附：一份虚构公司四个季度经营数据长文本】哪个季度环比增速由正转负？可能原因是什么？",
     "judge": "季度判断正确 / 原因有文本依据"},
    {"id": "L4", "category": "长文理解",
     "text": "【附：一篇论文摘要+方法节选】作者用什么方法解决了问题 X？与方法 Y 的核心区别是什么？",
     "judge": "方法识别正确 / 区别抓得准"},
    {"id": "L5", "category": "长文理解",
     "text": "【附：一段多人会议纪要】请提取：①已达成共识的决策 ②遗留待办（含负责人）。",
     "judge": "决策/待办分类正确 / 负责人归属正确"},
]

# =====================================================================
#  SEED_ANSWERS：预先塞进去的“模型回答”，用于演示盲测闭环。
#  类比：考试系统刚上线，总得先有几份“样板答卷”才能让人投票玩起来。
#  这里我们只给 5 道题填了两个模型的回答（豆包 / 文心一言），其余题目显示“待补充”。
#
#  ⚠️ 真实项目里，这两个回答你不用自己写——去豆包、文心一言的网页版把同一道题
#     问一遍，把回答复制进来就行。这一步叫“采集 baseline 数据”。
#  以后想接真实 API 自动生成，也是替换这里的来源，结构不用动。
# =====================================================================

SEED_ANSWERS = {
    "C1": {
        "豆包": "def is_palindrome(s):\\n    cleaned = ''.join(ch.lower() for ch in s if ch.isalpha())\\n    return cleaned == cleaned[::-1]\\n时间复杂度 O(n)，n 为字符串长度。",
        "文心一言": "import re\\ndef is_palindrome(s):\\n    s = re.sub(r'[^a-zA-Z]', '', s).lower()\\n    return s == s[::-1]\\n复杂度为 O(n)，n 为字符串长度。",
    
    
                "DeepSeek": "def is_palindrome(s: str) -> bool:\\n    “““Return True if s is a palindrome, ignoring case and non-letters.”””\\n    filtered = [c.lower() for c in s if c.isalpha()]\\n    return filtered == filtered[::-1]\\n\\nTime complexity: O(n) where n = len(s). We traverse the string once for filtering (O(n)) and once for comparison (O(n)), giving O(2n) = O(n).\\nSpace: O(n) for the filtered list.\\n\\nEdge cases: empty string → True; string with no letters → True.",
                "通义千问": "def is_palindrome(s):\\n    # 只保留字母，转小写\\n    chars = [c.lower() for c in s if c.isalpha()]\\n    # 双指针比较\\n    left, right = 0, len(chars) - 1\\n    while left < right:\\n        if chars[left] != chars[right]:\\n            return False\\n        left += 1\\n        right -= 1\\n    return True\\n\\n复杂度 O(n)，只遍历一次。\\n例子：is_palindrome(“A man, a plan, a canal: Panama”) → True",},
    "C2": {
        "豆包": "SELECT o.user_id, o.amount\\nFROM orders o\\nINNER JOIN (\\n    SELECT user_id, MAX(created_at) as latest\\n    FROM orders\\n    GROUP BY user_id\\n) t ON o.user_id = t.user_id AND o.created_at = t.latest;\\n\\n-- 说明：子查询找出每个用户最近订单的时间，再 JOIN 回来取对应金额。也可以用 ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY created_at DESC) 然后取 rn=1 的行。",
        "文心一言": "-- 方法一：使用窗口函数（推荐，语义清晰）\\nSELECT user_id, amount AS latest_order_amount\\nFROM (\\n    SELECT user_id, amount,\\n           ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn\\n    FROM orders\\n) sub\\nWHERE rn = 1;\\n\\n-- 方法二：使用相关子查询\\nSELECT o1.user_id, o1.amount\\nFROM orders o1\\nWHERE o1.created_at = (\\n    SELECT MAX(o2.created_at)\\n    FROM orders o2\\n    WHERE o2.user_id = o1.user_id\\n);\\n\\n-- 注意事项：如果同一用户有两条订单创建时间完全相同，方法一会稳定返回其中一条，方法二可能返回多条，需根据业务场景处理。",
    
    
                "DeepSeek": "-- Using ROW_NUMBER() window function (standard approach)\\nWITH ranked AS (\\n    SELECT\\n        user_id,\\n        amount,\\n        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn\\n    FROM orders\\n)\\nSELECT user_id, amount\\nFROM ranked\\nWHERE rn = 1;\\n\\n-- Note: ROW_NUMBER() guarantees exactly one row per user even with timestamp ties.\\n-- Alternative: DISTINCT ON (PostgreSQL-specific, often faster)\\nSELECT DISTINCT ON (user_id) user_id, amount\\nFROM orders\\nORDER BY user_id, created_at DESC;",
                "通义千问": "-- 方案：先找每个user最近时间，再取对应记录\\nSELECT o.user_id, o.amount\\nFROM orders o\\nWHERE o.created_at = (\\n    SELECT MAX(created_at)\\n    FROM orders\\n    WHERE user_id = o.user_id\\n);\\n\\n-- 说明：如果同一用户有多笔订单时间完全相同，会返回多条。生产环境建议用ROW_NUMBER()做去重。",},
    "C3": {
        "豆包": "function debounce(fn, delay) {\\n  let timer = null;\\n  return function(...args) {\\n    clearTimeout(timer);\\n    timer = setTimeout(() => fn.apply(this, args), delay);\\n  };\\n}\\n// 经典场景：搜索框输入联想，用户打字时不断重置定时器，停手 delay 毫秒后才真正发请求，避免每次按键都调接口。",
        "文心一言": "/**\\n * 防抖函数：在事件被连续触发时，只执行最后一次\\n * @param {Function} fn - 需要防抖的函数\\n * @param {number} delay - 延迟时间（毫秒）\\n * @param {boolean} immediate - 是否在首次触发时立即执行\\n * @returns {Function} 包装后的防抖函数\\n */\\nfunction debounce(fn, delay, immediate = false) {\\n    let timer = null;\\n    return function (...args) {\\n        const context = this;\\n        const callNow = immediate && !timer;\\n        clearTimeout(timer);\\n        timer = setTimeout(() => {\\n            timer = null;\\n            if (!immediate) fn.apply(context, args);\\n        }, delay);\\n        if (callNow) fn.apply(context, args);\\n    };\\n}\\n\\n// 典型应用场景：\\n// 1. 搜索输入框联想（input 事件）—— 用户停止输入后才发 API 请求\\n// 2. 窗口 resize 事件 —— 只在用户停止拖拽后重新计算布局\\n// 3. 按钮防重复提交 —— 防止用户连续点击导致多次请求",
    
    
                "DeepSeek": "/**\\n * Creates a debounced version of fn that delays invocation\\n * until after `delay` ms have elapsed since the last call.\\n */\\nfunction debounce(fn, delay) {\\n    let timeoutId = null;\\n    return function debounced(...args) {\\n        clearTimeout(timeoutId);\\n        timeoutId = setTimeout(() => fn.apply(this, args), delay);\\n    };\\n}\\n\\n// Use case: search-as-you-type. User types “hello”, we don't fire 5 API calls.\\n// Instead, we wait 300ms after the last keystroke, then send one request.\\nconst search = debounce(query => fetch(`/api/search?q=${query}`), 300);",
                "通义千问": "// 简洁版防抖函数\\nfunction debounce(fn, wait) {\\n    let timer;\\n    return function(...args) {\\n        clearTimeout(timer);\\n        timer = setTimeout(() => fn.apply(this, args), wait);\\n    };\\n}\\n\\n// 应用场景：\\n// 1. 搜索框输入联想，用户停止打字后才发请求\\n// 2. 窗口 resize，避免频繁计算\\n// 3. 提交按钮防重复点击",},
    "C4": {
        "豆包": "Bug：传入空列表时 len(nums) = 0，会导致除零错误 ZeroDivisionError。\\n\\n修复方案：\\ndef avg(nums):\\n    if not nums:\\n        return 0  # 或 raise ValueError(“列表不能为空”)\\n    return sum(nums) / len(nums)",
        "文心一言": "问题分析：\\n当 nums 为空列表 [] 时，len(nums) 返回 0，表达式 sum(nums) / len(nums) 会触发 ZeroDivisionError，这是典型的边界条件处理缺失。\\n\\n修复方案（根据业务场景选择）：\\n\\ndef avg(nums):\\n    “““计算列表的平均值\\n    Args:\\n        nums: 数字列表\\n    Returns:\\n        平均值；空列表返回 None\\n    ”””\\n    if not nums:\\n        return None\\n    return sum(nums) / len(nums)\\n\\n# 补充说明：\\n# 1. 返回 None 比返回 0 更安全——0 可能是有效平均值（如 [-1, 1]），不会被误读\\n# 2. 也可以选择抛异常 raise ValueError(“Cannot compute average of empty list”)，让调用方显式处理",
    
    
                "DeepSeek": "Bug: ZeroDivisionError when nums is empty (len(nums) = 0).\\n\\nFix — return a sentinel value or raise explicitly:\\n\\ndef avg(nums):\\n    if not nums:\\n        return None  # None signals “no meaningful average”\\n    return sum(nums) / len(nums)\\n\\nWhy None over 0?\\n- avg([-1, 0, 1]) = 0 is a valid result; returning 0 for empty would be ambiguous.\\n- Caller can distinguish “no data” from “average is zero” via `if avg(nums) is None`.",
                "通义千问": "Bug：传入空列表时，len(nums)=0，触发除零错误。\\n\\n修复：\\ndef avg(nums):\\n    if not nums:\\n        return 0  # 空列表返回0，符合直觉\\n    return sum(nums) / len(nums)\\n\\n也可以：\\ndef avg(nums):\\n    if len(nums) == 0:\\n        raise ValueError(“列表不能为空”)\\n    return sum(nums) / len(nums)",},
    "C5": {
        "豆包": "用 Python 的 OrderedDict 最简单：\\n\\nfrom collections import OrderedDict\\n\\nclass LRUCache:\\n    def __init__(self, capacity):\\n        self.cap = capacity\\n        self.cache = OrderedDict()\\n\\n    def get(self, key):\\n        if key not in self.cache:\\n            return -1\\n        self.cache.move_to_end(key)  # 标记最近使用\\n        return self.cache[key]\\n\\n    def put(self, key, value):\\n        if key in self.cache:\\n            self.cache.move_to_end(key)\\n        self.cache[key] = value\\n        if len(self.cache) > self.cap:\\n            self.cache.popitem(last=False)  # 弹出最久未用\\n\\n# OrderedDict 内部是双向链表+哈希表，move_to_end/popitem 都是 O(1)，所以整体 O(1)。",
        "文心一言": "实现思路：哈希表 + 双向链表。哈希表负责 O(1) 查找，双向链表负责 O(1) 维护访问顺序。\\n\\nclass Node:\\n    def __init__(self, key=0, value=0):\\n        self.key = key\\n        self.value = value\\n        self.prev = None\\n        self.next = None\\n\\nclass LRUCache:\\n    def __init__(self, capacity: int):\\n        self.capacity = capacity\\n        self.cache = {}  # key -> Node\\n        # 哨兵节点简化边界处理\\n        self.head = Node()\\n        self.tail = Node()\\n        self.head.next = self.tail\\n        self.tail.prev = self.head\\n\\n    def _remove(self, node):\\n        “““从链表中移除节点”””\\n        node.prev.next = node.next\\n        node.next.prev = node.prev\\n\\n    def _add_to_head(self, node):\\n        “““将节点插入到头部（标记为最近使用）”””\\n        node.next = self.head.next\\n        node.prev = self.head\\n        self.head.next.prev = node\\n        self.head.next = node\\n\\n    def get(self, key: int) -> int:\\n        if key not in self.cache:\\n            return -1\\n        node = self.cache[key]\\n        self._remove(node)\\n        self._add_to_head(node)\\n        return node.value\\n\\n    def put(self, key: int, value: int):\\n        if key in self.cache:\\n            self._remove(self.cache[key])\\n        node = Node(key, value)\\n        self.cache[key] = node\\n        self._add_to_head(node)\\n        if len(self.cache) > self.capacity:\\n            # 移除尾部节点（最久未使用）\\n            lru = self.tail.prev\\n            self._remove(lru)\\n            del self.cache[lru.key]\\n\\n时间复杂度分析：\\n- get: 哈希表查找 O(1)，链表操作 O(1)，总 O(1)\\n- put: 哈希表插入/更新 O(1)，链表操作 O(1)，删除 O(1)，总 O(1)\\n双向链表保证了在已知节点引用时，删除操作无需遍历。",
    
    
                "DeepSeek": "Implementation using OrderedDict (leverages internal doubly-linked list):\\n\\nfrom collections import OrderedDict\\n\\nclass LRUCache:\\n    def __init__(self, capacity: int):\\n        self.capacity = capacity\\n        self.cache = OrderedDict()  # preserves insertion order\\n\\n    def get(self, key: int) -> int:\\n        if key not in self.cache:\\n            return -1\\n        self.cache.move_to_end(key)  # O(1)\\n        return self.cache[key]\\n\\n    def put(self, key: int, value: int) -> None:\\n        if key in self.cache:\\n            self.cache.move_to_end(key)\\n        self.cache[key] = value\\n        if len(self.cache) > self.capacity:\\n            self.cache.popitem(last=False)  # FIFO pop, O(1)\\n\\nWhy O(1)? OrderedDict is implemented as a hash table + doubly-linked list. move_to_end() updates pointers in O(1); popitem(last=False) removes the head in O(1).",
                "通义千问": "用哈希表+双向链表实现：\\n\\nclass ListNode:\\n    def __init__(self, key=0, val=0):\\n        self.key = key\\n        self.val = val\\n        self.prev = self.next = None\\n\\nclass LRUCache:\\n    def __init__(self, capacity):\\n        self.cap = capacity\\n        self.map = {}\\n        self.head = ListNode()  # dummy head\\n        self.tail = ListNode()  # dummy tail\\n        self.head.next = self.tail\\n        self.tail.prev = self.head\\n\\n    def _move_to_front(self, node):\\n        # remove from current position\\n        node.prev.next = node.next\\n        node.next.prev = node.prev\\n        # insert after head\\n        node.next = self.head.next\\n        node.prev = self.head\\n        self.head.next.prev = node\\n        self.head.next = node\\n\\n    def get(self, key):\\n        if key not in self.map:\\n            return -1\\n        node = self.map[key]\\n        self._move_to_front(node)\\n        return node.val\\n\\n    def put(self, key, value):\\n        if key in self.map:\\n            node = self.map[key]\\n            node.val = value\\n            self._move_to_front(node)\\n        else:\\n            node = ListNode(key, value)\\n            self.map[key] = node\\n            self._move_to_front(node)\\n            if len(self.map) > self.cap:\\n                lru = self.tail.prev\\n                del self.map[lru.key]\\n                lru.prev.next = self.tail\\n                self.tail.prev = lru.prev\\n\\n时间复杂度：哈常表查找+链表操作均 O(1)。",},
    "L1": {
        "豆包": "三大核心原因：\\U0001f51d 定位失误——想做“所有人的工具”，结果没人觉得非用不可，没有聚焦核心用户群；\\U0001f522 上线太赶——为了追风口把半成品推上线，体验拉胯，口碑直接崩了；\\U0001f4b0 变现路径不清晰——免费获客但始终找不到付费点，烧钱模式撑不到拐点。排序按因果关系：定位错\\u2192产品糙\\u2192商业死。",
        "文心一言": "根据复盘文章，失败最核心的三个原因按重要性排序如下：\\n\\n1. 产品定位模糊——团队试图同时服务个人用户与企业客户，导致功能设计既要轻量又要专业，两端都不讨好。这是根本性的战略失误，决定了后续所有问题的走向。\\n\\n2. 过早追求增长而非留存——在产品尚未验证核心价值（PMF）时，就将大量资源投入投放和裂变，DAU虚高但次日留存率仅 12%。增长掩盖了产品问题。\\n\\n3. 团队内部认知不统一——创始人坚持“工具应免费”，运营负责人主张付费订阅，产品经理想做广告变现，三方拉锯浪费了三个月的决策窗口期。",
    
    
                "DeepSeek": "Top 3 failure causes, ranked:\\n\\n1. **No clear ICP (Ideal Customer Profile).** The product tried to serve both individual users and enterprise clients simultaneously, resulting in a feature set that satisfied neither. This is the root cause — all downstream issues trace back here.\\n\\n2. **Growth before PMF.** The team scaled user acquisition (ads, viral loops) when 7-day retention was only 12%. Vanity metrics masked the core problem: users didn't stick around because the product didn't solve a sharp enough pain.\\n\\n3. **Decision paralysis at leadership.** Founder insisted on free; COO pushed subscription; PM wanted ads. Three months of debate with no A/B test, no data — just opinions. Speed of decision matters more than perfect decisions in early-stage.",
                "通义千问": "核心失败原因（按重要性排序）：\\n\\n1. “定位太宽”——想一口气吃下个人和企业两个市场，结果哪边都没做深，用户觉得“可有可无”。\\n\\n2. “没跑通就放量”——产品还没验证PMF就大量烧钱拉新，DAU虚高但留存崩了。\\n\\n3. “内部拉锯”——创始人、运营、产品三方意见不统一，浪费三个月没做出决策。",},
    "L2": {
        "豆包": "不需要双审批。根据手册第三章第 2.3 条：半天以内（含半天）的请假只需直属上级审批；超过半天才需直属上级 + HR 双审批。周二请假半天符合第 2.3 条的“半天以内”条件，直属上级审批即可。",
        "文心一言": "不需要直属上级+HR双审批。\\n\\n依据：《员工手册》第三章“考勤与请假”第 2.3 条规定：\\n- 请假半天（含）以内：仅需直属上级审批\\n- 请假超过半天但不超过 2 天：需直属上级 + 部门负责人双审批\\n- 请假超过 2 天：需直属上级 + 部门负责人 + HR 三审批\\n\\n题干中员工请假半天，属于第 2.3 条第一款规定的情形，仅需直属上级审批即可，无需 HR 参与。",
    
    
                "DeepSeek": "No, only one-level approval is needed.\\n\\nPer Handbook Chapter 3, Section 2.3:\\n- Leave ≤ 0.5 day: direct supervisor only\\n- 0.5 < Leave ≤ 2 days: supervisor + department head\\n- Leave > 2 days: supervisor + department head + HR\\n\\nThe employee requested exactly 0.5 day (Tuesday half-day), which falls under the first tier. Direct supervisor approval suffices; HR involvement is not required.",
                "通义千问": "不需要双审批，只需直属上级审批。\\n\\n根据《员工手册》第三章第2.3条：请假半天以内只需直属上级审批。员工周二请假半天，符合该条款，无需HR参与。",},
    "L3": {
        "豆包": "Q2 季度环比增速由正转负。Q1 环比 +12%，Q2 环比 −3%。可能原因：材料中提到 Q2 核心客户流失 + 竞品大幅降价抢市场，加上 Q1 是春节旺季、Q2 是淡季的行业规律叠加影响。",
        "文心一言": "Q2（第二季度）环比增速由正转负，Q1 环比增长率为 +12%，Q2 降至 \\u22123%。\\n\\n可能原因（均有文本依据）：\\n1. 外部因素：竞品在 4 月中旬发起大规模价格战（材料第 5 段），导致公司被迫降价应对，营收承压。\\n2. 内部因素：Q2 流失了 3 个头部客户（材料第 7 段表格），这几家客户合计贡献 Q1 营收的 22%。\\n3. 周期因素：公司业务有 Q1 春节旺季效应，Q2 通常是季节性回调，但今年叠加了前两个因素，回调幅度远超往年。",
    
    
                "DeepSeek": "Q2 turned negative. Q1: +12% QoQ → Q2: −3% QoQ.\\n\\nLikely drivers (all grounded in the text):\\n1. Competitor price war launched mid-April (para 5), forcing margin compression.\\n2. Loss of 3 key accounts (para 7), together representing 22% of Q1 revenue.\\n3. Seasonal pattern: Q1 typically benefits from Chinese New Year peak; Q2 is a seasonal trough. The unusual magnitude of the decline this year suggests the first two factors amplified the seasonal effect.",
                "通义千问": "Q2季度环比增速由正转负。Q1 +12%，Q2 -3%。\\n\\n可能原因：\\n1. 竞品4月发起价格战，公司被迫跟进降价；\\n2. Q2流失3个大客户，这些客户占Q1营收的22%；\\n3. Q1是春节旺季，Q2是淡季，叠加前两个因素后回调幅度超常。",},
    "L4": {
        "豆包": "作者用的是对比学习（Contrastive Learning）+ 数据增强的方法。跟方法 Y（传统监督学习）的核心区别是：不需要大量人工标注数据，靠构造正负样本对让模型自己学特征表示，在少样本场景下效果明显更好。",
        "文心一言": "作者采用的方法是“基于对比学习的无监督预训练 + 下游微调”框架（见论文第 3.1-3.2 节），具体包括：随机数据增强构造正样本对、InfoNCE 损失函数训练编码器、以及一个针对任务 X 设计的专用数据增强策略。\\n\\n与方法 Y（基于传统监督学习的方法）的核心区别：\\n1. 数据依赖：方法 Y 依赖大量人工标注，本文方法仅需无标注原始数据即可进行强表征预训练；\\n2. 泛化能力：在低资源场景（标注数据仅 10% 可用）下，本文方法准确率高出 Y 约 8.3 个百分点（见论文表 2）；\\n3. 训练范式：Y 是端到端监督学习，本文是“预训练\\u2192微调”的两阶段范式，先学到通用特征再适配具体任务。",
    
    
                "DeepSeek": "The authors use a **contrastive self-supervised pre-training** framework with custom data augmentations, followed by task-specific fine-tuning.\\n\\nKey differences from Method Y (supervised baseline):\\n1. **Label dependency**: Y requires large-scale human annotations; this method learns representations from unlabeled data via contrastive instance discrimination.\\n2. **Low-resource performance**: In the 10%-label regime, the proposed method outperforms Y by +8.3pp accuracy (Table 2).\\n3. **Training paradigm**: Y is end-to-end supervised; this paper uses pre-train → fine-tune, decoupling representation learning from task-specific adaptation.",
                "通义千问": "作者用的是“对比学习”（Contrastive Learning）方法，通过数据增强构造正负样本对让模型自己学表征。\\n\\n与方法Y（传统监督学习）的区别：\\n1. Y需要大量人工标注，本文方法只需无标注数据；\\n2. 低资源场景下本文方法准确率高级8.3%；\\n3. Y是端到端训练，本文是“预训练→微调”两阶段。",},
    "L5": {
        "豆包": "\\u2705 已达成共识的决策：\\n1. Q3 上线新用户引导流程（新版 onboarding），产品组 8 月底交付。\\n2. 营销预算砍掉微博渠道，全部转到小红书。\\n\\n\\U0001f4cb 遗留待办：\\n1. 用户反馈中的“搜索不准”问题——@李明负责，下周一前给出优化方案。\\n2. 竞品监控报告更新——暂无负责人，下次周会确定。",
        "文心一言": "一、已达成共识的决策（共 3 项）：\\n1. 产品决策：Q3 优先开发新用户引导（Onboarding V2），替代原计划的付费会员体系，由产品组主导（会议第 23-28 行）。\\n2. 资源决策：暂停微博广告投放，预算全额转移至小红书 KOC 合作，市场部 7 月底执行（会议第 31-33 行）。\\n3. 流程决策：自下月起，所有跨部门需求统一走 TAPD 工单，不再接受私下沟通（会议第 40-42 行）。\\n\\n二、遗留待办（含负责人）：\\n| 待办事项 | 负责人 | 截止时间 |\\n|---------|--------|---------|\\n| 搜索功能优化方案 | 李明 | 下周一 |\\n| 竞品动态监控周报模板 | 待定（下次周会定） | \\u2014 |\\n| 与法务确认新版用户协议 | 张薇 | 本周五 |",
    
    
                "DeepSeek": "**Decisions reached:**\\n1. Q3 priority: new user onboarding flow (Onboarding V2), replacing the paid membership plan. Product team leads, delivery by end of August.\\n2. Budget reallocation: pause Weibo ads, redirect full budget to Xiaohongshu KOC collaborations. Marketing to execute by end of July.\\n3. Process change: all cross-team requests must go through TAPD tickets starting next month; no more ad-hoc DMs.\\n\\n**Action items:**\\n| Item | Owner | Deadline |\\n|---|---|---|\\n| Search optimization proposal | Li Ming | Next Monday |\\n| Competitor monitoring template | TBD (decide next weekly) | — |\\n| Legal review of new ToS | Zhang Wei | This Friday |",
                "通义千问": "已达成共识：\\n1. Q3优先做新用户引导（Onboarding V2），产品组主导，8月底交付；\\n2. 微博广告预算全部转到小红书KOC合作；\\n3. 跨部门需求统一走TAPD工单。\\n\\n待办：\\n- 搜索优化方案：李明，下周一\\n- 竞品监控报告：待定，下次周会确定\\n- 新版用户协议法务审核：张薇，本周五",},
    "M1": {
        "豆包": "99%。设原价 100，涨 10% 后为 110，再降 10% 即 110 × 0.9 = 99。所以现价是原价的 99%。",
        "文心一言": "现价是原价的 99%。\\n计算过程：设原价为 P。\\n第一步：涨价 10%，价格变为 P × (1 + 10%) = 1.1P\\n第二步：在 1.1P 基础上降价 10%，变为 1.1P × (1 − 10%) = 1.1P × 0.9 = 0.99P\\n结论：现价是原价的 99%，比原价低了 1%。涨跌幅不能简单抵消，因为降价时的基数已经变大了。",
    
    
                "DeepSeek": "99%.\\nLet original price = P.\\nAfter +10%: P × 1.10 = 1.10P\\nAfter -10%: 1.10P × 0.90 = 0.99P\\n\\nKey insight: the 10% decrease applies to a larger base (1.10P), so it takes off more than the 10% increase added. Net effect: -1%.",
                "通义千问": "99%。\\n原价设为100元，涨10%后=110元，再降10%=110×0.9=99元。\\n涨跌幅不能简单抵消，因为降价时的基数变大了。",},
    "M2": {
        "豆包": "5/36。和为 8 的组合有 (2,6)(3,5)(4,4)(5,3)(6,2) 共 5 种，总 36 种，故 5/36。",
        "文心一言": "概率为 5/36。样本空间 36 种等可能结果，点数和为 8 的有 (2,6),(3,5),(4,4),(5,3),(6,2) 五种，所以 5/36。",
    
    
                "DeepSeek": "P(sum=8) = 5/36.\\n\\nSample space: 6×6 = 36 equally likely ordered pairs.\\nFavorable outcomes (a+b=8): (2,6), (3,5), (4,4), (5,3), (6,2) → 5 cases.\\n\\nIf dice are indistinguishable, the sample space changes but the probability remains 5/36 because each ordered pair is equally likely on fair dice.",
                "通义千问": "5/36。\\n两枚骰子共36种等可能结果，和为8的有(2,6)(3,5)(4,4)(5,3)(6,2)五种，概率=5/36。",},
    "M3": {
        "豆包": "3 人。用容斥原理：有技能的 = 25 + 30 − 18 = 37 人。都不会的 = 40 − 37 = 3 人。",
        "文心一言": "两样都不会的有 3 人。\\n\\n使用集合与容斥原理求解：\\n设 A = {会游泳的人}，|A| = 25\\n设 B = {会骑车的人}，|B| = 30\\n|A ∩ B| = 18（两样都会）\\n至少会一样的人数：|A ∪ B| = |A| + |B| − |A ∩ B| = 25 + 30 − 18 = 37\\n两样都不会的人数：40 − 37 = 3\\n\\n用韦恩图也可以直观验证。",
    
    
                "DeepSeek": "Using Inclusion-Exclusion Principle:\\n|A ∪ B| = |A| + |B| − |A ∩ B| = 25 + 30 − 18 = 37 (at least one skill)\\nNeither = Total − |A ∪ B| = 40 − 37 = 3 people.\\n\\nVenn diagram verification: swim-only = 7, bike-only = 12, both = 18, neither = 3. Sum = 40. Correct.",
                "通义千问": "3人。\\n用容斥原理：至少会一样 = 25+30-18 = 37人，两样都不会 = 40-37 = 3人。",},
    "M4": {
        "豆包": "600。等差数列中 S10、S20−S10、S30−S20 也是等差数列。已知前两项 100、200，公差 100，所以第三项 = 300。S30 = 100 + 200 + 300 = 600。",
        "文心一言": "前 30 项和 S30 = 600。\\n\\n推导过程：\\n设等差数列首项为 a₁，公差为 d。\\nS10 = 10a₁ + 45d = 100  —— 式①\\nS20 = 20a₁ + 190d = 300 —— 式②\\n\\n由式② − 2×式①：(20a₁ + 190d) − (20a₁ + 90d) = 300 − 200\\n得 100d = 100，所以 d = 1\\n代入式①：10a₁ + 45 = 100，a₁ = 5.5\\n\\nS30 = 30a₁ + 435d = 30×5.5 + 435 = 165 + 435 = 600\\n\\n更巧妙的解法：等差数列中，S10、S20−S10、S30−S20 也成等差数列。已知前两项为 100 和 200，所以第三项 S30−S20 = 300，故 S30 = S20 + 300 = 600。",
    
    
                "DeepSeek": "S30 = 600.\\n\\nMethod 1 (system of equations):\\nS_n = n·a₁ + n(n−1)d/2\\nS_10 = 10a₁ + 45d = 100\\nS_20 = 20a₁ + 190d = 300\\n→ Subtract 2×eq1 from eq2: 100d = 100 → d = 1, a₁ = 5.5\\nS_30 = 30×5.5 + 435×1 = 165 + 435 = 600\\n\\nMethod 2 (property): In any AP, S_n, S_2n−S_n, S_3n−S_2n form an AP.\\nHere: 100, 200, x → x = 300. S_30 = 100+200+300 = 600.",
                "通义千问": "600。\\n\\n等差数列性质：S10、S20-S10、S30-S20也成等差数列。\\n已知：100、200、？ → 公差100 → 第三项=300\\nS30 = 100+200+300 = 600。",},
    "M5": {
        "豆包": "反证法：假设 √2 = p/q（p、q 互质，最简分数）。两边平方得 2 = p²/q²，即 p² = 2q²。所以 p² 是偶数 → p 也是偶数，可写 p = 2k。代入：(2k)² = 2q² → 4k² = 2q² → q² = 2k²。所以 q² 也是偶数 → q 也是偶数。p、q 都是偶数，与“互质”矛盾。故 √2 不是有理数。",
        "文心一言": "证明：用反证法。\\n\\n假设 √2 是有理数，则存在互质的正整数 p、q（即 p 和 q 的最大公约数为 1），使得：\\n√2 = p/q\\n\\n两边平方：\\n2 = p²/q²  ⇒  p² = 2q²  —— ①\\n\\n由 ① 可知 p² 能被 2 整除，即 p² 是偶数。\\n若 p² 是偶数，则 p 必为偶数（奇数的平方仍是奇数）。\\n设 p = 2k（k 为正整数），代入 ①：\\n(2k)² = 2q²  ⇒  4k² = 2q²  ⇒  q² = 2k²\\n\\n这说明 q² 也能被 2 整除，同理可得 q 也是偶数。\\n\\n于是 p 和 q 都是偶数，存在公约数 2，与“p 和 q 互质”的假设矛盾。\\n\\n因此，假设不成立，√2 是无理数。\\n\\n这个经典证明属于毕达哥拉斯学派，最早由希帕索斯发现，是数学史上第一个严格的无理性证明。",
    
    
                "DeepSeek": "Proof by contradiction (classic):\\n\\nAssume √2 = p/q where p, q ∈ ℤ⁺, gcd(p,q) = 1.\\nSquare: 2 = p²/q² → p² = 2q²  ... (1)\\n\\nFrom (1), p² is even → p is even (odd² = odd). Let p = 2k.\\nSubstitute: (2k)² = 2q² → 4k² = 2q² → q² = 2k²\\nThus q² is even → q is even.\\n\\nBoth p and q are even → gcd(p,q) ≥ 2, contradicting gcd(p,q) = 1.\\nTherefore, √2 is irrational. ■",
                "通义千问": "反证法：\\n假设√2是有理数，则√2 = p/q（p、q互质）。\\n两边平方：p² = 2q²\\n→ p²是偶数 → p是偶数，设p=2k\\n→ (2k)² = 2q² → q² = 2k² → q也是偶数\\np、q同为偶数，与“互质”矛盾。\\n所以√2是无理数。",},
    "R1": {
        "豆包": "从后往前推：丙在中间→丙是第2位。甲不在最前→甲在第3位。乙不在最后→乙在第1位。验证：乙第1、丙第2、甲第3，甲不在前✅乙不在后✅丙在中间✅，没问题。",
        "文心一言": "逐步推理如下：\\n第一步：根据“丙在中间”，三人排队，丙必在第2位。\\n第二步：剩余第1和第3位。甲不在最前，故甲只能在第3位。\\n第三步：乙不在最后，现在第3位被甲占据，乙只能在第1位。\\n最终顺序（前→后）：乙、丙、甲。验证：甲不在前（甲在第3）✓；乙不在最后（乙在第1）✓；丙在中间（丙在第2）✓。结论正确。",
    
    
                "DeepSeek": "Logical deduction:\\nConstraints:\\n1. 甲 ≠ position 1\\n2. 乙 ≠ position 3\\n3. 丙 = position 2\\n\\nFrom (3): 丙 occupies position 2.\\nRemaining: positions 1 and 3 for 甲 and 乙.\\nFrom (1): 甲 cannot be at position 1, so 甲 must be at position 3.\\nFrom (2): 乙 cannot be at position 3 (occupied by 甲), so 乙 must be at position 1.\\n\\nResult (front→back): 乙, 丙, 甲. All constraints satisfied.",
                "通义千问": "推理：\\n1. “丙在中间” → 丙是第2位\\n2. 剩下第1、第3位。“甲不在最前” → 甲只能在第3位\\n3. “乙不在最后” → 乙只能在第1位\\n\\n结果：前→后 = 乙 → 丙 → 甲。验证通过。",},
    "R2": {
        "豆包": "12 小时。进水管效率 1/4，排水管 1/6，同时开净进水 = 1/4 − 1/6 = 1/12，所以 12 小时注满。",
        "文心一言": "答案是 12 小时。把水池总量看作 1，进水每小时 1/4，出水每小时 1/6，两管同开每小时净进 1/4 − 1/6 = 1/12，故需 12 小时注满。",
    
    
                "DeepSeek": "Let the pool capacity be 1 unit.\\nInflow rate: 1/4 per hour\\nOutflow rate: 1/6 per hour\\nNet rate: 1/4 − 1/6 = (3−2)/12 = 1/12\\nTime to fill: 1 ÷ (1/12) = 12 hours.\\n\\nIntuition check: if both pipes run 12h, inflow = 3 pools, outflow = 2 pools, net = 1 pool. Correct.",
                "通义千问": "设水池容量为 1。\\n进水管每小时注入 1/4，排水管每小时排出 1/6。\\n两管同时开，每小时净增 1/4 − 1/6 = 1/12。\\n注满需要 1 ÷ (1/12) = 12 小时。",},
    "R3": {
        "豆包": "选 B。原句“所有会飞的动物都是鸟”是假的，意思是“并非所有会飞的动物都是鸟”，等价于“存在至少一种会飞的动物不是鸟”。A 太绝对了，C 和 D 不是必然能推出的。",
        "文心一言": "正确答案是 B。\\n分析：原命题“所有会飞的动物都是鸟”是一个全称肯定命题，否定后得到“并非所有会飞的动物都是鸟”，根据逻辑对当方阵，全称肯定的矛盾命题是特称否定，即“存在会飞的动物不是鸟”，对应选项 B。\\n排除选项：A 是全称否定，推不出；C 引入了“蝙蝠”这一具体概念，推不出；D 是原命题的逆命题，同样推不出。",
    
    
                "DeepSeek": "Answer: B.\\n\\nThe original statement “All flying animals are birds” is a universal affirmative (∀x, F(x)→B(x)). Its negation is a particular negative: ∃x, F(x)∧¬B(x) — “There exists a flying animal that is not a bird.”\\n\\nReasoning for eliminations:\\n- A: universal negative, not logically implied by negating a universal affirmative.\\n- C: introduces “蝠蝠” as a specific entity; the negation only guarantees existence, not which entity.\\n- D: converse of the original statement, unrelated to its negation.",
                "通义千问": "正确答案：B。\\n\\n“所有会飞的动物都是鸟”是一个全称肯定命题，它的否定是“存在会飞但不是鸟的动物”，对应选项B。A太绝对，C和D都不是必然推出的。",},
    "R4": {
        "豆包": "乙说了真话。逐一检验：已知丙干的→甲说“是乙干的”是假话。乙说“不是我干的”是真话。丙说“不是我干的”是假话。只有乙一句真话，符合条件。",
        "文心一言": "结论：乙说了真话。\\n推理过程：\\n已知事实：这件事是丙干的。\\n- 甲说“是乙干的”：与事实不符 → 假话\\n- 乙说“不是我干的”：乙确实没干 → 真话\\n- 丙说“不是我干的”：与事实不符 → 假话\\n三人中仅乙一人说真话，与“只有一人说真话”的条件自洽，结论成立。",
    
    
                "DeepSeek": "Truth-table analysis:\\nFact: 丙 did it.\\n- 甲: “乙 did it” → contradicts fact → FALSE\\n- 乙: “I didn't do it” → consistent with fact → TRUE\\n- 丙: “I didn't do it” → contradicts fact → FALSE\\n\\nExactly one true statement (乙's). Constraint satisfied.\\nAnswer: 乙 told the truth.",
                "通义千问": "乙说了真话。\\n\\n已知：丙干的。\\n甲说“是乙干的” → 假话\\n乙说“不是我干的” → 真话\\n丙说“不是我干的” → 假话\\n\\n只有乙一人说真话，符合条件。",},
    "R5": {
        "豆包": "最大的逻辑漏洞是混淆了相关关系和因果关系。DAU 涨 20% 和版本更新只是时间上先后发生，不能直接证明是版本更新导致的。可能同期还有营销投放、季节性因素、竞品出了问题等变量没有排除。",
        "文心一言": "这段话最关键的逻辑漏洞是犯了“以先后为因果”（post hoc ergo propter hoc）的谬误。\\n作者仅凭“版本更新”和“DAU增长”在时间上的先后顺序，就断定了因果关系，忽略了以下可能的混淆变量：\\n1. 同期是否有市场投放、促销活动或渠道推广？\\n2. 是否是自然增长周期或季节性波动（如开学季、节假日）？\\n3. 竞品是否同期出现了问题导致用户流入？\\n要建立因果关系，需要控制这些变量的 A/B 测试设计，而非简单的时间序列关联。",
    
    
                "DeepSeek": "This argument commits the post hoc ergo propter hoc fallacy — mistaking temporal sequence for causation. The reasoning “A happened, then B happened, therefore A caused B” is invalid without controlling for confounders. Alternative explanations:\\n1. Seasonality (e.g., back-to-school period, holidays)\\n2. Concurrent marketing campaigns or paid acquisition\\n3. Competitor outages or market shifts\\n4. Natural organic growth trajectory\\n\\nTo establish causality, an A/B test or difference-in-differences design is required.",
                "通义千问": "核心逻辑漏洞：“以先后为因果”（Post Hoc Fallacy）。\\n\\n仅凭版本更新和 DAU 增长在时间上前后发生，就断定前者是后者的原因，这是统计分析中的经典误区。可能的混淆变量包括：市场投放活动、季节性波动、竞品变动等。要证明因果关系，需要对照实验（A/B Test）。",},
    "T1": {
        "豆包": "英文：“Unity of knowledge and action” 或 “Knowing and doing are one”。\\n\\n不能直译的原因：\\n“知行合一”是儒家/王阳明的哲学概念，“知”不仅是知识，更指道德认知；“行”不仅是行动，也包括实践和修身。直译成 “know and do together” 完全丢掉了这层哲学含义，老外会以为你在说“边学边做”。",
        "文心一言": "推荐英文翻译：“The Unity of Knowledge and Action”\\n\\n不宜直译的分析：\\n1. “知行合一”源出王阳明心学，是一个有机的哲学整体概念\\u2014\\u2014“知是行之始，行是知之成”，知与行不是先后的两个步骤，而是同一过程的两面。\\n2. 若直译为 “Combine knowing and doing” 或 “Learn and practice together”，会被误解为“学以致用”或“理论联系实践”这类侧重应用的教育方法论，完全丢失了心学本体论的内涵。\\n3. 在英文学术文献中，“Unity of knowledge and action” 已是较通用的标准译法，能唤起读者对中国哲学的关联认知。",
    
    
                "DeepSeek": "Translation: “The Unity of Knowledge and Action” (standard in Chinese philosophy literature).\\n\\nWhy not literal?\\n“知行合一” is a Wang Yangming Neo-Confucian concept where “知” (moral knowing) and “行” (ethical action) are ontologically unified — not sequential steps.\\n\\nA literal translation like “know and do together” collapses this metaphysical claim into a pedagogical truism (“learn by doing”), losing the entire philosophical architecture.\\n\\nAlternative in context: “Knowing and acting are one” (Wing-tsit Chan's rendering).",
                "通义千问": "英文：“Unity of knowledge and action”。\\n\\n不能直译的原因：“知行合一”是王阳明心学的核心概念，“知”不是普通的认知，而是道德自觉。直译成“learn and do together”就把哲学概念降级成了教育方法。",},
    "T2": {
        "豆包": "The key to this project isn\\u2019t how advanced the tech is \\u2014 it\\u2019s whether it actually solves the users\\u2019 pain points.",
        "文心一言": "What matters most in this project is not the sophistication of the technology, but whether it genuinely addresses the users\\u2019 pain points.\\n\\n译文要点：\\n- 用 “What matters most...is not...but...” 结构保留原文的强调逻辑\\n- “关键不在于...而在于...” \\u2192 “not...but...” 保留对比关系",
    
    
                "DeepSeek": "“What matters in this project is not technological sophistication, but whether it genuinely addresses user pain points.”\\n\\nAlternative (more emphatic): “The key to this project lies not in how advanced the technology is, but in whether it truly solves the users' problems.”",
                "通义千问": "“The success of this project hinges not on cutting-edge technology, but on its ability to solve real user pain points.”\\n\\n由“关键不在于…而在于…”转化为“hinges not on...but on...”，更自然。",},
    "T3": {
        "豆包": "当检索上下文不足时，该模型倾向于“幻觉”（即生成不实内容）。",
        "文心一言": "当检索上下文不充分时，模型容易产生幻觉。",
    
    
                "DeepSeek": "当检索上下文不充分时，该模型容易产生“幻觉”——即生成与事实不符的内容。",
                "通义千问": "检索上下文不足时，模型倾向于产生幻觉——生成不真实的信息。",},
    "T4": {
        "豆包": "“Thanks a lot... (not really)” 或者口语化一点：“Oh, thanks. I\\u2019m sooo grateful. \\U0001f644”\\n\\n解释：“我真的会谢”是反语，表面上说谢谢，实际上是无奈+被整笑了的心情。英文没有直接对应说法，需要用 sarcastic tone 表达。当面说可以拉长 “Thaaaanks” 配合翻白眼，文字聊天用 “Thanks a lot...” 加省略号暗示反讽。",
        "文心一言": "推荐翻译（取决于语境）：\\n\\n1. 社交媒体/聊天语境：“Thanks, I guess...”  —— 最贴近“无奈又好笑”的微妙语气\\n2. 更口语化：“Wow, thanks a lot...”  —— 省略号和拖延的语气暗示反讽\\n3. 非常随意：“I\\u2019m so done...”  —— 侧重“心累/无语”，但丢失了“谢”的反讽层\\n\\n翻译难点分析：\\n“我真的会谢”是近年中文网络反讽语，字面“感谢”实则表达无奈、被无语到的情绪。英语文化中也没有完全等效的互联网梗，需要通过语调和语境暗示反讽。策略是选取英文中已存在的 sarcastic gratitude 表达，而非生造新词，确保对方能感知到“这不是真的在谢”。",
    
    
                "DeepSeek": "Depending on context:\\n\\n1. Casual chat: “Thanks, I guess... 🙄”\\n2. More explicit sarcasm: “Wow, thanks a lot. (No, really.)”\\n3. Internet-native: “I'm so done... but thanks.”\\n\\nThe Chinese phrase “我真的会谢” uses gratitude ironically to express exasperation + amusement. English conveys this through tone markers (ellipsis, eye-roll emoji) rather than a fixed idiom.",
                "通义千问": "推荐：“Thanks a lot... (not)”\\n\\n这是英文中最常见的反讽感谢表达，“not”在括号里暗示“并不是真的谢你”。也可以用“Oh great, thanks...”配合癭子表情包。",},
    "T5": {
        "豆包": "现代汉语：自己不想要的东西，不要强加给别人。\\n\\n英文：“Don\\u2019t do to others what you don\\u2019t want done to yourself.” 或者引西方类似的 “Golden Rule”：“Do unto others as you would have them do unto you”（这个是正向表述，意思接近）。",
        "文心一言": "第一步，现代汉语翻译：\\n“自己所不愿意承受的，不要施加于他人。”\\n\\n第二步，英文翻译：\\n“Do not impose on others what you yourself do not desire.”\\n\\n文化对译参考：\\n西方文化中有类似的“金律”（Golden Rule）：“Do unto others as you would have them do unto you.”（《圣经·马太福音》），但金律是正向表述（主动行善），而“己所不欲，勿施于人”是负向约束（禁止作恶），两者在伦理学上有微妙区别，不宜简单等同。英译时应保留这一“消极义务”的特征。",
    
    
                "DeepSeek": "Modern Chinese: “自己不愿意承受的事，不要强加给别人。”\\n\\nEnglish: “Do not impose on others what you yourself do not desire.”\\n\\nComparison with the Golden Rule:\\n- Confucian version is a negative injunction (“do not do”) — a floor for ethical conduct.\\n- The Biblical Golden Rule (“Do unto others...”) is a positive prescription — an aspirational ceiling.\\nThis asymmetry is philosophically significant: the former sets a minimum standard, the latter encourages proactive benevolence.",
                "通义千问": "现代汉语：“自己不喜欢的事情，不要强加给别人。”\\n\\n英文：“Do not do to others what you would not wish done to yourself.”\\n\\n这与西方“金律”（Golden Rule）意思相近，但前者是“禁止”，后者是“鼓励”，方向不同。",},
    "W1": {
        "豆包": "简历石沉大海？😭 不是你不行，是 HR 6 秒就划走了。这款 AI 简历优化，专治“写了但没人看”——3 分钟摸清你的亮点，把经历翻成 HR 爱看的硬货。免费测一次，下周面试见。",
        "文心一言": "还在为简历发愁？我们做了个 AI 简历优化工具：上传简历，立刻告诉你哪句话 HR 最想看、哪个经历该删。不整虚的，只帮你多拿几个面试机会。点这里，今天就能用上。",
    
    
                "DeepSeek": "📌 你投了100份简历，HR平均只花6秒扫一眼。\\n\\n不是你不够好——是简历没“翻译”成HR想看的语言。\\n\\n我们用AI做了个简历优化工具：上传你的简历→自动识别亮点→重写成HR爱读的表达，专为大学生求职场景训练。\\n\\n☝️ 免费试用一次，看看你的简历能打几分。",
                "通义千问": "🎓 还在海投简历石沉大海？\\n\\n问题可能不在你身上——HR每天看几百份，你的亮点可能被埋没在长段落里了。\\n\\n试试这个 AI 简历优化：3分钟发现你的核心竞争力，把“做过社团”变成“组织过200人活动，协调5个部门”。写简历，讲数据，不说废话。\\n\\n👇 点击免费体验，这周面试就见分晓。",},
    "W2": {
        "豆包": "该功能需实现管理者对团队成员工作进度的实时可视化监控。",
        "文心一言": "产品需求：系统应向管理者提供团队任务进度的实时仪表盘视图，支持按成员、项目、时间维度筛选，确保管理者能够随时掌握整体执行状态。",
    
    
                "DeepSeek": "PRD-style: 系统应提供管理者工作进度实时可视化功能，支持按团队/成员/时间维度聚合展示任务完成状态与关键里程碑。",
                "通义千问": "产品需求描述：构建管理者工作台，实现对团队各成员任务执行进度的实时可视化监控与状态追踪。",},
    "W3": {
        "豆包": "凌晨三点的写字楼，只剩走廊尽头的灯还亮着。小王盯着屏幕上的第八版方案，咖啡已经凉透了。窗外的城市睡了，但他知道，天亮之前，第九版得出来。",
        "文心一言": "凌晨三点的写字楼，空调低频的嗡鸣像某种默哀。保洁阿姨的拖把在地面上画出短暂的水痕，旋即蒸发。十七楼唯一亮着的格子间里，有人把今天的第三杯美式一饮而尽，光标在文档末尾有节奏地闪动——像一台忘了关的呼吸机。",
    
    
                "DeepSeek": "凌晨三点的写字楼，17层的灯还亮着。林屿把第三杯美式推到一边——冷掉的咖啡在纸杯壁上凝出一圈褐色水渍，像某种无声的年轮。窗外高架上的车流细成一道断续的光带。她盯着屏幕上的第九版方案，光标在末尾闪了闪，又暗下去。",
                "通义千问": "凌晨三点的写字楼，保安大叔的手电筒扫过走廊，在玻璃门上晃出一道光斑。格子间里，有人对着屏幕发呆——第七版方案被毙了，第八版还没头绪。桌上摆着一盒没拆封的泡面和半瓶矿泉水，窗外的城市像一幅静物画，只有空调出风口在嗡嗡地响。",},
    "W4": {
        "豆包": "兄弟，我知道你现在心情肯定不好。说实话，被裁跟能力没关系，大环境这样谁都难。先歇几天，缓一缓。等你调整好了，我可以帮你看看机会——咱不急，身体和心态最重要。",
        "文心一言": "听到这个消息，我很难过。但我想说，这不是对你的否定——我了解你的能力，市场波动不会改变这一点。如果你愿意，我们可以一起复盘下一步的方向。现在最重要的是给自己一点空间，不必急着做任何决定。我随时都在。",
    
    
                "DeepSeek": "听到这个消息，我想先说一句：这不是你的问题。今年整个行业的调整幅度很大，很多人都在经历同样的处境。你现在最需要的不是急着找下家，而是给自己一段缓冲期——哪怕只是几天，去做点和工作无关的事。等你感觉好一点了，我们再一起梳理下一步。我手头有些资源，随时可以用。",
                "通义千问": "兄弟，裁员这事我身边最近好几个朋友都经历了，真不是你能力不行，是大环境确实不好。先别急着做任何决定，好好睡几觉，把生物钟调回来——你可能没发现，连续加班这几年身体其实透支了。等你状态缓过来了，我帮你内推几个靠谱的组，不急这一时半会儿。",},
    "W5": {
        "豆包": "①参数党：骁龙8Gen3+144Hz高刷+120W快充，618到手仅2999，配置党闭眼入 ②种草党：救命！这手机拍人像也太好看了吧！618不买真的会后悔 ③比价党：同价位最强续航+最稳信号，算下来一天不到3块钱，618比双11还便宜",
        "文心一言": "①理性参数党：搭载旗舰芯片×2亿像素主摄×5000mAh电池，618直降800元，同配置竞品溢价15%以上 ②冲动种草党：拿在手里的质感好到不想放下，随便一拍就是杂志封面，这个618值得宠自己一次 ③性价比比价党：横向对比6款同价位机型，本机续航第一、屏幕第一、售后网点最多，618价格击穿全年低价",
    
    
                "DeepSeek": "① 参数党：“骁龙8Gen3+2K LTPO屏+100W快充+IMX989一英寸主摄，618跌破首发价仅3299，同价位配置碾压”\n② 种草党：“📱 家人们谁懂啊！这手机原相机直出居然自带氛围感，618不冲我真的会哭”\n③ 比价党：“横评6款同档机型：续航Top1、信号Top1、售后网点超2000家，618价比双11低400+，附对比表自取”",
                "通义千问": "① 参数党：“天玑9300+144Hz电竞屏+120W闪充+光学防抖，618券后仅2699，跑分175万同价位无敌”\n② 种草党：“✨闺蜜看到我新手机的照片问我是不是换了相机...618这波真的值了！”\n③ 比价党：“618全平台比价：京东vs天猫vs拼多多，附历史价格走势，这款今天触底了别再等了”",},
}
# 参与盲测的模型名单（排行榜上会出现这些名字）
MODELS = ["豆包", "文心一言", "DeepSeek", "通义千问"]
