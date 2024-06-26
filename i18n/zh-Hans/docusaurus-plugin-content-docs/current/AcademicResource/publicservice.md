---
sidebar_position: 1
title: 公开服务
sidebar_label: 公开服务
---
## Github代理

**服务地址**：[https://ghproxy.com/](https://ghproxy.com/)

在克隆仓库时，可以通过在 URL 前添加 `https://ghproxy.com/` 进行加速。例如：
```bash
git clone https://ghproxy.com/https://github.com/user/repository.git
```

下载 GitHub 文件：当你想下载 GitHub 上的文件时，可以通过https://ghproxy.com/ 进行加速。例如：
```bash
wget https://ghproxy.com/https://github.com/user/repository/archive/refs/heads/main.zip
```

配置 Git 代理：在 Git 全局配置中添加代理设置：
```bash
git config --global http.proxy https://ghproxy.com/ git config --global https.proxy https://ghproxy.com/
```


## HuggingFace镜像站
**服务地址**：[https://hf-mirror.com/](https://hf-mirror.com/)

下载 Hugging Face 模型：可以在模型 URL 前添加镜像站地址进行加速。例如：
```bash
from transformers import AutoModelForSequenceClassification, AutoTokenizer  model_name ="bert-base-uncased"model = AutoModelForSequenceClassification.from_pretrained(f"https://hf-mirror.com/models/{model_name}/") tokenizer = AutoTokenizer.from_pretrained(f"https://hf-mirror.com/models/{model_name}/")
```

替换模型下载 URL：直接将下载模型的 URL 替换为镜像站 URL。例如：
```bash
model_name = "bert-base-uncased"model_url = f"https://hf-mirror.com/models/{model_name}/"
```



