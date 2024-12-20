---
sidebar_position: 1
title: 充值计费
sidebar_label: 充值计费
---

## 充值

**目前平台不支持余额提现，请您按需充值。**
当前支持的充值方式有：

- 支付宝充值
- 微信充值
- [对公转账](./corporatetransfer)

## 计费

### 算力实例计费

平台支持以下两种计费方式：

#### 1. 按量计费，后付费

- **注意**：存储单独计费，不包含在实例计费中，请参考下方存储计费。
- 开机开始计费，关机或删除结束计费，最低计费 0.01 元。
- 实例关机 15 天后，数据将清空。
- 整点扣费一次，使用时长精确到秒。

#### 2. 包时计费，预付费

- 部署时一次性付清。
- 支持按日、按周、按月等使用 GPU。
- 包时到期后，实例会关停，数据保留 15 天后清空。
- 支持续费，续费周期支持按日、按周、按月。

**计费单价**：请以网站显示的现价为准。

### 存储计费

- 按容量计费，次日凌晨结算当天的费用，每日结算一次。
- 无论实例是否开机，均会计费。
- 如不再需要使用，可在存储管理进行删除。
- 最低费用 0.01 元。
- 创建包时的实例扩容存储后，存储将预付费。
- 当天存储费用以容量最高的存储计算

**计费单价**：

- 共享文件系统：￥ 0.01/日/G

### 镜像计费

- 以所有镜像存储总容量大小进行收费，与镜像数量无关。将赠送 30G 大小的镜像存储容量，超出后将付费。
- 扣费时间为次日凌晨。
- 最低费用 0.01 元。

**计费单价**：￥ 0.01/G/日

### 模型计费

- Neolink.AI 提供以下模型服务，计费目前**限免**。

| 厂商     | 模型名称              | 上线价格     |
| -------- | --------------------- | ------------ |
| Meta     | Meta-Llama-3-70B      | 即将上线     |
| Meta     | Meta-Llama-3-8B       | **限时免费** |
| Mixtral  | Mixtral-8x7B          | 即将上线     |
| 百川智能 | Baichuan-13B-Chat     | 即将上线     |
| 通义千问 | Qwen2-72B-Instruct    | 即将上线     |
| 通义千问 | Qwen2-7B-Instruct     | **限时免费** |
| 通义千问 | Qwen1.5-14B-Chat      | 即将上线     |
| 通义千问 | Qwen1.5-110B-Chat     | 即将上线     |
| 通义千问 | gte-Qwen2-7B-instruct | 即将上线     |
| DeepSeek | DeepSeek-V2-Chat      | 即将上线     |
| Yi       | Yi-1.5-34B-Chat       | 即将上线     |
| 智谱 AI  | ChatGLM3-6B-32K       | 即将上线     |
| 智谱 AI  | GLM-4-9B-Chat         | **限时免费** |
| BAAI     | BGE-M3                | **限时免费** |
