---
sidebar_position: 4
title: 数据传输
sidebar_label: 数据传输
---

您可以在本地和算力实例之间进行数据上下传，有以下方式：

1.[JupyterLab](../Built-in_tools/jupyterlab.md)：目前 JupyterLab 暂不支持批量文件或文件夹的上传/下载。

2.[存储管理](createstorage)：支持上传文件。不支持上传文件夹，不支持下载文件、文件夹。

3.scp命令：支持使用命令行上传下载文件和文件夹。

4.可视化工具如 [FileZilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_(en)) 或者 [XShell](https://www.xshellcn.com/zhishi/xshell-cswjjc.html)：使用外部软件，拖拉拽即可完成上传下载。

## 使用JupyterLab上下传

### 上传

按照如图所示操作上传文件。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-4.png').default} alt="JupyterLab界面" style={{width: '300px', height: 'auto'}} />

### 下载

按照如图所示操作下载文件，选中文件，然后鼠标右键。
<img src={require('../../../../../static/img/jupyterlab/jupyterlab-5.png').default} alt="JupyterLab界面" style={{width: '500px', height: 'auto'}} />
注意JupyterLab不能下载文件夹,可以使用命令行工具将文件夹压缩成一个压缩文件。这里是一个常用的压缩命令示例，假设你要将文件夹my_folder压缩成my_folder.zip：
```bash
zip -r my_folder.zip my_folder
```

## 使用存储管理上传

在[存储管理](createstorage)小节，说明了如何通过存储管理功能上传文件。

## scp命令上下传

此方法支持文件与文件夹的上下传。

### 上传

上传本地文件到服务器：

```bash
#上传文件
scp -P port_number /path/to/local/file username@remote_host:/path/to/remote/directory

#上传文件夹
scp -P port_number -r /path/to/local/file username@remote_host:/path/to/remote/directory
```

**参数说明：**

- port_number：服务器端口号
- /path/to/local/file：本地文件的路径。
- username@remote_host：远程服务器的用户名和地址。
- /path/to/remote/directory：上传到远程服务器的目标目录路径。

**示例：**

```bash
#上传文件
scp -P 30626 ./file.txt root@fc4e4fbf-3c3e-4fce-a90a-e2ae5a6axxxx.gws.neolink-ai.com:/root/data

#上传文件夹
scp -P 30626 -r ./file root@fc4e4fbf-3c3e-4fce-a90a-e2ae5a6axxxx.gws.neolink-ai.com:/root/data
```

### 下载

在本地机器上执行以下命令：

```bash
#下载文件
scp  -P port_number username@remote_host:/path/to/remote/file /path/to/local/directory

#下载文件夹
scp  -P port_number -r username@remote_host:/path/to/remote/file /path/to/local/directory
```

**参数说明：**

- port_number：服务器端口号
- username@remote_host：远程服务器的用户名和地址。
- /path/to/remote/file：远程服务器上文件的路径。
- /path/to/local/directory：下载到本地的目标目录。

**示例：**

```bash
#下载文件
scp -P 30626 root@fc4e4fbf-3c3e-4fce-a90a-e2ae5a6axxxx.gws.neolink-ai.com:/root/data/file.txt ./

#下载文件夹
scp -P 30626 root@fc4e4fbf-3c3e-4fce-a90a-e2ae5a6axxxx.gws.neolink-ai.com:/root/data/file ./
```

## 可视化工具上下传
您也可以使用可视化工具如 [FileZilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_(en)) 或者 [XShell](https://www.xshellcn.com/zhishi/xshell-cswjjc.html)。