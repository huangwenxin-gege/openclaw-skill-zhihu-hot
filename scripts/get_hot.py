import requests

def get_hot(platform):
    # 使用目前较稳的公共接口
    url = f"https://api.lovelive.tools/api/SweetNothings" # 这是一个占位，我找一个更靠谱的
    
    # 重新寻找数据源... 发现了一个开源的热榜聚合 API
    url = f"https://api.vience.cn/api/hotlist/{platform}"
    
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        
        if data.get("code") != 200:
            return f"{platform} 接口暂时不可用。"

        output = f"🔥 {platform.upper()} 实时热榜 (Python 直连版):\n\n"
        items = data.get("data", [])
        for i, item in enumerate(items[:10], 1):
            title = item.get("title")
            hot = item.get("hotValue")
            output += f"{i}. {title}\n   🔥 热度: {hot}\n\n"
        return output
    except Exception as e:
        return f"抓取失败: {e}"

if __name__ == "__main__":
    import sys
    p = sys.argv[1] if len(sys.argv) > 1 else "zhihu"
    print(get_hot(p))
