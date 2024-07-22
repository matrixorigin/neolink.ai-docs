---
sidebar_position: 4
title: 数据传输
sidebar_label: 数据传输
---

您可以在本地和算力实例之间进行数据上下传，有以下方式：

1.[JupyterLab](../ContainerInstance/jupterlab)：目前 JupyterLab 暂不支持批量文件或文件夹的上传/下载。

2.[Matrix存储管理](createstorage)：支持上传文件。不支持上传文件夹，不支持下载文件、文件夹。

3.scp命令：支持使用命令行上传下载文件和文件夹。

4.可视化工具如 [FileZilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_(en)) 或者 [XShell](https://www.xshellcn.com/zhishi/xshell-cswjjc.html)：使用外部软件，拖拉拽即可完成上传下载。

## 使用JupyterLab上下传

### 上传

按照如图所示操作上传文件。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-4.png').default} alt="JupyterLab界面" style={{width: '300px', height: 'auto'}} />

### 下载

按照如图所示操作下载文件,选中文件，然后鼠标右键。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-5.png').default} alt="JupyterLab界面" style={{width: '500px', height: 'auto'}} />
注意JupyterLab不能下载文件夹,可以使用命令行工具将文件夹压缩成一个压缩文件。这里是一个常用的压缩命令示例，假设你要将文件夹my_folder压缩成my_folder.zip：
```bash
zip -r my_folder.zip my_folder
```


## 使用存储管理上传
在[存储管理](createstorage)小节，说明了如何通过存储管理功能上传文件。

## scp命令上下传
此方法支持文件与文件夹的上下传。

复制您的 SSH 登录指令，如：ssh -p 40567 user@111.51.90.14。在您的本地机器上执行以下命令，其中40567是实例端口号，111.51.90.14是实例ip，您需要**根据您的实例**进行更改：

### 上传

在本地机器上执行以下命令：

```bash
scp -rP 40567 [本地待上传文件夹] user@111.51.90.14:[云主机目标文件夹]
```

### 下载

在本地机器上执行以下命令：

```bash
scp -rP 40567 user@111.51.90.14:[云主机待上传文件夹] [本地目标文件夹]
```

## 可视化工具上下传
您也可以使用可视化工具如 [FileZilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_(en)) 或者 [XShell](https://www.xshellcn.com/zhishi/xshell-cswjjc.html)。