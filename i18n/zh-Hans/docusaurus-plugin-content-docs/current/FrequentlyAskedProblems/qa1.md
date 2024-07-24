---
sidebar_position: 1
title: 如何登录JputerLab界面
sidebar_label: 如何登录JputerLab界面
---


1.进入左侧侧边栏中的**算力实例**，在具体的实例的内置工具下，点击Jupyterlab，首先进入JupyterLab 启动时的登录界面。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-1.png').default} alt="JupyterLab登录" style={{width: '600px', height: 'auto'}} />

2.按照登录界面介绍，点击具体实例，点击终端，进入终端输入命令：
```bash
jupyter server list
```
3.得到以下输出，注意复制'token='后的内容 <mark>c8de56fa... </mark> 作为密码粘贴到登录页面的密码字段中。复制URL进入浏览器无法顺利进入JupyterLab，需要采取上文的输入token的方法。
```bash
http://localhost:8888/?token=c8de56fa... :: /Users/you/notebooks
```

4.进入JupyterLab界面。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-2.png').default} alt="JupyterLab界面" style={{width: '1000px', height: 'auto'}} />