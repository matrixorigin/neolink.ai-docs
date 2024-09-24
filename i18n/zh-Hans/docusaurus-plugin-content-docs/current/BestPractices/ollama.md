---
sidebar_position: 2
title: 使用 Ollama 部署大语言模型
sidebar_label: 使用 Ollama 部署大语言模型
---

# 使用 Ollama 部署大语言模型

## Ollama 是什么？

Ollama 是一个开源的大型语言模型服务工具，它允许用户在自己的硬件环境中轻松部署和使用大规模预训练模型。Ollama 的主要功能是在 Docker 容器内部署和管理大型语言模型（LLM），使用户能够快速地在本地运行这些模型。Ollama 简化了部署过程，通过简单的安装指令，用户可以执行一条命令就在本地运行开源大型语言模型。


## 前置依赖

- 完成[实例的创建](../QuickStart/instance%20getstarted.md)，注意需选用带有 ollama-webui 的镜像。

## 下载大语言模型

这里以 qwen:0.5b 为例。

```bash
ollama pull qwen:0.5b
```

<img src={require('../../../../../static/img/demo2/ollama-1.png').default} alt="下载qwen:0.5b" style={{width: '1000px', height: 'auto'}} />

## 运行大语言模型

```bash
ollama run qwen:0.5b
```

<img src={require('../../../../../static/img/demo2/ollama-1.png').default} alt="运行qwen:0.5b" style={{width: '1000px', height: 'auto'}} />

至此，你已成功在实例部署大语言模型并实现知识问答。