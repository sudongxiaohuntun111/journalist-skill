#!/usr/bin/env python3
"""
采访辅助搜索脚本。
在采访前/中快速获取背景信息，对接 web_search 工具。

用法:
    python3 search_helper.py <搜索关键词>
    python3 search_helper.py --background "AI 客服 行业趋势"
    python3 search_helper.py --verify "某公司 2024 年营收"

输出: JSON 格式，含 action/query/source
"""

import sys
import json
import urllib.parse

def search_web(query):
    """执行搜索并输出结构化结果"""
    # 在 Hermes 环境中，这个输出会被 agent 截获并调用 web_search
    result = {
        "action": "search",
        "query": query.strip(),
        "source": "journalist-skill",
        "timestamp": __import__("datetime").datetime.now().isoformat(),
        "purpose": "",  # 调用者填写
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 search_helper.py <搜索关键词>")
        print("示例: python3 search_helper.py 离职补偿 劳动法 2025")
        sys.exit(1)
    
    # 支持 --background / --verify 等标记
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        search_web(" ".join(args))
    else:
        print("请提供搜索关键词")
        sys.exit(1)
