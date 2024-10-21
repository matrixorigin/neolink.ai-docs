---
sidebar_position: 4
title: Comfyui
sidebar_label: Comfyui
---

# ComfyUI

ComfyUI 是一个强大且灵活的图形界面工具，专为处理稳定扩散模型（Stable Diffusion）而设计。它允许用户通过拖放节点的方式，轻松构建和管理复杂的推理流程。ComfyUI 支持多种模型格式，如 `checkpoint`、Lora、ControlNet 等，并能够进行模型组合和优化，适用于模型推理、图片生成和深度学习相关开发任务。

本文将介绍如何在 `neolink.ai` 平台上使用官方 ComfyUI 镜像进行部署。

## 部署步骤

### 1. 创建算力实例

首先，在 `neolink.ai` 平台上进行登录，并按照以下步骤操作：

1. 在主界面找到 **算力实例**，然后点击 **创建实例**。
2. **推荐选择单卡模式**，因为多卡模式目前不支持 ComfyUI 的部署。
3. **显卡推荐 4090**，此显卡性价比最高且兼容性最佳。3090 和 H100 也可使用，但暂不支持 H20。
4. **数据盘配置不要修改**，请保持默认挂载路径设置。
5. 在镜像选择上，找到 **官方镜像**，然后选择以下镜像版本：
   - `comfyui:0.22-SDXL-python3.11-pytorch2.4.1-cuda12.1.0-ubuntu22.04`
6. 输入 **实例名称**，并确认其他参数配置无误。

**截图示例：**
<img src={require('../../../../../static/img/comfyui/1.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../../static/img/comfyui/2.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 2. 部署实例

在点击 **立即创建** 按钮之前，请确保完成以下设置：

1. 取消勾选无卡模式，以确保 GPU 正常使用。
2. 不要修改数据盘的挂载路径，保持默认配置。这是为了确保 ComfyUI 的部署和运行能够顺利进行。
   完成以上步骤后，点击 **立即创建** 按钮，系统会开始部署实例。部署过程可能需要几分钟，具体时长取决于资源的可用性。

**截图示例：**
<img src={require('../../../../../static/img/comfyui/3.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 3. 部署完成

一旦实例创建完成，你可以通过平台的内置工具来启动 ComfyUI。启动步骤如下：

1. 进入 `neolink.ai` 平台的 **算力实例** 页面。
2. 在已部署好的实例中，找到 **内置工具** 选项。
3. 点击 **ComfyUI**，即可打开部署好的 ComfyUI 镜像。
4. 点击 **Queue Prompt**，即可开始进行图片生成操作。

**截图示例：**
<img src={require('../../../../../static/img/comfyui/4.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../../static/img/comfyui/7.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

ComfyUI 的详细教程请参考官方文档：[ComfyUI 官方 GitHub](https://github.com/comfyanonymous/ComfyUI)。
启动后，你可以通过 Web 界面进行模型推理和开发，所有配置和依赖已经准备完毕，ComfyUI 可立即使用。

## 上传 Checkpoint 文件

这里我们以`ghostmix_v20Bakedvae.safetensors`模型为例，详细讲解如何上传`checkpoint`文件。更多关于文件上传的详细教程，请参考官方文档：[数据存储->存储管理->大文件上传](https://neolink-ai.com/docs/DataStorage/createstorage)。

### 1.上传模型

通过大文件上传指引 [数据存储->存储管理->大文件上传](https://neolink-ai.com/docs/DataStorage/createstorage) 进行模型上传。由于文件较大，上传过程可能较慢，请耐心等待。

### 2.移动至目标文件夹

上传好的文件保存在`data`数据盘下，因此需要移动至目标文件夹`checkpoint`下

1. 在已部署好的实例中，找到 **内置工具** 选项，通过 ssh 登陆指令和密码进行登录
   <img src={require('../../../../../static/img/comfyui/8.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

2.移动文件至目标文件夹`checkpoint`下
<img src={require('../../../../../static/img/comfyui/9.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 3.使用模型

刷新 comfyui 镜像即可选择`ghostmix_v20Bakedvae.safetensors`模型进行创作。
<img src={require('../../../../../static/img/comfyui/10.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

---

通过以上步骤，你可以在 `neolink.ai` 平台上成功部署并启动 ComfyUI，上传自己的模型文件，并利用 ComfyUI 的功能进行开发和模型推理。
