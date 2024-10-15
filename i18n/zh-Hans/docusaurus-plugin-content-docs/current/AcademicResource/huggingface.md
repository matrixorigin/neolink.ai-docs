---
sidebar_position: 2
title: HuggingFace 镜像站
sidebar_label: HuggingFace 镜像站
---

# huggingface

Hugging Face 是一家专注于人工智能和自然语言处理的公司，提供了一个开源平台和工具集合（如 Transformers 库），帮助开发者轻松使用预训练模型，尤其在文本处理和机器学习领域。

<img src={require('../../../../../static/img/huggingface/1.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

开发者可以在 Hugging Face 上访问和使用成千上万的预训练模型，进行模型微调，处理开源数据集，或者在 Model Hub 上分享和寻找模型。同时，他们还可以利用无代码工具快速搭建 AI 应用，或通过 API 轻松集成模型到自己的项目中。

**NOTE:** 本加速代理服务旨在缓解学术用途中访问 Hugging Face 时遇到的网络速度问题，方便用户获取相关资源。请注意，本服务不提供稳定性保障，且在遭遇恶意攻击等情况下，可能会随时中止服务。

## 如何使用镜像站

### 方法一：网页下载

在镜像站内[https://hf.neolink-ai.com/](https://hf.neolink-ai.com/)搜索，并在模型主页的**Files and Version**中下载文件
<img src={require('../../../../static/img/huggingface/2.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../static/img/huggingface/3.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 方法二：huggingface-cli

`huggingface-cli` 是 Hugging Face 官方提供的命令行工具，用于下载、管理和操作 Hugging Face 平台上的模型和数据集。

#### 1. 安装依赖

```bash
pip install -U huggingface_hub
```

### 2. 设置环境变量

Linux

```bash
export HF_ENDPOINT=https://hf.neolink-ai.com
```

Windows Powershell

```bash
$env:HF_ENDPOINT = "https://hf.neolink-ai.com"
```

建议将上面这一行写入`~/.bashrc`

#### 3.1 下载模型

```bash
huggingface-cli download --resume-download gpt2 --local-dir gpt2
```

#### 3.2 下载数据集

```bash
huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext
```

可以添加 `--local-dir-use-symlinks False` 参数禁用文件软链接，这样下载路径下所见即所得。

编写 python 代码并运行：

```python
from transformers import AutoModel, AutoTokenizer

# 下载 BERT 模型和分词器
model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("BERT 模型下载完成！")
```

<img src={require('../../../../../static/img/huggingface/4.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 方法三：使用环境变量（非侵入式）

非侵入式，能解决大部分情况。huggingface 工具链会获取`HF_ENDPOINT`环境变量来确定下载文件所用的网址，所以可以使用通过设置变量来解决。

```bash
HF_ENDPOINT=https://hf.neolink-ai.com python your_script.py
```

不过有些数据集有内置的下载脚本，那就需要手动改一下脚本内的地址来实现了。

### 常见问题

#### Q:有些项目需要登录，如何下载？

#### A:部分 Gated Repo 需登录申请许可。为保障账号安全，本站不支持登录，需先前往 Hugging Face 官网登录、申请许可，在[官网](https://huggingface.co/settings/tokens)这里获取 Access Token 后回镜像站用命令行下载。

### huggingface-cli： 添加`--token`参数

```bash
huggingface-cli download --token hf_*** --resume-download meta-llama/Llama-2-7b-hf --local-dir Llama-2-7b-hf
```

### hfd： 添加`--hf_username` `--hf_token`参数

```bash
hfd meta-llama/Llama-2-7b --hf_username YOUR_HF_USERNAME --hf_token hf_***
```

其余如`from_pretrained`、`wget`、`curl`如何设置认证 token，详见上面第一段提到的教程。
