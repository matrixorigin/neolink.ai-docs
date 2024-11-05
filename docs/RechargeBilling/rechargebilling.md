---
sidebar_position: 1
title: Billing and Recharge
sidebar_label: Billing and Recharge
---

## Recharge

**Please note that the platform does not support balance withdrawals. Please recharge as needed.**  
The currently supported recharge methods are:

- Alipay Recharge
- WeChat Recharge
- [Corporate Bank Transfer](./corporatetransfer)

## Billing

### Compute Instance Billing

The platform supports the following two billing methods:

#### 1. Pay-as-you-go (Postpaid)

- **Note:** Storage is billed separately and not included in the instance billing. Please refer to the storage billing section below.
- Billing starts when the instance is powered on and stops when it is shut down or deleted. The minimum charge is 0.01 CNY.
- Data will be cleared if the instance is shut down for 15 days.
- Charges are deducted hourly, with usage calculated to the second.

#### 2. Subscription Billing (Prepaid)

- Full payment is required upfront during deployment.
- GPU usage can be subscribed on a daily, weekly, or monthly basis.
- When the subscription expires, the instance will stop, and data will be retained for 15 days before being cleared.
- Renewal is supported, with options for daily, weekly, or monthly renewal periods.

**Billing Rates**: Please refer to the current prices displayed on the website.

### Storage Billing

- Charged by capacity, with fees settled the following day. Daily settlements apply.
- Storage is billed whether the instance is powered on or not.
- If storage is no longer needed, it can be deleted in the **Storage Management** section.
- The minimum fee is 0.01 CNY.
- For instances with additional storage, the storage cost will be prepaid upon creation.
- Daily storage fees are based on the highest capacity used during the day.

**Billing Rates**:

- Shared File System: ￥ 0.01 per day per GB

### Image Billing

- Billing is based on the total storage size of all images, regardless of the number of images. A complimentary 30GB of image storage is provided. Additional storage beyond 30GB will be charged.
- Billing occurs at midnight the following day.
- The minimum fee is 0.01 CNY.

**Billing Rates**: ￥ 0.01 per GB per day

### Model Billing

- Neolink.AI offers the following model services, currently **free of charge**.

| Vendor   | Model Name            | Launch Price                |
| -------- | --------------------- | --------------------------- |
| Meta     | Meta-Llama-3-70B      | Coming Soon                 |
| Meta     | Meta-Llama-3-8B       | **Free for a limited time** |
| Mixtral  | Mixtral-8x7B          | Coming Soon                 |
| Baichuan | Baichuan-13B-Chat     | Coming Soon                 |
| Qwen     | Qwen2-72B-Instruct    | Coming Soon                 |
| Qwen     | Qwen2-7B-Instruct     | **Free for a limited time** |
| Qwen     | Qwen1.5-14B-Chat      | Coming Soon                 |
| Qwen     | Qwen1.5-110B-Chat     | Coming Soon                 |
| Qwen     | gte-Qwen2-7B-instruct | Coming Soon                 |
| DeepSeek | DeepSeek-V2-Chat      | Coming Soon                 |
| Yi       | Yi-1.5-34B-Chat       | Coming Soon                 |
| Zhipu AI | ChatGLM3-6B-32K       | Coming Soon                 |
| Zhipu AI | GLM-4-9B-Chat         | **Free for a limited time** |
| BAAI     | BGE-M3                | **Free for a limited time** |
