---
sidebar_position: 1
title: 知识服务
sidebar_label: 知识服务
---

## 创建知识库

点击 Neolink.AI 平台左侧导航栏中的**知识服务**，进入**我的知识库**界面，点击右上角的**创建知识库**，在弹出的对话框中填写相关信息，包括数据类型（如文本、表格）、知识库名称、描述、Embedding 模型和知识标签，最后点击“确定”完成创建。

<img src={require('../../../../../static/img/knowledge/create-knowledgebase.png').default} alt="创建知识库" style={{width: '600px', height: 'auto'}} />

## 添加内容

### 上传文件

在知识库列表中，点击想要操作的知识库，进入知识库详情页后，点击右上角的**添加内容**按钮，上传本地文件以添加内容。

<img src={require('../../../../../static/img/knowledge/add-content.png').default} alt="添加内容" style={{width: '600px', height: 'auto'}} />

在文件上传界面上传资料，目前支持的文件格式包括 TXT、PDF、DOC 和 DOCX。每次最多可同时上传 10 个文件，累计上传数量不超过 300 个，每个文件大小限制为 20MB，不允许上传同名文件。

<img src={require('../../../../../static/img/knowledge/add-content-1.png').default} alt="添加内容" style={{width: '600px', height: 'auto'}} />

### 内容分段

接下来可以对文本内容进行分段，在分段设置页面，我们可以选择按照默认值自动分段，也可以进行自定义分段。


<img src={require('../../../../../static/img/knowledge/add-content-4.png').default} alt="分段" style={{width: '600px', height: 'auto'}} />

- 分段标识符：分段标识符是指用于将长文本或复杂数据分割为较小部分的标识，以便每个段落、句子或数据块能生成独立的嵌入向量，目前支持以下标识符：
  - 换行
  - 中文句号
  - 中文叹号
  - 中文问号
  - 英文句号
  - 英文叹号
  - 英文问号

- 分段最大长度：支持范围为[100,800]。

- 文本预处理规则：在生成 embedding 之前，文本预处理是关键步骤，以确保输入的文本适合用于生成高质量的向量表示。目前支持以下规则：
  - 替换掉连续的空格、换行符和制表符
  - 删除所有 URL 和电子邮箱地址

分段完成后，您可以在知识库页面查看已分段的内容。

<img src={require('../../../../../static/img/knowledge/add-content-3.png').default} alt="添加内容" style={{width: '800px', height: 'auto'}} />

如果需要重新分段，可以在知识库页面点击右上角的设置图标，进入重新分段页面。

