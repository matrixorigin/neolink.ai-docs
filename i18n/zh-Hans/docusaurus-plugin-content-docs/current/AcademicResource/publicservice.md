---
sidebar_position: 1
title: 公开服务
sidebar_label: 公开服务
---

__NOTE:__ 本加速代理服务旨在缓解学术用途中访问 GitHub 和 Hugging Face 时遇到的网络速度问题，方便用户获取相关资源。请注意，本服务不提供稳定性保障，且在遭遇恶意攻击等情况下，可能会随时中止服务。


## Github 镜像站

**服务地址**：[https://githubfast.com/](https://githubfast.com/)

在克隆仓库时，将 `https://github.com` 替换为 `https://githubfast.com` 进行加速。例如：
```bash
git clone https://githubfast.com/xxx/xxx.git
```

下载 GitHub 文件：当你想下载 GitHub 上的文件时，可以通过 https://githubfast.com/ 进行加速。例如：
```bash
wget https://githubfast.com/xx/xxx.zip
```

## HuggingFace 镜像站

**服务地址**：[https://hf-mirror.com/](https://hf-mirror.com/)

下载 Hugging Face 模型：可以在模型 URL 前添加镜像站地址进行加速。例如：

```bash
from transformers import AutoModelForSequenceClassification, AutoTokenizer  model_name ="bert-base-uncased"model = AutoModelForSequenceClassification.from_pretrained(f"https://hf-mirror.com/models/{model_name}/") tokenizer = AutoTokenizer.from_pretrained(f"https://hf-mirror.com/models/{model_name}/")
```

替换模型下载 URL：直接将下载模型的 URL 替换为镜像站 URL。例如：

```bash
model_name = "bert-base-uncased"model_url = f"https://hf-mirror.com/models/{model_name}/"
```



