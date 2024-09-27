---
sidebar_position: 3
title: Ollama
sidebar_label: Ollama
---

# Ollama

Ollama 是一个开源的大型语言模型服务工具，它允许用户在自己的硬件环境中轻松部署和使用大规模预训练模型，用户可以使用它通过 API 或 Web 界面调用这些模型执行任务，如生成文本、进行对话、代码生成等。Neolink.AI 平台现已集成 Ollama-WebUI 镜像。

## 如何使用

创建实例时，选择镜像名前缀为 **ollama-webui** 的镜像。实例创建完成后，在实例列表右侧的内置工具中会显示 **Ollama** 和 **WebUI** 两个工具，分别对应 Ollama 的 API 接口和 Web 用户界面。

__NOTE：__ 不支持在无卡模式下使用。

<img src={require('../../../../../static/img/tools/ollama-1.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

接下来将介绍如何使用 Ollama 的命令行、WebUI 界面以及 API 接口三种方式与大语言模型进行对话。

### Ollama 命令

Ollama 提供了一些基本命令，可以方便地进行模型的下载、启动、删除等操作。

ollama run 命令用于启动并运行指定的语言模型，允许用户与模型进行实时对话或推理。如果指定的模型在本地不存在，Ollama 会自动从模型库下载该模型。启动后，用户可以输入文本并接收模型生成的响应，实现实时对话。

```bash
ollama run <model_name>
```
<img src={require('../../../../../static/img/tools/ollama-7.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

如需了解 Ollama 命令更多使用方法，可参考 Ollama [官方文档](https://github.com/ollama/ollama/blob/main/README.md#quickstart)

### Ollama WebUI

Ollama Web-UI 是 Ollama 平台的一种基于 Web 的用户界面，允许用户通过浏览器与 Ollama 提供的模型进行交互。接下来我将介绍一下如何使用 Ollama WebUI 下载大语言模型实现对话。如需了解更多关于 WebUI 的用法可参考官方文档 [openwebui](https://docs.openwebui.com/features/)。

点击内置工具中的 **Ollama**，会跳转到 WebUI 登录界面，首次点击需要先进行注册。

<img src={require('../../../../../static/img/tools/ollama-3.png').default} alt="ollama" style={{width: '300px', height: 'auto'}} />

成功登录后，将进入 WebUI 界面。然而，此时还无法进行对话，因为尚未部署大语言模型。请点击左上角的**选择一个模型**下拉菜单，在文本框中输入所需拉取的模型名称，例如输入 `llama3.1`，然后点击**从 Ollama.com 拉取 "llama3.1"**。系统将自动开始拉取模型，并显示下载进度。

<img src={require('../../../../../static/img/tools/ollama-4.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

在模型下载后，我们就可以实现对话。

<img src={require('../../../../../static/img/tools/ollama-5.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />

### Ollama API

Ollama API 提供了一种简单的方式，允许开发者通过编程接口与 Ollama 模型进行交互。通过 Ollama API，用户可以轻松集成和调用大型语言模型，实现各种自然语言处理任务。此外，Ollama 兼容 OpenAI 的 [Chat Completions API](https://github.com/ollama/ollama/blob/main/docs/openai.md)，用户可以在本地使用更多与 OpenAI API 相关的工具和应用程序，与 Ollama 模型进行交互，而不需要依赖外部服务。

点击内置工具中的 **Ollama**，会跳转到 API 获取界面。

<img src={require('../../../../../static/img/tools/ollama-2.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />

地址栏中地址就为 Ollama API。下面将介绍如何使用 API 来实现问答。如需了解 Ollama API 的更多用法可参考官方[API 文档](https://github.com/ollama/ollama/blob/main/docs/api.md)。

- cURL

    ```bash
    curl https://985046a9-50d0-4f5d-be1d-fbad9568xxxx.gw.neolink-ai.com/ollama-api/api/chat \
        -H "Content-Type: application/json" \
        -d '{
            "model": "llama3.1",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "what is llama?"
                }
            ],
        "stream": false
        }'
    ```

    <img src={require('../../../../../static/img/tools/ollama-6.png').default} alt="ollama" style={{width: '800px', height: 'auto'}} />

- Open Python library

    __NOTE__: api_key 是一个必填参数，但在实际使用过程中并不会被真正用到，这是为了兼容 OpenAI 格式。

    ```python
    from openai import OpenAI

    client = OpenAI(
        base_url = 'https://985046a9-50d0-4f5d-be1d-fbad9568xxxx.gw.neolink-ai.com/ollama-api/v1',
        api_key='ollama', # required, but unused
    )

    response = client.chat.completions.create(
    model="llama3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The LA Dodgers won in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )
    print(response.choices[0].message.content)
    ```

     <img src={require('../../../../../static/img/tools/ollama-8.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />