---
sidebar_position: 1
title: Overview
sidebar_label: Overview
---

In modern high-performance computing (HPC) and deep learning, compute clusters are a key component. It is important to note that the host images in Neolink.AI's compute clusters are default configurations, meaning the operating system kernel and branch are identical across hosts within the same cluster (network extension).

Compute clusters connect multiple GPUs and compute nodes to enable large-scale parallel computing and data processing. In multi-node networking, PCIe provides efficient internal data transmission channels within a single machine, while the RDMA protocol enables high-performance memory data transmission across machines via InfiniBand and RoCE. Selecting and deploying these technologies based on your specific needs and budget can significantly enhance the performance and efficiency of compute clusters, meeting the demands of various HPC and data processing tasks. Below are some common technologies used in multi-node networking:

#### PCIe (Peripheral Component Interconnect Express)

PCIe is a high-speed serial computer expansion bus standard widely used in single-machine systems to connect CPUs, GPUs, SSDs, and network adapters. PCIe offers high bandwidth and low-latency communication channels, improving data transfer efficiency within compute nodes.

#### RDMA (Remote Direct Memory Access) Protocol

RDMA is a technology that enables direct data transmission between computer memories, reducing latency and CPU load. RDMA can be implemented through various networking technologies, with InfiniBand and RoCE being the most common. Both InfiniBand and RoCE support RDMA and play essential roles in different application scenarios.

**1. InfiniBand**

InfiniBand is a high-performance networking technology designed for high-bandwidth, low-latency data transmission. It is widely used in supercomputing and HPC environments.

**Advantages:**

- **High Bandwidth:** InfiniBand offers extremely high bandwidth, with the latest standards reaching hundreds of Gbps.
- **Low Latency:** InfiniBand provides ultra-low latency, typically in the microsecond range, making it ideal for applications requiring fast data transfer.
- **RDMA Support:** InfiniBand natively supports RDMA, enabling direct memory access and significantly enhancing data transmission efficiency.

**Disadvantages:**

- **High Cost:** InfiniBand hardware and maintenance costs are relatively high, making it less suitable for projects with limited budgets.

**Applications:**

InfiniBand is often used in supercomputing centers and research institutions that require exceptional computing power and data transfer speeds. Its high-performance characteristics make it well-suited for deep learning training and scientific computing tasks involving large-scale data processing.

**2. RoCE (RDMA over Converged Ethernet)**

RoCE is an Ethernet-based RDMA technology designed to bring the high-efficiency data transfer capabilities of RDMA into traditional Ethernet environments.

**Advantages:**

- **Ethernet Compatibility:** RoCE is compatible with existing Ethernet infrastructure, making it more flexible and cost-effective to deploy and maintain.
- **Cost-Effective:** Although RoCE's performance is slightly lower than InfiniBand, its lower hardware and maintenance costs make it suitable for most HPC and data center applications.

**Disadvantages:**

- **Slightly Lower Performance:** Compared to InfiniBand, RoCE offers slightly lower bandwidth and higher latency, but it still meets the requirements of most applications.

**Applications:**

RoCE is widely used in data centers and enterprise computing environments, particularly in systems already utilizing Ethernet architectures. It provides a balanced solution between cost and performance, promoting the adoption of efficient RDMA technology across a broader range of applications.
