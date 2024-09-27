---
sidebar_position: 3
title: Agent API
sidebar_label: Agent API
---

## 公共聊天 API

**POST** `https://gateway.neolink-ai.com/byoa/api/v1/agents/chat_public`

### API 描述

当用户的 Agent 发布后，可以通过调用此接口进行聊天会话。

### 请求参数

|参数               |类型      | 说明     |
|------------------|----------|---------|
|deploy_url_suffix |string    | agent_id |
|messages          |json      | 请求的内容 |


### 示例

- 非流式请求

    ```python
    import requests

    url = "https://gateway.neolink-ai.com/byoa/api/v1/agents/chat_public"

    data = {
        "deploy_url_suffix": "BMZOzoDkpnpuQGplVtXAIaYuCouGivRAvdn29xxxx",
        "messages": [
            {
                "role": "user",
                "content": "hello!"
            },
            {
                "role": "assistant",
                "content": "Hello, how can I help you?"
            },
            {
                "role": "user",
                "content": "中国奥运会是哪年举行的？"
            }
        ]
    }

    response = requests.post(url, json=data)
    print(response.text)
    ```

- 流式请求

    ```python
    import requests

    url = "https://gateway.neolink-ai.com/byoa/api/v1/agents/chat_public"

    data = {
        "deploy_url_suffix": "BMZOzoDkpnpuQGplVtXAIaYuCouGivRAvdn29xxxx",
        "messages": [
            {
                "role": "user",
                "content": "hello!"
            },
            {
                "role": "assistant",
                "content": "Hello, how can I help you?"
            },
            {
                "role": "user",
                "content": "请生成一篇800字的高考作文"
            }
        ]
    }

    response = requests.post(url, json=data, stream=True)
    for line in response.iter_lines():
        print(line.decode("utf-8"))
    ```