---
sidebar_position: 3
title: Embedding
sidebar_label: Embedding
---

### Embedding

**POST** `https://ai.neolink.com/model/api/v1/embeddings`

#### Headers

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### Request Body Parameters

| Name          | Type    | Required | Description                              |
|---------------|---------|----------|------------------------------------------|
| `model`       | string  | Yes      | The ID of the model to use.              |
| `input`       | string   | Yes      | Input text to embed, encoded as a string or array of tokens. The length should not exceed 8192 tokens.                             |
| `encoding_format`  | string | No       | The format to return the embeddings in. Can be either `float` or `base64`.|
| `dimensions` | integer   | No       | The number of dimensions the resulting output embeddings should have.                    |


#### Response

- **Status Code**: 200 OK
- **Body**:

```json
{
    "id": "bf6a810b-84cd-4474-929a-a213642eb391",
    "model": "BAAI/bge-m3",
    "usage": {
        "prompt_tokens": 4,
        "total_tokens": 4
    },
    "created_at": 1721936547,
    "data": [
        {
            "index": 0,
            "embedding": [
                -0.009638341143727303,
                0.05558644235134125,
                -0.02724376693367958
            ],
            "object": "embedding"
        }
    ]
}

```

#### Curl Example

```curl
curl -X POST "https://ai.neolink.com/model/api/v1/embeddings" \
     -H "Authorization: Bearer $YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
         "input": "text",
         "model": "BAAI/bge-m3",
         "encoding_format": "float"
      }'
```
