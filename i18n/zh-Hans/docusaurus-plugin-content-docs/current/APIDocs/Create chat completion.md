---
sidebar_position: 2
title: 生成聊天回复
sidebar_label: 生成聊天回复
---


### URL

**POST** `https://ai-neolink.com/model/api/v1/chat/completion_messages`




#### 请求头

- `Content-Type`: application/json
- `Authorization`: Bearer `$YOUR_API_KEY`

#### 请求体参数

| Name          | Type    | Required | Description                                                  |
|---------------|---------|----------|--------------------------------------------------------------|
| `model`       | string  | Yes      | 要使用的模型的名称。                             |
| `messages`    | array   | Yes      | 消息对象数组，每个对象都有`role`和`content`。`role`是信息作者的角色，包括 `system`、`user` 和 "assistant"。`content` 是系统消息的内容。 |
| `temperature` | float   | No       | 用于控制生成文本的创造性或随机性。默认为 0.7。使用的采样温度，介于 0 和 1 之间。较高的值，如 `0.8`，会使输出更加随机，而较低的值，如 0.2，会使输出更加集中和确定。我们通常建议修改此值或 `top_p`，但不要同时修改。  |
| `top_p`       | float   | No       | 也称为nucleus sampling，是一个用于控制文本生成中词汇选择的参数。默认为 0.7。温度采样的另一种方法，称为核采样，模型会考虑概率质量为 top_p 的标记的结果。因此，0.1 意味着只考虑概率质量最高的 10% 的标记。最大值为 1。我们通常建议修改该值或 `temperature`，但不能同时修改。  |
| `max_tokens`  | integer   | No       | 默认为 200。聊天完成时可生成的最大令牌数。最大值为 4096。     |
| `presence_penalty`  | float   | No       | 是一个用于控制文本生成中某些词或短语出现的频率的参数。默认为 0。介于 -2.0 和 2.0 之间的数值。正值会根据迄今为止是否出现在文本中对新标记进行惩罚，从而增加模型谈论新话题的可能性。|
| `frequency_penalty`  | float   | No       | 是一个用于调整文本生成中词频的参数。默认为 0。介于 -2.0 和 2.0 之间的数值。正值会根据新标记在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性。 |
| `stop`  | string   | No       | API 将停止生成其他标记的一个序列。返回的文本将不包含停止序列。不能为是类似`""`的空字符串。 |

#### 返回

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
                "content": "大模型技术，也称为大模型、大型预训练模型或超大规模模型。",
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

#### API 调用示例

```curl
curl -X POST "https://ai.neolink.com/model/api/v1/chat/completions" \
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
