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
3. **显卡推荐 4090**，此显卡性价比最高且兼容性最佳。H100也可使用，但暂不支持H20。
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

ComfyUI 的详细教程请参考官方文档：[ComfyUI 官方 GitHub](https://github.com/comfyanonymous/ComfyUI)。


启动后，你可以通过 Web 界面进行模型推理和开发，所有配置和依赖已经准备完毕，ComfyUI 可立即使用。

## 上传 Checkpoint 文件

目前镜像中默认加载的模型为 `sd_xl_base_1.0_0.9vae.safetensors`。如果你需要使用其他模型，用户可以通过平台的 **存储管理** 功能上传自己的模型文件或 `checkpoint` 文件：

1. 进入实例的 **存储管理** 页面。
2. 点击 **上传文件** 按钮，选择本地的 `checkpoint` 文件或者其他模型文件（Lora,ControlNet等）上传到实例中。
3. 上传速度可能较慢，建议耐心等待文件上传完成。

**截图示例：**
<img src={require('../../../../../static/img/comfyui/5.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../../static/img/comfyui/6.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 大文件上传
上传大文件到 Neolink.ai 的存储管理部分可以通过以下步骤完成：

1. **安装 mc 客户端：**
   需要安装 `mc` 客户端用于与 Neolink.ai 存储服务交互。

2. **配置存储 alias：**
   在安装 `mc` 客户端后，使用以下命令配置连接 Neolink.ai 的存储别名：
   ```
   mc config host add bucket-user-9vf4fvx0 https://file.gw.neolink-ai.com bucket-user-9vf4fvx0 Ji2CMJbB5zpvRHIeIDCK4gX3XjjiVm3Mm3YcsPls
   ```

3. **文件上传：**
   - **单个文件上传：** 使用以下命令上传所需的文件：
     ```
     mc cp <需要上传的文件路径> bucket-user-9vf4fvx0/pvc-c819d373-8638-4a9d-9ac8-7d1fe884a6af
     ```
   - **目录上传：** 如果需要上传整个目录，使用以下命令：
     ```
     mc cp --recursive <需要上传的目录路径> bucket-user-9vf4fvx0/pvc-c819d373-8638-4a9d-9ac8-7d1fe884a6af
     ```

4. **文件下载：**
   - **下载文件：** 使用以下命令下载存储中的文件：
     ```
     mc cp bucket-user-9vf4fvx0/pvc-c819d373-8638-4a9d-9ac8-7d1fe884a6af/<存储文件路径> <本地路径>
     ```
   - **下载目录：** 下载整个目录的命令为：
     ```
     mc cp --recursive bucket-user-9vf4fvx0/pvc-c819d373-8638-4a9d-9ac8-7d1fe884a6af/<存储目录路径> <本地路径>
     ```

这样通过配置 `mc` 客户端后，就可以进行大文件的上传和下载操作，方便快捷。

上传完成后，你的 `checkpoint` 文件将会被挂载到实例的指定路径中，你可以在 ComfyUI 中加载并使用你上传的模型。

**截图示例：**
<img src={require('../../../../../static/img/comfyui/4.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../../static/img/comfyui/7.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

---

通过以上步骤，你可以在 `neolink.ai` 平台上成功部署并启动 ComfyUI，上传自己的模型文件，并利用 ComfyUI 的功能进行开发和模型推理。
