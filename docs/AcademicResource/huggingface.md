---
sidebar_position: 2
title: HuggingFace Mirror Site
sidebar_label: HuggingFace Mirror Site
---

# huggingface

Hugging Face is a company focused on artificial intelligence and natural language processing, offering an open-source platform and toolset (such as the Transformers library) to help developers easily use pre-trained models, especially in text processing and machine learning fields.

<img src={require('../../static/img/huggingface/1.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

Developers can access and utilize thousands of pre-trained models on Hugging Face, perform model fine-tuning, process open-source datasets, or share and discover models on the Model Hub. Additionally, they can leverage no-code tools to quickly build AI applications or integrate models into their projects via APIs.

**NOTE:** This acceleration proxy service aims to address network speed issues encountered when accessing Hugging Face for academic purposes, making it easier for users to obtain relevant resources. Please note that this service does not guarantee stability and may be discontinued at any time in case of malicious attacks or other disruptions.

## How to Use the Mirror Site

### Method 1: Web Download

Search within the mirror site [https://hf.neolink-ai.com/](https://hf.neolink-ai.com/) and download files from the **Files and Version** section on the model's homepage.
<img src={require('../../static/img/huggingface/2.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../static/img/huggingface/3.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### Method 2: huggingface-cli

`huggingface-cli` is the official command-line tool provided by Hugging Face to download, manage, and operate models and datasets from the Hugging Face platform.

#### 1. Install Dependencies

```bash
pip install -U huggingface_hub
```

#### 2. Set Environment Variables

Linux

```bash
export HF_ENDPOINT=https://hf.neolink-ai.com
```

Windows Powershell

```bash
$env:HF_ENDPOINT = "https://hf.neolink-ai.com"
```

It is recommended to add the above line to your `~/.bashrc`

#### 3.1 Download a Model

```bash
huggingface-cli download --resume-download gpt2 --local-dir gpt2
```

#### 3.2 Download a Dataset

```bash
huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext
```

You can add the `--local-dir-use-symlinks False` parameter to disable symbolic links, ensuring that the downloaded content matches the visible files in the target directory.

Create and run the following Python code:

```python
from transformers import AutoModel, AutoTokenizer

# Download the BERT model and tokenizer
model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("BERT model downloaded successfully!")
```

<img src={require('../../static/img/huggingface/4.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### Method 3：Use Environment Variables (Non-intrusive)

This non-intrusive method can solve most cases. Hugging Face’s toolchain will use the `HF_ENDPOINT` environment variable to determine the URL for downloading files, so setting the variable can help resolve network issues.

```bash
HF_ENDPOINT=https://hf.neolink-ai.com python your_script.py
```

However, for certain datasets with built-in download scripts, you may need to manually update the script’s URLs.

### FAQs

#### Q:Some projects require login credentials. How can I download them?

#### A:Some gated repositories require login and permission requests. To ensure account security, this mirror site does not support login. You need to log in and request permission on the Hugging Face official website first, then obtain an Access Token from [here](https://huggingface.co/settings/tokens) and use it for command-line downloads on the mirror site.

### huggingface-cli：Use the `--token` Parameter

```bash
huggingface-cli download --token hf_*** --resume-download meta-llama/Llama-2-7b-hf --local-dir Llama-2-7b-hf
```

### hfd： Use `--hf_username` `--hf_token` Parameters

```bash
hfd meta-llama/Llama-2-7b --hf_username YOUR_HF_USERNAME --hf_token hf_***
```

### For other use cases such as `from_pretrained`、`wget`、`curl` where token authentication is needed, refer to the tutorials mentioned in the first section.
