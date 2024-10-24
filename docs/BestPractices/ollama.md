---
sidebar_position: 2
title: Deploying Large Language Models with Ollama
sidebar_label: Deploying Large Language Models with Ollama
---

# Deploying Large Language Models with Ollama

## What is Ollama?

Ollama is an open-source tool designed for large language model services, enabling users to easily deploy and utilize large-scale pre-trained models on their own hardware environments. Its primary feature is managing and deploying large language models (LLMs) inside Docker containers, allowing users to run these models locally with minimal effort. By simplifying the deployment process, Ollama ensures that users can run open-source large language models on their local environment with a single command after installation.

## Prerequisites

- Complete the [instance creation](../QuickStart/instance%20getstarted.md) process, ensuring you select an image that includes `ollama-webui`.

## Downloading a Large Language Model

Here, we use `qwen:0.5b` as an example.

```bash
ollama pull qwen:0.5b
```

<img src={require('../../static/img/demo2/ollama-1.png').default} alt="下载 qwen:0.5b" style={{width: '1000px', height: 'auto'}} />

## Running the Large Language Model

```bash
ollama run qwen:0.5b
```

<img src={require('../../static/img/demo2/ollama-1.png').default} alt="运行 qwen:0.5b" style={{width: '1000px', height: 'auto'}} />

At this point, you have successfully deployed a large language model on your instance and enabled knowledge-based Q&A.
