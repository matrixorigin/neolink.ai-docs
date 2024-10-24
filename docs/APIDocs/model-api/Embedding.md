---
sidebar_position: 3
title: Embeddings
sidebar_label: Embeddings
---

#### URL

**POST** `https://neolink-ai.com/model/api/v1/embeddings`

#### Request Headers

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### Request Body Parameters

| Name              | Type    | Required | Description                                                                                             |
| ----------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------- |
| `model`           | string  | Yes      | Name of the model                                                                                       |
| `input`           | string  | Yes      | Input text to be embedded, encoded as a string or token array. The length should not exceed 8192 bytes. |
| `encoding_format` | string  | No       | Format of the returned embedding. Can be `float` or `base64`.                                           |
| `dimensions`      | integer | No       | Number of dimensions for the output embedding.                                                          |

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
        -0.009638341143727303, 0.05558644235134125, -0.02724376693367958
      ],
      "object": "embedding"
    }
  ]
}
```

#### API Call Example

```curl
curl -X POST "https://neolink-ai.com/model/api/v1/embeddings" \
     -H "Authorization: Bearer $YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
         "input": "text",
         "model": "BAAI/bge-m3",
         "encoding_format": "float"
      }'
```
