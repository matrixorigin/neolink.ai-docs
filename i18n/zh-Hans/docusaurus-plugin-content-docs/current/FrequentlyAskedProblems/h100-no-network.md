---
sidebar_position: 3
title: H100 实例如何离线安装软件
sidebar_label: H100 实例如何离线安装软件
---


针对 GPU 型号为 H100 的实例无法联网问题，我们为此类实例提供了专门的官方镜像（镜像名称后缀为 **-h100**），您只需要在创建实例的时候选择此类镜像，apt 和 pip 将在进行软件包/依赖的安装时指向本地源，实现离线环境下的软件部署。目前本地源包含的软件包列表与清华源一致。

<img src={require('../../../../../static/img/getstarted/getstarted-create-instance-1.png').default} alt="租用实例" style={{width: '900px', height: 'auto'}} />