---
sidebar_position: 3
title: 使用 comfyui 生图创作
sidebar_label: 使用 comfyui 生图创作
---

# ComfyUI

ComfyUI 是一个强大且灵活的图形界面工具，专为处理稳定扩散模型（Stable Diffusion）而设计。它允许用户通过拖放节点的方式，轻松构建和管理复杂的推理流程。ComfyUI 支持多种模型格式，如 `checkpoint`、Lora、ControlNet 等，并能够进行模型组合和优化，适用于模型推理、图片生成和深度学习相关开发任务。

本文将介绍如何在 `neolink.ai` 平台上使用官方 ComfyUI 镜像，上传模型以实现个性化创作。

## 前置依赖

- 完成[实例的创建](../Built-in_tools/comfyui.md)，注意需选用带有 comfyui-webui 的镜像。

## 上传自己的模型文件

这里我们以`ghostmix_v20Bakedvae.safetensors`模型为例，详细讲解如何上传`checkpoint`文件。更多关于文件上传的详细教程，请参考官方文档：[数据存储->存储管理->大文件上传](https://neolink-ai.com/docs/DataStorage/createstorage)。

### 1.上传模型

通过大文件上传指引 [数据存储->存储管理->大文件上传](https://neolink-ai.com/docs/DataStorage/createstorage) 进行模型上传。由于文件较大，上传过程可能较慢，请耐心等待。

### 2.移动至目标文件夹

上传好的文件保存在`data`数据盘下，因此需要移动至目标文件夹`checkpoint`下

1. 在已部署好的实例中，找到 **内置工具** 选项，通过 ssh 登陆指令和密码进行登录
   <img src={require('../../../../../static/img/comfyui/8.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

2.移动文件至目标文件夹`checkpoint`下
<img src={require('../../../../../static/img/comfyui/9.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

## 开始创作

刷新 comfyui 镜像即可选择`ghostmix_v20Bakedvae.safetensors`模型进行创作。
<img src={require('../../../../../static/img/comfyui/10.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

---

通过以上步骤，你可以在 `neolink.ai` 平台的`comfyuia`镜像上，上传自己的模型文件，并利用 ComfyUI 的功能进行开发和模型推理。
