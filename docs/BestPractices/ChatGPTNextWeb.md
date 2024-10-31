---
sidebar_position: 3
title: Build Your Personalized ChatGPT Service
sidebar_label: Build Your Personalized ChatGPT Service
---

# Easily Build Your Personalized ChatGPT Service on neolink.ai

In the field of artificial intelligence, personalized chatbots are rapidly emerging as a new trend favored by tech enthusiasts. These chatbots go beyond simple Q&A interactions, leveraging deep learning to understand user behavior and preferences, offering more precise and personalized services to meet diverse user needs.

On **neolink.ai**, you can deploy your private ChatGPT web application with just one click, seamlessly connecting with intelligent services. Whether using **Meta-Llama-3-8B**, **Meta-Llama-3.1-405B**, **Qwen2-7B-Instruct**, or **GLM-4-9B-Chat**, these advanced AI models deliver efficient and customized conversational experiences. With the support of these powerful models, your personalized chatbot becomes more intuitive, providing smarter, more thoughtful assistance in both work and everyday life.

## Instructions:

### 1. Download the Example Code

Open the terminal and enter the following command to download the example code:

```bash
git clone https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web.git
```

<img src={require('../../static/img/bestpractice/chatgpt-1.png').default} alt="Download the Example Code" style={{width: '1000px', height: 'auto'}} />

### 2. Install Dependencies

#### [Node.js](https://nodejs.org/en)

Verify Installation:  
Open the command line or terminal and enter the following command to verify if Node.js is installed successfully:

```bash
node -v
npm -v
```

#### [yarn](https://yarnpkg.com/getting-started/install)

- **macOS and Linux**: Use the following command to install Yarn:
  ```bash
  curl -o- -L https://yarnpkg.com/install.sh | bash
  ```
- or use npm to install Yarn：
  ```bash
  npm install --global yarn
  ```
- Verify Installation:
  ```bash
  yarn --version
  ```

### 3. Get Your API Key

- Register and log in to the [Neolink.ai](https://neolink-ai.com/) website. Navigate to the console, and click **Model Plaza** in the left sidebar to choose the model you need. Here, we use **Qwen2-7B-Instruct** as an example.  
  <img src={require('../../static/img/bestpractice/chatgpt-2.png').default} alt="Get API Key - Step 1" style={{width: '1000px', height: 'auto'}} />

- In the console homepage, click **API Management** from the left sidebar and create your own API Key.  
  <img src={require('../../static/img/bestpractice/chatgpt-3.png').default} alt="Get API Key - Step 2" style={{width: '1000px', height: 'auto'}} />

### 4. Modify Configuration

- Open the downloaded files and locate the `next.config.mjs` file. Add the following after `nextConfig.rewrites = async () => {`:

  ```javascript
  {
      source: "/api/v1/chat/completions",
      destination: "https://neolink-ai.com/model/api/v1/chat/completions",
  }
  ```

  <img src={require('../../static/img/bestpractice/chatgpt-4.png').default} alt="Modify Configuration - Step 1" style={{width: '1000px', height: 'auto'}} />

- Copy the `.env.template` file and rename it to `.env.local`.  
  <img src={require('../../static/img/bestpractice/chatgpt-5.png').default} alt="Modify Configuration - Step 2" style={{width: '1000px', height: 'auto'}} />

- Modify the configuration in `.env.local`:
  ```
  BASE_URL=https://neolink-ai.com/model/api
  ```
  <img src={require('../../static/img/bestpractice/chatgpt-6.png').default} alt="Modify Configuration - Step3" style={{width: '1000px', height: 'auto'}} />

### 5. Start the Project

- Start the project in the `ChatGPT-Next-Web` folder. The first startup might take a bit longer, so please be patient:
  ```bash
  yarn install && yarn dev
  ```
  <img src={require('../../static/img/bestpractice/chatgpt-7.png').default} alt="启动项目" style={{width: '1000px', height: 'auto'}} />
- Once started successfully, open your browser and visit the following address to access the homepage:  
  [http://localhost:3000/](http://localhost:3000/)

### 6. Update Configuration

- In your browser, go to [http://localhost:3000/#/settings](http://localhost:3000/#/settings) to open the settings page.
- Enter the API Key you created earlier and select the corresponding model (e.g., **Qwen/Qwen2-7B-Instruct**).  
  <img src={require('../../static/img/bestpractice/chatgpt-8.png').default} alt="Update Configuration - Step 1" style={{width: '1000px', height: 'auto'}} />

- Return to the homepage, and you can now start conversations with the model.  
  <img src={require('../../static/img/bestpractice/chatgpt-9.png').default} alt="Update Configuration - Step 2" style={{width: '1000px', height: 'auto'}} />

By following the steps above, you have successfully deployed your personalized ChatGPT service. With continuous upgrades from the neolink.ai platform, your AI assistant will become even more powerful, bringing you unexpected surprises and value. Visit [neolink.ai](https://neolink-ai.com/) to explore more possibilities today!
