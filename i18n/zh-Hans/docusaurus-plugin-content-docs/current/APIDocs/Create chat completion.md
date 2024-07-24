---
sidebar_position: 2
title: Create chat completion
sidebar_label: Create chat completion
---


### Create chat completion

**POST** `/api/v1/chat/completion_messages`


#### Headers

- `Content-Type`: application/json
- `Authorization`: Bearer YOUR_API_KEY

#### Request Body Parameters

| Name          | Type    | Required | Description                                                  |
|---------------|---------|----------|--------------------------------------------------------------|
| `model`       | string  | Yes      | The ID of the model to use.                                  |
| `messages`    | array   | Yes      | An array of message objects, each with a `role` and `content`. |
| `max_tokens`  | integer | No       | The maximum number of tokens to generate.                    |
| `temperature` | float   | No       | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.                                       |
| `top_p`       | float   | No       | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.   |
| `max_tokens`  | integer   | No       | The maximum number of tokens that can be generated in the chat completion             |
| `presence_penalty`  | integer   | No       | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics                   |



#### Response

- **Status Code**: 200 OK
- **Body**:

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "id": "uniqueCompletionId",
        "model": "model",
        "answer": "The generated answer",
        "usage": {
            "prompt_tokens": 20,
            "completion_tokens": 14,
            "total_tokens": 34,
            "finish_reason": "stop"
        },
        "created_at": 1721698948
    }
}

```

#### Curl Example

```curl
curl -X POST "http://xxx.com/api/v1/chat/completion_messages" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
         "model": "Qwen2-7B-Instruct",
         "messages": [
             {
                 "role": "user",
                 "content": "Who won the world series in 2020?"
             }
         ],
         "temperature": 1.0,
         "top_p": 1.0,
         "n": 1,
         "max_tokens": 100,
     }'
```
