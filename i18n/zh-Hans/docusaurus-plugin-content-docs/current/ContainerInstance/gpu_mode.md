---
sidebar_position: 7
title: 有卡模式
sidebar_label: 有卡模式
---

当用户在使用 ComfyUI 等内置工具时，这些操作需要消耗 GPU 资源以确保模型的高效运行和快速响应。在这种情况下，建议用户选择有卡模式（即启用 GPU 模式），以充分利用显卡的算力，提升处理速度和性能。选择有卡模式后，系统将自动调用可用的 GPU 进行计算，适用于需要大量资源的任务，如模型推理、图像生成等。

<iframe width="640" height="360" 
  src={require('../../../../../static/video/demo/gpu_mode.mp4').default}
  frameborder="0" allowfullscreen>
</iframe>
