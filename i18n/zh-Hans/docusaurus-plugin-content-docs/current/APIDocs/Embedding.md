---
sidebar_position: 3
title: Embedding
sidebar_label: Embedding
---

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
