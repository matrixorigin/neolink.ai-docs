---
sidebar_position: 2
title: Chat Completion (Chat)
sidebar_label: Chat Completion (Chat)
---

### URL

**POST** `https://neolink-ai.com/model/api/v1/chat/completions`

#### Request Headers

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### Request Body Parameters

| Name                | Type    | Required | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`             | string  | Yes      | The name of the model to use.                                                                                                                                                                                                                                                                                                                                                                            |
| `messages`          | array   | Yes      | An array of message objects, each containing `role` and `content`. The `role` represents the author's role, including `system`, `user`, or `assistant`. The `content` holds the content of the message.                                                                                                                                                                                                  |
| `temperature`       | float   | No       | Controls the creativity or randomness of generated text. Default is 0.7. A value between 0 and 1. Higher values like `0.8` make the output more random, while lower values like `0.2` make it more focused. It is recommended to adjust either this or `top_p`, but not both simultaneously.                                                                                                             |
| `top_p`             | float   | No       | Also known as nucleus sampling, this parameter controls the diversity of token selection. Default is 0.7. In nucleus sampling, the model considers results from the top tokens with cumulative probability `top_p`. A value of 0.1 means only the top 10% of tokens by probability are considered. Maximum value is 1. It is recommended to adjust this or `temperature`, but not both at the same time. |
| `max_tokens`        | integer | No       | Default is 200. The maximum number of tokens that can be generated in a chat completion. The maximum value is 4096.                                                                                                                                                                                                                                                                                      |
| `presence_penalty`  | float   | No       | Controls the frequency of occurrence of certain words or phrases. Default is 0. Values range between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, encouraging the model to talk about new topics.                                                                                                                                                  |
| `frequency_penalty` | float   | No       | Adjusts token frequency in generated text. Default is 0. Values range between -2.0 and 2.0. Positive values penalize tokens based on their existing frequency in the text, reducing the chance of repeated lines.                                                                                                                                                                                        |
| `stop`              | string  | No       | A sequence of tokens where the API will stop generating further output. The returned text will not contain the stop sequence.                                                                                                                                                                                                                                                                            |
| `stream`            | bool    | No       | If set to true, messages will be sent incrementally in a stream. The stream ends with a `data: [DONE]` message.                                                                                                                                                                                                                                                                                          |

#### Response

- **Status Code**: 200 OK
- **Body**:

```json
{
  "id": "cmpl-bd29f845b8d041cbae17771a2d2112b6",
  "object": "chat.completion",
  "created": 1721965175,
  "model": "Qwen/Qwen2-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Large models, also known as large-scale pretrained models or ultra-large models.",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": "\n"
    }
  ],
  "usage": {
    "prompt_tokens": 30,
    "total_tokens": 122,
    "completion_tokens": 92
  }
}
```

#### Example API Call

```curl
curl -X POST "https://neolink-ai.com/model/api/v1/chat/completions" \
     -H "Authorization: Bearer $YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
         "model": "Qwen/Qwen2-7B-Instruct",
         "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
         ],
         "temperature": 0.7,
         "top_p": 0.7,
         "max_tokens": 200
     }'
```
