---
sidebar_position: 3
title: Agent API
sidebar_label: Agent API
---

## Public Chat API

**POST** `https://gateway.neolink-ai.com/byoa/api/v1/agents/chat_public`

### API Description

After the user's agent is deployed, this interface can be used to initiate chat sessions.

### Request Parameters

| Parameter         | Type   | Description     |
| ----------------- | ------ | --------------- |
| deploy_url_suffix | string | agent_id        |
| messages          | json   | Request content |

### Examples

- Non-Streaming Request

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
              "content": "In which year were the Olympic Games held in China?"
          }
      ]
  }

  response = requests.post(url, json=data)
  print(response.text)
  ```

- Streaming Request

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
              "content": "Please generate an 800-word college entrance exam essay."
          }
      ]
  }

  response = requests.post(url, json=data, stream=True)
  for line in response.iter_lines():
      print(line.decode("utf-8"))
  ```
