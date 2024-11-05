---
sidebar_position: 3
title: 搭建你的个性化 ChatGPT 服务
sidebar_label: 搭建你的个性化 ChatGPT 服务
---

# 轻松在 neolink.ai 上搭建你的个性化 ChatGPT 服务

在人工智能领域，私人定制的聊天机器人正迅速崭露头角，成为技术爱好者追捧的新趋势。这些机器人不仅仅局限于简单的问答互动，还具备深度学习用户行为和偏好的能力，进而提供更加精准、个性化的服务，满足用户的多样化需求。

在 **neolink.ai** 上，你只需一键，就能免费部署你的私人 ChatGPT 网页应用，轻松接入智能服务。不管是 **Meta-Llama-3-8B**，还是 **Qwen2-7B-Instruct** 和 **GLM-4-9B-Chat**，这些先进的 AI 模型都能给你带来高效又个性化的对话体验。有了这些强大的模型支持，你的专属聊天助手不仅能更懂你，还能在工作和生活中给你提供更贴心、更智能的帮助。

## 操作指南：

### 1. 下载实例代码

进入终端界面，输入下面的指令，下载实例代码：

```bash
git clone https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web.git
```

<img src={require('../../../../../static/img/bestpractice/chatgpt-1.png').default} alt="下载实例代码" style={{width: '1000px', height: 'auto'}} />

### 2. 安装依赖

#### [Node.js ](https://nodejs.org/en)

验证安装： 打开命令行或终端，输入以下命令来验证 Node.js 是否安装成功：

```bash
node -v
npm -v
```

#### [yarn](https://yarnpkg.com/getting-started/install)

- **macOS 和 Linux**：使用以下命令来安装 Yarn：
  ```bash
  curl -o- -L https://yarnpkg.com/install.sh | bash
  ```
- 或者使用 npm 安装 Yarn：
  ```bash
  npm install --global yarn
  ```
- 验证 Yarn 是否安装成功：
  ```bash
  yarn --version
  ```

### 3. 获得 API key

- 注册并登录 [Neolink.ai](https://neolink-ai.com/) 官网，进入控制台界面，左侧导航栏点击 **模型广场**，选取你需要的大模型，这里我们以 **Qwen2-7B-Instruct** 为例。
  <img src={require('../../../../../static/img/bestpractice/chatgpt-2.png').default} alt="获得 API key-1" style={{width: '1000px', height: 'auto'}} />
- 在控制台首页，左侧导航栏点击 **API 管理**，创建你自己的 API Key。
  <img src={require('../../../../../static/img/bestpractice/chatgpt-3.png').default} alt="获得 API key-2" style={{width: '1000px', height: 'auto'}} />

### 4. 修改配置

- 打开下载的文件，找到 `next.config.mjs`，在 `nextConfig.rewrites = async () => {` 后添加：
  ```javascript
  {
      source: "/api/v1/chat/completions",
      destination: "https://neolink-ai.com/model/api/v1/chat/completions",
  }
  ```
  <img src={require('../../../../../static/img/bestpractice/chatgpt-4.png').default} alt="修改配置-1" style={{width: '1000px', height: 'auto'}} />
- 将 `.env.template` 文件复制一份，并将其重命名为 `.env.local`。
  <img src={require('../../../../../static/img/bestpractice/chatgpt-5.png').default} alt="修改配置-2" style={{width: '1000px', height: 'auto'}} />
- 修改 `.env.local` 的配置：
  ```
  BASE_URL=https://neolink-ai.com/model/api
  ```
  <img src={require('../../../../../static/img/bestpractice/chatgpt-6.png').default} alt="修改配置-3" style={{width: '1000px', height: 'auto'}} />

### 5. 启动项目

- 在 `ChatGPT-Next-Web` 文件夹下启动项目，初次启动可能稍微有些慢，请耐心等待：
  ```bash
  yarn install && yarn dev
  ```
  <img src={require('../../../../../static/img/bestpractice/chatgpt-7.png').default} alt="启动项目" style={{width: '1000px', height: 'auto'}} />
- 启动成功后，在浏览器输入以下地址访问首页：
  [http://localhost:3000/](http://localhost:3000/)

### 6. 修改配置

- 在浏览器输入 [http://localhost:3000/#/settings](http://localhost:3000/#/settings)，进入设置界面。
- 输入你之前创建的 API Key，并选择对应的模型（以 **Qwen/Qwen2-7B-Instruct** 为例）。
  <img src={require('../../../../../static/img/bestpractice/chatgpt-8.png').default} alt="修改配置-1" style={{width: '1000px', height: 'auto'}} />
- 返回主页，即可使用模型进行对话。
  <img src={require('../../../../../static/img/bestpractice/chatgpt-9.png').default} alt="修改配置-2" style={{width: '1000px', height: 'auto'}} />

通过上述步骤操作，你已成功部署你的个性化 ChatGPT 服务。未来，借助 neolink.ai 平台的不断升级，你的 AI 助手将变得更加强大，为你带来更多意想不到的惊喜与价值。快去 [neolink.ai](https://neolink-ai.com/) 上体验并探索更多可能性吧！
