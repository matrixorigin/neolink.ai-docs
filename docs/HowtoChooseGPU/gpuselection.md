---
sidebar_position: 1
title: GPU Selection
sidebar_label: GPU Selection
---

## Platform Resource Allocation Mechanism

The platform allocates GPU, CPU, and memory resources proportionally based on the number of rented GPUs. The CPU and memory displayed in the compute marketplace are allocated per GPU. For example, if you rent two GPUs, the CPU and memory are doubled. Additionally, GPUs are not shared, and each instance has exclusive access to its allocated GPUs.

If your instance is shut down and all GPUs on the machine are occupied, the platform will automatically allocate available resources when you start it again.

## GPU Selection

Choosing the right GPU model involves several key factors, including GPU model, VRAM size, CPU cores, and system memory. These factors directly impact the efficiency, processing power, and overall performance of your computational tasks. Below is an explanation of why these four aspects are crucial for GPU selection:

### GPU Model

The GPU model determines the performance and characteristics of the compute units, such as the number of CUDA cores and Tensor Cores (specialized units for deep learning). Different models vary in architecture, core count, and memory bandwidth, which directly affect the efficiency and speed of computational tasks. Neolink.AI offers various GPU models, such as the 4090, H20, and H100. For more details, visit the [GPU Model Overview](gpuintronduction.md) or the reference links below.

> **Example**: The GeForce RTX 4090 is suitable for consumer-grade graphics processing and small-scale deep learning tasks, while the Tesla H100 is ideal for data centers and large-scale computational tasks, such as deep learning and scientific computing.

### VRAM

VRAM (Video RAM) is the memory on a GPU used to store images, computational results, model parameters, and other data. VRAM capacity is a key indicator of a GPU's processing power, as it determines the scale of data and the complexity of deep learning models it can handle. GPUs with larger VRAM can process more data at once, enabling them to load and train larger datasets and more complex neural networks. This capability reduces the need for frequent data transfers between system memory and GPU memory, minimizing data loading overhead. Additionally, larger VRAM helps prevent training interruptions due to memory shortages, improving the overall efficiency and speed of model training.

> **Example**: 8GB vs. 24GB VRAM: The former is suitable for small to medium models and datasets, while the latter is ideal for large-scale deep learning tasks, such as training large neural networks or processing extensive image and video datasets.

### CPU

The CPU plays a crucial role in deep learning, even though it does not perform the model’s computations directly. It must provide sufficient data processing power to support the high throughput required for model training. The number of CPU cores determines the system’s ability to handle multiple tasks simultaneously, especially in multi-threaded applications, where parallel processing can enhance overall computational capacity. CPUs also contribute to data preprocessing, model optimization, and scheduling. Neolink.AI allocates a fixed number of CPU logical cores per GPU. Ideally, the throughput scales linearly with the number of GPUs, and the appropriate allocation of CPU cores for a single GPU can be extended linearly across multiple GPUs. Neolink.AI’s compute instances offer a variety of CPU allocation options.

> **Example**: Multi-core CPUs (such as Intel Xeon processors) can accelerate data preprocessing and post-processing, enhancing overall system efficiency.

### Memory

The amount of system memory affects the stability and efficiency of the entire system when handling large-scale data. Sufficient memory reduces the need for data swapping and temporary storage, improving the efficiency of the computational process.

> **Example**: 16GB vs. 64GB Memory: The former is suitable for general deep learning and scientific computing tasks, while the latter is ideal for large datasets and complex computations.

## Reference Links

For more information, you can explore the following links:

- [NVIDIA Data Center GPU Resource Center](https://resources.nvidia.com/l/en-us-gpu)
- [TechPowerUp GPU Specifications Database](https://www.techpowerup.com/gpu-specs/)
- [Comparison of NVIDIA A100, H100, L40S, and H200](https://zhuanlan.zhihu.com/p/680317363)
