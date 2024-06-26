---
sidebar_position: 1
title: 概要
sidebar_label: 概要
---
平台已经内置了以下框架及版本的镜像，使用该镜像的实例就会自带相应框架软件。如果以下自带的框架版本或Python版本不满足需求，请继续看下方配置其他版本的框架或Python方法。

### 配置环境方法

1.先查看平台内置镜像中是否有您需要的框架版本，如果有首选平台内置的镜像。

2.如果平台中没有合适的框架版本，那么查询自己的框架需要什么CUDA版本，比如PyTorch=1.9.0需要CUDA=11.1，那么可以选择Miniconda/CUDA=11.1的平台镜像，然后在镜像内安装自己需要的框架，免去安装cudatoolkit的麻烦。（平台内置的CUDA均带.h头文件，如有二次编译代码的需求更方便）。

3.如果以上条件都不满足，则可随便挑选一个Miniconda镜像，在开机后自行安装相关框架、CUDA、甚至其他版本的Python。


| 框架       | 框架版本 | Python版本                | CUDA版本          |
|------------|----------|---------------------------|------------------|
| PyTorch    | 1.1.0    | 3.7 (Ubuntu 18.04)       | 10.0             |
| PyTorch    | 1.5.1    | 3.8 (Ubuntu 18.04)       | 10.1             |
| PyTorch    | 1.6.0    | 3.8 (Ubuntu 18.04)       | 10.1             |
| PyTorch    | 1.7.0    | 3.8 (Ubuntu 18.04)       | 11.0             |
| PyTorch    | 1.8.1    | 3.8 (Ubuntu 18.04)       | 11.1             |
| PyTorch    | 1.9.0    | 3.8 (Ubuntu 18.04)       | 11.1             |
| PyTorch    | 1.10.0   | 3.8 (Ubuntu 20.04)       | 11.3             |
| PyTorch    | 1.11.0   | 3.8 (Ubuntu 20.04)       | 11.3             |
| PyTorch    | 2.0.0    | 3.8 (Ubuntu 20.04)       | 11.8             |
| PyTorch    | 2.1.0    | 3.10 (Ubuntu 22.04)      | 12.1             |
| PyTorch    | 2.3.0    | 3.12 (Ubuntu 22.04)      | 12.1             |
| TensorFlow | 1.15.5   | 3.8 (Ubuntu 20.04)       | 11.4             |
| TensorFlow | 2.5.0    | 3.8 (Ubuntu 18.04)       | 11.2             |
| TensorFlow | 2.9.0    | 3.8 (Ubuntu 20.04)       | 11.2             |
| Miniconda  | conda3   | 3.7 (Ubuntu 16.04)       | 9.0              |
| Miniconda  | conda3   | 3.8 (Ubuntu 18.04)       | 10.0             |
| Miniconda  | conda3   | 3.8 (Ubuntu 18.04)       | 10.1             |
| Miniconda  | conda3   | 3.8 (Ubuntu 18.04)       | 10.2             |
| Miniconda  | conda3   | 3.8 (Ubuntu 18.04)       | 11.1             |
| Miniconda  | conda3   | 3.8 (Ubuntu 18.04)       | 11.3             |
| Miniconda  | conda3   | 3.8 (Ubuntu 20.04)       | 11.3 (cudagl)    |
| Miniconda  | conda3   | 3.8 (Ubuntu 20.04)       | 11.6             |
| Miniconda  | conda3   | 3.8 (Ubuntu 20.04)       | 11.8             |
| Miniconda  | conda3   | 3.10 (Ubuntu 22.04)      | 11.8             |
| JAX        | 0.3.10   | 3.8 (Ubuntu 18.04)       | 11.1             |
| PaddlePaddle | 2.2.0   | 3.8 (Ubuntu 18.04)       | 11.2             |
| PaddlePaddle | 2.4.0   | 3.8 (Ubuntu 18.04)       | 11.2             |
| TensorRT   | 8.5.1    | 3.8 (Ubuntu 20.04)       | 11.8             |
| TensorRT   | 8.6.1    | 3.8 (Ubuntu 20.04)       | 11.8             |
| Gromacs    | 2022.2   | 3.8 (Ubuntu 18.04)       | 11.4             |
| Jittor     | 1.3.1    | 3.8 (Ubuntu 18.04)       | 11.3             |