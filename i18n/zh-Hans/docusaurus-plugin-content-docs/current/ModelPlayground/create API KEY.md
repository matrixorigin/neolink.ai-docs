---
sidebar_position: 3
title: 创建API KEY
sidebar_label: 创建API KEY
---
API Key支持访问模型广场所有的模型，APIKey
长期有效，请您不要将密钥信息共享至公开环境，妥善保管。获取APIKey 方式如下：

1.进入左侧侧边栏中的**API 管理**，点击**API KEY**
<img src={require('../../../../../static/img/apikey/apikey1.png').default} alt="模型广场" style={{width: '1000px', height: 'auto'}} />
2.点击**创建API KEY**。
<img src={require('../../../../../static/img/getstarted/modelservice4.png').default} alt="模型广场" style={{width: '1000px', height: 'auto'}} />
3.在**模型广场**中,选择想要调用的模型，复制模型id。在API请求头中的"model"字段中填写模型ID，以便调用相应的模型。更详细的信息可参考[API文档](../category/apidocs)。
