---
sidebar_position: 2
title: 数据传输
sidebar_label: 数据传输
---

您可以在本地和算力实例之间进行数据上下传，有以下方式：

1.[Matrix存储管理](createstorage)

2.scp命令

3.可视化工具如 [FileZilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_(en)) 或者 [XShell](https://www.xshellcn.com/zhishi/xshell-cswjjc.html)。

## 使用存储管理上传
参考[存储管理](createstorage)小节。

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