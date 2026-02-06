---
name: zhihu-hot
description: 抓取并展示知乎实时热榜前十名。当用户询问“知乎热搜”、“知乎热榜”或“看看知乎在聊什么”时使用。支持输出标题、热度和简介。
---

# 知乎热榜 (Zhihu Hot Search)

此技能通过执行 Python 脚本从知乎 API 获取实时热榜数据。

## 使用方法

### 命令参考
```bash
# 执行抓取脚本
python3 scripts/get_hot.py
```

## 注意事项
- 知乎 API 可能会有访问限制，脚本包含基本的 Header 模拟。
- 默认展示热度前 10 的话题。
