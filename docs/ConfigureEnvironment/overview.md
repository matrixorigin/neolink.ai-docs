---
sidebar_position: 1
title: overview
sidebar_label: overview
---

The platform provides built-in images with the following frameworks and versions. Instances created with these images will come pre-installed with the corresponding framework software. If the pre-installed framework versions or Python versions do not meet your requirements, please refer to the methods below for configuring other versions.

### Environment Configuration Methods

1. **Check for Built-in Framework Versions:**
   First, verify if the required framework version is available in the platform's built-in images. If it is, prioritize using the built-in image.

2. **Install Frameworks Using CUDA-Compatible Images:**  
   If the required framework version is not available, determine which CUDA version your framework needs. For example, PyTorch 1.9.0 requires CUDA 11.1. In this case, select a platform image with Miniconda/CUDA 11.1 and install the required framework within the image. This saves the effort of installing `cudatoolkit`. (The platform's CUDA images include header files (.h), making it more convenient for secondary code compilation if needed.)

3. **Manual Installation:**  
   If neither of the above options meets your needs, you can select any Miniconda image and manually install the necessary frameworks, CUDA, or even other Python versions after the instance starts.

| framework    | framework version | Python version      | CUDA version  |
| ------------ | ----------------- | ------------------- | ------------- |
| PyTorch      | 1.1.0             | 3.7 (Ubuntu 18.04)  | 10.0          |
| PyTorch      | 1.5.1             | 3.8 (Ubuntu 18.04)  | 10.1          |
| PyTorch      | 1.6.0             | 3.8 (Ubuntu 18.04)  | 10.1          |
| PyTorch      | 1.7.0             | 3.8 (Ubuntu 18.04)  | 11.0          |
| PyTorch      | 1.8.1             | 3.8 (Ubuntu 18.04)  | 11.1          |
| PyTorch      | 1.9.0             | 3.8 (Ubuntu 18.04)  | 11.1          |
| PyTorch      | 1.10.0            | 3.8 (Ubuntu 20.04)  | 11.3          |
| PyTorch      | 1.11.0            | 3.8 (Ubuntu 20.04)  | 11.3          |
| PyTorch      | 2.0.0             | 3.8 (Ubuntu 20.04)  | 11.8          |
| PyTorch      | 2.1.0             | 3.10 (Ubuntu 22.04) | 12.1          |
| PyTorch      | 2.3.0             | 3.12 (Ubuntu 22.04) | 12.1          |
| TensorFlow   | 1.15.5            | 3.8 (Ubuntu 20.04)  | 11.4          |
| TensorFlow   | 2.5.0             | 3.8 (Ubuntu 18.04)  | 11.2          |
| TensorFlow   | 2.9.0             | 3.8 (Ubuntu 20.04)  | 11.2          |
| Miniconda    | conda3            | 3.7 (Ubuntu 16.04)  | 9.0           |
| Miniconda    | conda3            | 3.8 (Ubuntu 18.04)  | 10.0          |
| Miniconda    | conda3            | 3.8 (Ubuntu 18.04)  | 10.1          |
| Miniconda    | conda3            | 3.8 (Ubuntu 18.04)  | 10.2          |
| Miniconda    | conda3            | 3.8 (Ubuntu 18.04)  | 11.1          |
| Miniconda    | conda3            | 3.8 (Ubuntu 18.04)  | 11.3          |
| Miniconda    | conda3            | 3.8 (Ubuntu 20.04)  | 11.3 (cudagl) |
| Miniconda    | conda3            | 3.8 (Ubuntu 20.04)  | 11.6          |
| Miniconda    | conda3            | 3.8 (Ubuntu 20.04)  | 11.8          |
| Miniconda    | conda3            | 3.10 (Ubuntu 22.04) | 11.8          |
| JAX          | 0.3.10            | 3.8 (Ubuntu 18.04)  | 11.1          |
| PaddlePaddle | 2.2.0             | 3.8 (Ubuntu 18.04)  | 11.2          |
| PaddlePaddle | 2.4.0             | 3.8 (Ubuntu 18.04)  | 11.2          |
| TensorRT     | 8.5.1             | 3.8 (Ubuntu 20.04)  | 11.8          |
| TensorRT     | 8.6.1             | 3.8 (Ubuntu 20.04)  | 11.8          |
| Gromacs      | 2022.2            | 3.8 (Ubuntu 18.04)  | 11.4          |
| Jittor       | 1.3.1             | 3.8 (Ubuntu 18.04)  | 11.3          |
