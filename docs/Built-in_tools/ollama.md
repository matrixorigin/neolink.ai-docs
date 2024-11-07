---
sidebar_position: 3
title: Ollama
sidebar_label: Ollama
---

# Ollama

Ollama is an open-source large language model service tool that allows users to easily deploy and use large pre-trained models on their own hardware. Users can call these models via API or a web interface to perform tasks such as text generation, conversation, and code generation. The Neolink.AI platform now integrates the Ollama-WebUI image.

## How to Use

When creating an instance, select an image with the **ollama-webui** prefix. Once the instance is created, two tools—**Ollama** and **WebUI**—will appear under the built-in tools on the right side of the instance list. These correspond to the Ollama API interface and the web user interface, respectively.

**NOTE:** Not supported in no-GPU mode.

<img src={require('../../static/en-img/ollama/ollama-1.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

Next, we will introduce how to interact with large language models using three methods: the command line, the WebUI interface, and the API.

### Ollama Commands

Ollama provides several basic commands to facilitate downloading, launching, and deleting models.

The `ollama run` command is used to start and run a specified language model, enabling users to engage in real-time conversations or inference. If the specified model is not available locally, Ollama will automatically download it from the model library. Once launched, users can input text and receive model-generated responses for real-time interaction.

```bash
ollama run <model_name>
```

<img src={require('../../static/en-img/ollama/ollama-7.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

For more information on how to use Ollama commands, refer to the official Ollama [documentation](https://github.com/ollama/ollama/blob/main/README.md#quickstart).

### Ollama WebUI

Ollama WebUI is a web-based user interface that allows users to interact with models provided by Ollama through a browser. Below, we will introduce how to use the Ollama WebUI to download a large language model and conduct a conversation. For more details on how to use the WebUI, refer to the official [openwebui documentation](https://docs.openwebui.com/features/).

Click on **Ollama** under the built-in tools to access the WebUI login page. On your first visit, registration will be required.

<img src={require('../../static/en-img/ollama/ollama-3.png').default} alt="ollama" style={{width: '300px', height: 'auto'}} />

After successfully logging in, you will enter the WebUI interface. However, you cannot initiate a conversation just yet because no large language model has been deployed. Click on the **Select a Model** dropdown menu in the upper left corner, enter the desired model name in the text box, such as `llama3.1`, and click **Pull 'llama3.1' from Ollama.com**. The system will automatically begin downloading the model and display the download progress.

<img src={require('../../static/en-img/ollama/ollama-4.png').default} alt="ollama" style={{width: '500px', height: 'auto'}} />

Once the model is downloaded, you can start a conversation.

<img src={require('../../static/en-img/ollama/ollama-5.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />

### Ollama API

The Ollama API provides a simple way for developers to interact with Ollama models programmatically. Through the Ollama API, users can easily integrate and invoke large language models to perform various natural language processing tasks. Additionally, Ollama is compatible with OpenAI's [Chat Completions API](https://github.com/ollama/ollama/blob/main/docs/openai.md), allowing users to use more OpenAI-related tools and applications locally to interact with Ollama models without relying on external services.

Click on **Ollama** under the built-in tools to access the API page.

<img src={require('../../static/en-img/ollama/ollama-2.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />

The address shown in the browser's address bar is the Ollama API endpoint. Below, we will introduce how to use the API to perform Q&A tasks. For more information on the Ollama API, refer to the official [API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).

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

  <img src={require('../../static/en-img/ollama/ollama-6.png').default} alt="ollama" style={{width: '800px', height: 'auto'}} />

- Open Python library

  **NOTE**: The `api_key` is a required parameter, but it is not actually used in practice. This is for compatibility with the OpenAI format.

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

  <img src={require('../../static/en-img/ollama/ollama-8.png').default} alt="ollama" style={{width: '600px', height: 'auto'}} />
