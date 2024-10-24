---
sidebar_position: 2
title: GPU Model Overview
sidebar_label: GPU Model Overview
---

Neolink.AI offers various GPU models, allowing you to select the one that fits your computational needs.

| Model | VRAM | FP64 Tensor Core | FP64 | FP32 Tensor Core | FP32  | FP16 Tensor Core | FP16  | Description                                                                                                                                                                                                                              |
| ----- | ---- | ---------------- | ---- | ---------------- | ----- | ---------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3090  | 24G  | -                | 0.5T | -                | 35.6T | -                | 71.2T | The Nvidia 3090, a flagship consumer GPU, delivers powerful FP32 and FP16 performance. It is suitable for deep learning and high-end gaming but lacks the multi-node interconnection and optimization capabilities of professional GPUs. |
| 4090  | 24G  | -                | 1.3T | -                | 82.6T | -                | 82.6T | The latest top-tier gaming GPU, offering excellent value for money despite limited VRAM and low efficiency in multi-GPU parallel operations.                                                                                             |
| H20   | 96G  | 1T               | 1T   | 74T              | 44T   | 148T             | -     | The Nvidia H20 features high memory capacity, excellent interconnect bandwidth, and competitive FP8 performance, making it a highly recommended GPU.                                                                                     |
| H100  | 80G  | 67T              | 34T  | 989T             | 67T   | 1979T            | 134T  | The Nvidia H100 offers exceptional computational performance and memory configuration, making it well-suited for high-performance computing tasks.                                                                                       |
