---
sidebar_position: 1
title: Jupyterlab
sidebar_label: Jupyterlab
---

## 什么是 JupyterLab？

JupyterLab 是一个灵活的用户界面，专为创建和共享计算文档而设计，尤其适用于数据科学、机器学习、科学计算和教育等领域。作为 Jupyter Notebook的下一代界面，JupyterLab 提供了更加丰富和可扩展的功能。

它集成了多种工具，如代码编辑器、终端、文本编辑器、文件浏览器和笔记本，用户可以在一个界面中方便地切换不同的工具，无需在多个窗口之间来回切换。此外，JupyterLab 支持多种编程语言，包括 Python、R、Julia 和 Scala，用户能够在同一环境中进行跨语言的开发和实验，无需安装多个不同的开发环境。

Neolink 的所有镜像目前均集成了 JupyterLab 这一内置工具，无论是开展复杂的数据分析，进行机器学习模型训练，亦或是执行日常的编程任务，用户都可以借助这一工具有效提升工作效率。
  
## 应用场景

- 数据科学和分析：数据科学家可以使用 JupyterLab 进行数据清洗、分析和建模，方便地处理和可视化数据。
机器学习和深度学习：

- 提供对机器学习库（如 Scikit-learn、TensorFlow、PyTorch 等）的支持，方便构建、训练和评估模型。

- 教育和培训：适用于教学，教师可以创建交互式讲义，学生可以实时实验和学习。

- 科学研究：研究人员可以使用 JupyterLab 记录实验过程、分析结果，并生成可重复的研究文档。

- 快速原型开发：开发人员可以利用 JupyterLab 快速原型化应用程序，测试和迭代想法。

## 操作步骤

进入左侧侧边栏中的**算力实例**，在具体的实例的内置工具下，点击**Jupyterlab**，即可进入 JupyterLab 界面。
<img src={require('../../../../../static/img/qa/ssh-interrupt-1.png').default} alt="" style={{width: '600px', height: 'auto'}} />

<img src={require('../../../../../static/img/jupyterlab/jupyterlab-2.png').default} alt="JupyterLab界面" style={{width: '600px', height: 'auto'}} />

## 基本功能

JupyterLab 界面主要包括两大部分，即文件浏览区和工作区。

<img src={require('../../../../../static/img/jupyterlab/jupyterlab-3.png').default} alt="JupyterLab界面" style={{width: '500px', height: 'auto'}} />

在文件浏览区，双击文件夹名称，进入文件目录。点击文件上传标识，选择待上传的文件。

<img src={require('../../../../../static/img/jupyterlab/jupyterlab-4.png').default} alt="JupyterLab界面" style={{width: '200px', height: 'auto'}} />

在文件浏览区，右键点击指定文件夹或文件，即可进行文件管理。

<img src={require('../../../../../static/img/jupyterlab/jupyterlab-5.png').default} alt="JupyterLab界面" style={{width: '300px', height: 'auto'}} />

在工作区域，点击 Other > Terminal 即可新打开一个终端。JupyterLab 在关闭终端或 Notebook 选项卡后，默认不会终止运行。

<img src={require('../../../../../static/img/jupyterlab/jupyterlab-6.png').default} alt="JupyterLab界面" style={{width: '500px', height: 'auto'}} />

