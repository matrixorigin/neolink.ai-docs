---
sidebar_position: 4
title: Agent应用
sidebar_label: Agent应用
---

用户可以使用 Agent 工具构建基于 Chat 对话模式的 Agent 应用，该应用支持访问知识库，提供对话的上下文信息。用户可通过公开访问入口或 API 集成两种方式进行接入。

<iframe width="640" height="360" 
  src="https://community-shared-data-1308875761.cos.ap-beijing.myqcloud.com/artwork/neolinkdocs/video/agent.mov" 
  frameborder="0" allowfullscreen>
</iframe>

## 创建 Agent

在平台左侧模型服务处找到** Agent 应用**，在右侧点击**创建 Agent**。

<img src={require('../../../../../static/img/knowledge/agent-1.png').default} alt="创建 agent" style={{width: '600px', height: 'auto'}} />

## 发布 Agent

点击 Agent 列表中你想要发布的 Agent，进入详情页面。要创建一个完整的 Agent，需要设置以下几项：

- **提示词**（System prompt）：定义 Agent 的角色、职责和技能，控制对话的基调和方向。
- **知识库**：默认情况下为空，可根据需求导入知识库，作为上下文参考。关于知识库的详细使用方式，请参阅 [知识服务](../KnowledgeBase/knowledge-service.md) 章节。
- **模型服务**：选择 Agent 对话使用的大语言模型，支持 Neolink 和 OpenAI 提供的模型服务，但需要注意的是，OpenAI 存在网络连接问题，API Base 需要填写 OpenAI 代理地址，因为目前无法直接连接官方的 OpenAI endpoint。

设置完毕后后，可以在右侧的 **调试与预览** 界面进行测试，以验证 Agent 的实际表现并进行调整。

<img src={require('../../../../../static/img/knowledge/agent-2.png').default} alt="创建 agent" style={{width: '600px', height: 'auto'}} />

调试完毕，点击右上角**发布**按钮即可进行发布。回到 Agent 列表，可以看到 Agent 状态为**已发布**。

<img src={require('../../../../../static/img/knowledge/agent-3.png').default} alt="创建 agent" style={{width: '600px', height: 'auto'}} />

您可以随时对 Agent 进行修改和更新。

## 访问统计

在**访问与统计**页面，我们统计了 Agent 应用的消息数量和 token 调用量，统计包含了调试预览阶段的数据。

<img src={require('../../../../../static/img/knowledge/agent-4.png').default} alt="创建 agent" style={{width: '800px', height: 'auto'}} />

复制访问 URL 并在浏览器中打开，即可直接运行 Agent。该 URL 地址支持分享，外部用户无需登录账户即可访问和使用该 Agent。

<img src={require('../../../../../static/img/knowledge/agent-5.png').default} alt="创建 agent" style={{width: '600px', height: 'auto'}} />
