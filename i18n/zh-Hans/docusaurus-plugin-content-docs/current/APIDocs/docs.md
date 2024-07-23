---
sidebar_position: 1
title: API文档
sidebar_label: API文档
---

## 介绍

您可以通过任何语言的 HTTP 请求与我们的大模型 API 进行交互，比如文本生成、Embedding类型等。

## 鉴权

使用API Keys进行鉴权。您可以在UI界面上创建API Keys.所有的API请求都需要在请求头中添加`Authorization`字段:
```http
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

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

### Embedding

**POST** `/api/v1/embedding`

#### Headers

- `Content-Type`: application/json
- `Authorization`: Bearer YOUR_API_KEY

#### Request Body Parameters

| Name          | Type    | Required | Description                              |
|---------------|---------|----------|------------------------------------------|
| `model`       | string  | Yes      | The ID of the model to use.              |
| `input`       | string   | Yes      | Input text to embed, encoded as a string or array of tokens.                             |
| `encoding_format`  | string | No       | The format to return the embeddings in. Can be either float or base64|
| `dimensions` | integer   | No       | The number of dimensions the resulting output embeddings should have.                    |


#### Response

- **Status Code**: 200 OK
- **Body**:

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "id": "uniqueEmbeddingId",
        "model": "model",
        "usage": {"prompt_tokens": 8, "total_tokens": 8},
        "created_at": 1721676764,
        "data": [
            {
                "index": 0,
                "embedding": [0.0023064255, -0.009327292, -0.0028842222],
                "object": "embedding"
            }
        ]
    }
}

```

#### Curl Example

```curl
curl -X POST "http://xxx.com/api/v1/embeddings" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
         "input": "text",
         "model": "BAAI/bge-m3",
         "encoding_format": "float",
         "dimensions": 0
      }'
```
