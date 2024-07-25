---
sidebar_position: 3
title: TensorBoard
sidebar_label: TensorBoard
---
TensorBoard 用于可视化模型的训练过程、模型结构、数据分布等信息，帮助用户更好地理解和调试他们的模型。更详细的信息可以参考[最佳实践-进行TensorFlow模型训练](../BestPractices/tensorflow)

### 操作步骤

进入左侧侧边栏中的**算力实例**，在具体的实例的内置工具下，点击Tensorboard，进入Tensorboard界面即可查看。
<img src={require('../../../../../static/img/tensorboard/tensorboard-1.png').default} alt="tensorboard" style={{width: '1000px', height: 'auto'}} />

### 注意事项

您需要编写代码将日志写入环境变量**TENSORBOARD_LOG_PATH**所对应的路径，TensorBoard 将自行获取相应目录的数据。