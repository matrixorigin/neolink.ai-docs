---
sidebar_position: 2
title: HuggingFace Mirror
sidebar_label: HuggingFace Mirror
---

**NOTE:** This proxy acceleration service aims to alleviate network speed issues encountered in academic usage scenarios when accessing Hugging Face, making it easier for users to obtain related resources. Please be aware that this service does not offer stability guarantees and may be terminated at any time in case of malicious attacks or other disruptions.

**Service URL:** [https://hf-mirror.com/](https://hf-mirror.com/)

Below is an example of how to download the `bert-base-uncased` model on Hugging Face:

- Set up environment variables

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

- Install the transformers library

```bash
pip install transformers
```

- Download the Hugging Face model

Write and run the following Python code:

```python
from transformers import AutoModel, AutoTokenizer

# Download BERT model and tokenizer
model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("BERT model downloaded successfully!")
```

<img src={require('../../static/img/accerate/acc-1.png').default} alt="创建集群" style={{width: '700px', height: 'auto'}} />
