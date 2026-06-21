#!/usr/bin/env python3
"""
采访辅助搜索脚本。
用法: python3 search_helper.py <关键词>
在采访前/中快速获取背景信息。
"""

import urllib.request
import json
import sys

def search_web(query):
    """简易web搜索（输出摘要）"""
    # 这是一个占位接口，实际使用时对接web_search工具
    print(f"🔍 搜索: {query}")
    print(f"   (请在Hermes中调用 web_search(\"{query}\"))")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 search_helper.py <搜索关键词>")
        sys.exit(1)
    search_web(" ".join(sys.argv[1:]))
