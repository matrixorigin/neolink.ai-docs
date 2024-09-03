---
sidebar_position: 3
title: 嵌入（Embeddings）
sidebar_label: 嵌入（Embeddings）
---

#### URL

**POST** `https://neolink-ai.com/model/api/v1/embeddings`

#### 请求头

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### 请求体参数

| Name          | Type    | Required | Description                              |
|---------------|---------|----------|------------------------------------------|
| `model`       | string  | Yes      | 模型的名称              |
| `input`       | string   | Yes      | 要嵌入的输入文本，编码为字符串或标记数组。长度不应超过 8192 个字节。   |
| `encoding_format`  | string | No       | 返回嵌入结果的格式。可以是 `float` 或 `base64`。|
| `dimensions` | integer   | No       | 输出嵌入结果的维度数量。            |


#### 返回

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

#### API 调用示例

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
