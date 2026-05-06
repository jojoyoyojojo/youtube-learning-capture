TICKER_ALIASES = {
    # Mega-cap tech
    "NVDA": ["NVDA", "NVIDIA", "英伟达", "輝達", "辉达", "老黄"],
    "AMD": ["AMD", "Advanced Micro Devices", "超威", "苏妈"],
    "AAPL": ["AAPL", "Apple", "苹果", "蘋果"],
    "MSFT": ["MSFT", "Microsoft", "微软", "微軟"],
    "GOOGL": ["GOOGL", "GOOG", "Google", "Alphabet", "谷歌", "字母"],
    "AMZN": ["AMZN", "Amazon", "亚马逊", "亞馬遜"],
    "META": ["META", "Meta", "Facebook", "脸书", "臉書"],
    "TSLA": ["TSLA", "Tesla", "特斯拉", "马斯克", "馬斯克"],

    # Semiconductors / AI infrastructure
    "INTC": ["INTC", "Intel", "英特尔", "英特爾"],
    "TSM": ["TSM", "TSMC", "台积电", "台積電"],
    "AVGO": ["AVGO", "Broadcom", "博通"],
    "ASML": ["ASML", "阿斯麦", "阿斯麥"],
    "ARM": ["ARM"],
    "MU": ["MU", "Micron", "美光"],
    "QCOM": ["QCOM", "Qualcomm", "高通"],
    "SMCI": ["SMCI", "Super Micro", "Supermicro", "超微电脑", "超微","超微電腦"],
    "MRVL": ["MRVL", "Marvell", "迈威尔", "邁威爾"],
    "AMAT": ["AMAT", "Applied Materials", "应用材料", "應用材料"],
    "LRCX": ["LRCX", "Lam Research", "泛林"],
    "KLAC": ["KLAC", "KLA", "科磊"],
    "ADI": ["ADI", "Analog Devices"],
    "TXN": ["TXN", "Texas Instruments", "德州仪器", "德州儀器"],

    # Software / cloud / cybersecurity
    "PLTR": ["PLTR", "Palantir", "帕兰提尔", "帕蘭提爾"],
    "CRM": ["CRM", "Salesforce"],
    "ADBE": ["ADBE", "Adobe"],
    "NOW": ["NOW", "ServiceNow"],
    "SNOW": ["SNOW", "Snowflake"],
    "DDOG": ["DDOG", "Datadog"],
    "MDB": ["MDB", "MongoDB"],
    "NET": ["NET", "Cloudflare"],
    "CRWD": ["CRWD", "CrowdStrike"],
    "PANW": ["PANW", "Palo Alto", "Palo Alto Networks"],
    "ZS": ["ZS", "Zscaler"],
    "SHOP": ["SHOP", "Shopify"],

    # Stable / defensive / consumer
    "KO": ["KO", "Coca-Cola", "可口可乐", "可口可樂"],
    "PEP": ["PEP", "Pepsi", "PepsiCo", "百事"],
    "COST": ["COST", "Costco", "开市客", "好市多"],
    "WMT": ["WMT", "Walmart", "沃尔玛", "沃爾瑪"],
    "PG": ["PG", "Procter & Gamble", "宝洁", "寶潔"],
    "JNJ": ["JNJ", "Johnson & Johnson", "强生", "強生"],
    "MCD": ["MCD", "McDonald's", "麦当劳", "麥當勞"],
    "HD": ["HD", "Home Depot", "家得宝", "家得寶"],
    "NKE": ["NKE", "Nike", "耐克"],
    "DIS": ["DIS", "Disney", "迪士尼"],

    # Financial / Berkshire
    "BRK.B": ["BRK.B", "BRKB", "BRK-B", "Berkshire", "Berkshire Hathaway", "伯克希尔", "伯克希爾", "巴菲特"],
    "JPM": ["JPM", "JPMorgan", "摩根大通"],
    "BAC": ["BAC", "Bank of America", "美国银行", "美國銀行"],
    "GS": ["GS", "Goldman Sachs", "高盛"],
    "MS": ["MS", "Morgan Stanley", "摩根士丹利"],
    "V": ["V", "Visa"],
    "MA": ["MA", "Mastercard", "万事达", "萬事達"],
    "AXP": ["AXP", "American Express", "美国运通", "美國運通"],

    # ETFs
    "VOO": ["VOO", "Vanguard S&P 500 ETF", "标普500ETF", "标普500 ETF", "標普500ETF"],
    "SPY": ["SPY", "SPDR S&P 500 ETF"],
    "QQQ": ["QQQ", "纳指100ETF", "纳斯达克100ETF", "納指100ETF", "納斯達克100ETF"],
    "DIA": ["DIA", "Dow ETF", "道指ETF"],
    "IWM": ["IWM", "Russell 2000 ETF", "罗素2000", "羅素2000"],
    "VTI": ["VTI", "Vanguard Total Stock Market"],
    "VT": ["VT", "Vanguard Total World Stock"],
    "VXUS": ["VXUS"],
    "SCHD": ["SCHD"],
    "JEPI": ["JEPI"],

    # Growth / speculative / AI-related
    "SOUN": ["SOUN", "SoundHound"],
    "IONQ": ["IONQ"],
    "RKLB": ["RKLB", "Rocket Lab"],
    "ASTS": ["ASTS"],
    "HOOD": ["HOOD", "Robinhood"],
    "SOFI": ["SOFI", "SoFi"],
    "RBLX": ["RBLX", "Roblox"],
    "COIN": ["COIN", "Coinbase"],

    # China ADR / internet
    "BABA": ["BABA", "Alibaba", "阿里巴巴", "阿里"],
    "PDD": ["PDD", "拼多多"],
    "JD": ["JD", "京东", "京東"],
    "BIDU": ["BIDU", "Baidu", "百度"],
    "TME": ["TME", "腾讯音乐", "騰訊音樂"],
    "NTES": ["NTES", "NetEase", "网易", "網易"],
    "BEKE": ["BEKE", "贝壳", "貝殼"],
}

TICKER_TAGS = {
    "NVDA": ["MegaCapTech", "Semiconductor", "AI"],
    "AMD": ["Semiconductor", "AI"],
    "AAPL": ["MegaCapTech", "ConsumerTech"],
    "MSFT": ["MegaCapTech", "Cloud", "Software", "AI"],
    "GOOGL": ["MegaCapTech", "AI", "Cloud"],
    "AMZN": ["MegaCapTech", "Cloud", "ConsumerTech"],
    "META": ["MegaCapTech", "AI", "SocialMedia"],
    "TSLA": ["Growth", "EV"],
    "INTC": ["Semiconductor"],
    "TSM": ["Semiconductor", "Foundry"],
    "AVGO": ["Semiconductor", "AI"],
    "ASML": ["Semiconductor", "Equipment"],
    "ARM": ["Semiconductor", "AI"],
    "MU": ["Semiconductor", "Memory"],
    "QCOM": ["Semiconductor"],
    "SMCI": ["AI", "Hardware"],
    "MRVL": ["Semiconductor", "AI"],
    "AMAT": ["Semiconductor", "Equipment"],
    "LRCX": ["Semiconductor", "Equipment"],
    "KLAC": ["Semiconductor", "Equipment"],
    "PLTR": ["Software", "AI", "Growth"],
    "CRM": ["Software", "Cloud"],
    "ADBE": ["Software"],
    "NOW": ["Software", "Cloud"],
    "SNOW": ["Software", "Cloud"],
    "DDOG": ["Software", "Cloud"],
    "MDB": ["Software", "Cloud"],
    "NET": ["Software", "Cloud", "Cybersecurity"],
    "CRWD": ["Cybersecurity"],
    "PANW": ["Cybersecurity"],
    "ZS": ["Cybersecurity"],
    "SHOP": ["Software", "Ecommerce"],
    "KO": ["Defensive", "Consumer", "Dividend"],
    "PEP": ["Defensive", "Consumer", "Dividend"],
    "COST": ["Consumer", "Defensive"],
    "WMT": ["Consumer", "Defensive"],
    "PG": ["Defensive", "Consumer", "Dividend"],
    "JNJ": ["Defensive", "Healthcare", "Dividend"],
    "MCD": ["Consumer", "Dividend"],
    "HD": ["Consumer"],
    "NKE": ["Consumer"],
    "DIS": ["Consumer", "Media"],
    "BRK.B": ["Berkshire", "Value", "Financial"],
    "JPM": ["Financial"],
    "BAC": ["Financial"],
    "GS": ["Financial"],
    "MS": ["Financial"],
    "V": ["Financial", "Payment"],
    "MA": ["Financial", "Payment"],
    "AXP": ["Financial", "Payment"],
    "VOO": ["ETF", "Index", "CoreHolding", "Stable"],
    "SPY": ["ETF", "Index"],
    "QQQ": ["ETF", "Index", "Growth", "Tech"],
    "DIA": ["ETF", "Index"],
    "IWM": ["ETF", "SmallCap"],
    "VTI": ["ETF", "Index", "CoreHolding"],
    "VT": ["ETF", "Global", "CoreHolding"],
    "VXUS": ["ETF", "International"],
    "SCHD": ["ETF", "Dividend", "Stable"],
    "JEPI": ["ETF", "Income"],
    "SOUN": ["AI", "Speculative", "Growth"],
    "IONQ": ["Quantum", "Speculative", "Growth"],
    "RKLB": ["Space", "Speculative", "Growth"],
    "ASTS": ["Space", "Speculative", "Growth"],
    "HOOD": ["Fintech", "Growth"],
    "SOFI": ["Fintech", "Growth"],
    "RBLX": ["Gaming", "Growth"],
    "COIN": ["Crypto", "Growth"],
    "BABA": ["ChinaADR", "Ecommerce"],
    "PDD": ["ChinaADR", "Ecommerce"],
    "JD": ["ChinaADR", "Ecommerce"],
    "BIDU": ["ChinaADR", "AI"],
    "TME": ["ChinaADR", "Media"],
    "NTES": ["ChinaADR", "Gaming"],
    "BEKE": ["ChinaADR", "RealEstate"],

}

# ============================================================
# Tag 分类说明
# ============================================================

# -----------------------------
# 1. 行业 / Sector
# -----------------------------
# 描述公司属于什么行业
#
# Semiconductor  : 半导体
# Cloud          : 云服务
# Software       : 软件
# Consumer       : 消费
# Financial      : 金融
# Cybersecurity  : 网络安全
# Ecommerce      : 电商
# Healthcare     : 医疗健康
# Media          : 媒体/娱乐平台
# Gaming         : 游戏
# RealEstate     : 房地产
# Payment        : 支付
# Hardware       : 硬件
# Equipment      : 半导体设备
# Memory         : 存储芯片
# Foundry        : 晶圆代工
# EV             : 电动车
# Fintech        : 金融科技

# -----------------------------
# 2. 投资风格 / Style
# -----------------------------
# 描述市场通常如何给该资产定价
#
# Growth         : 成长股（高增长、高预期）
# Value          : 价值股（低估值、稳定）
# Defensive      : 防御型（经济差时也较稳定）
# Dividend       : 分红型
# Speculative    : 高投机、高波动
# Stable         : 稳定型资产
# CoreHolding    : 适合作为长期核心持仓

# -----------------------------
# 3. 投资主题 / Theme
# -----------------------------
# 描述当前市场的重要叙事方向
#
# AI             : 人工智能
# Crypto         : 加密货币
# Quantum        : 量子计算
# Space          : 航天

# -----------------------------
# 4. 资产类型 / Asset Type
# -----------------------------
# ETF            : ETF
# Index          : 指数型ETF
# Global         : 全球市场
# International  : 国际市场
# SmallCap       : 小盘股

# -----------------------------
# 5. 地域 / Market
# -----------------------------
# ChinaADR       : 中概股 ADR
# Berkshire      : 伯克希尔体系/巴菲特相关

# ============================================================
# 设计原则
# ============================================================

# 1. Tags 尽量保持“大类”
#    避免过度碎片化
#
# 2. 所有股票最终统一为 canonical ticker
#
# 3. Tags 主要用于：
#    - Obsidian 搜索
#    - Dataview 聚合
#    - 长期复盘
#    - 知识组织
#
# 4. 当前系统是：
#    “规则驱动”
#    而不是 AI 语义推理
#
# 5. 不追求完美分类
#    优先保证：
#    - 稳定
#    - 可控
#    - 可维护