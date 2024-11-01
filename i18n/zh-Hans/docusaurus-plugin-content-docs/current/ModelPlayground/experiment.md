---
sidebar_position: 6
title: 体验中心
sidebar_label: 体验中心
---

体验中心是一个在线交互平台，用户可以直接输入数据并观察模型输出，无需编程，适用于快速测试和了解模型性能。

## 操作步骤

1.进入左侧侧边栏中的**体验中心**；在**体验中心**页面，可以看到体验中心上线的模型，可以通过**模型**进行筛选。
<img src={require('../../../../../static/img/experience/1.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />

2.在**提示词**部分，输入系统提示词，例如“你好，我是你的专属 AI 客服”，以便调整模型的输出。
<img src={require('../../../../../static/img/experience/2.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />

3.最后，通过调整参数 Temperature、Top P 和 Max_tokens 来控制模型的输出。

• Temperature 用于调节生成文本的随机性和创造性，值越大随机性越强，取值范围为 0-1。

• Top P 控制输出 tokens 的多样性，值越大，输出的 tokens 类型越丰富，取值范围同样为 0-1。

• Max_tokens 则限制输出文本的最大 tokens 数量，默认值为 200，最大值为 4096。

<img src={require('../../../../../static/img/experience/3.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />
