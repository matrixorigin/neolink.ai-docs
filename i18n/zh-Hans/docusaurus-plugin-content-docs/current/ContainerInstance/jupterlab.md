---
sidebar_position: 3
title: JupyterLab
sidebar_label: JupyterLab
---
### 操作步骤

1.进入左侧侧边栏中的**算力实例**，在具体的实例的内置工具下，点击Jupyterlab，首先进入JupyterLab 启动时的登录界面。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-1.png').default} alt="JupyterLab登录" style={{width: '600px', height: 'auto'}} />

2.按照登录界面介绍，利用[ssh](ssh)连接算力实例，在终端输入命令：
```bash
jupyter server list
```
3.得到以下输出，复制'token='后的内容 <mark>c8de56fa... </mark> 作为密码粘贴到登录页面的密码字段中。注意:复制URL进入浏览器无法顺利进入JupyterLab，需要采取上文的输入token的方法。
```bash
http://localhost:8888/?token=c8de56fa... :: /Users/you/notebooks
```

4.进入JupyterLab界面。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-2.png').default} alt="JupyterLab界面" style={{width: '1000px', height: 'auto'}} />

### 基本功能介绍

JupyterLab 界面主要包括两大部分，即文件浏览区和工作区。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-3.png').default} alt="JupyterLab界面" style={{width: '1000px', height: 'auto'}} />
在文件浏览区，双击文件夹名称，进入文件目录。点击文件上传标识，选择待上传的文件。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-4.png').default} alt="JupyterLab界面" style={{width: '300px', height: 'auto'}} />
在文件浏览区，右键点击指定文件夹或文件，即可进行文件管理。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-5.png').default} alt="JupyterLab界面" style={{width: '500px', height: 'auto'}} />
在工作区域，点击 Other > Terminal 即可新打开一个终端。JupyterLab 在关闭终端或 Notebook 选项卡后，默认不会终止运行。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-6.png').default} alt="JupyterLab界面" style={{width: '700px', height: 'auto'}} />