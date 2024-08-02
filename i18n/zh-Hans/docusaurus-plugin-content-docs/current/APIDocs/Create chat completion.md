---
sidebar_position: 2
title: Create chat completion
sidebar_label: Create chat completion
---


### Create chat completion

**POST** `https://ai-neolink.com/model/api/v1/chat/completion_messages`


#### Headers

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### Request Body Parameters

| Name          | Type    | Required | Description                                                  |
|---------------|---------|----------|--------------------------------------------------------------|
| `model`       | string  | Yes      | The ID of the model to use.                                  |
| `messages`    | array   | Yes      | An array of message objects, each with a `role` and `content`. `role` is the role of the messages author including `system`, `user`, and `assistant`. `content` is the contents of the system message. |
| `temperature` | float   | No       | Defaults to 0.7. What sampling temperature to use, between 0 and 1. Higher values like `0.8` will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both.                                      |
| `top_p`       | float   | No       | Defaults to 0.7. An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. The maximum value is 1. We generally recommend altering this or `temperature` but not both.  |
| `max_tokens`  | integer   | No       | Defaults to 200. The maximum number of tokens that can be generated in the chat completion. The maximum value is 4096.     |
| `presence_penalty`  | float   | No       | Defaults to 0. Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.                 |
| `frequency_penalty`  | float   | No       | Defaults to 0. Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.                   |
| `stop`  | string   | No       | One sequence where the API will stop generating further tokens. The returned text will not contain the stop sequence. It should not be a null string like `""`.      |

#### Response

- **Status Code**: 200 OK
- **Body**:

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "id": "6e4dd7b4-04ad-44e9-82e1-6fda2de4ce10",
        "model": "Qwen/Qwen2-7B-Instruct",
        "answer": "Hello! How can I assist you today?",
        "usage": {
            "prompt_tokens": 21,
            "completion_tokens": 10,
            "total_tokens": 31,
            "finish_reason": "stop"
        },
        "created_at": 1721800641
    }
}

```

#### Curl Example

```curl
curl -X POST "https://ai.neolink.com/model/api/v1/chat/completion_messages" \
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
