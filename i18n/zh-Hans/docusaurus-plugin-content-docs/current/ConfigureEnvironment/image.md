---
sidebar_position: 3
title: 镜像
sidebar_label: 镜像
---

## 官方镜像

Neolink.AI 提供了多种官方镜像，在侧边栏中选择**镜像管理**，可以看到一系列的官方镜像，选择适合的官方镜像后，点击**部署**。

<img src={require('../../../../../static/img/imgmanagement/imagemanagement-1.png').default} alt="上传数据" style={{width: '700px', height: 'auto'}} />

跳转到已选择官方镜像的创建实例界面。

<img src={require('../../../../../static/img/imgmanagement/imagemanagement-2.png').default} alt="上传数据" style={{width: '700px', height: 'auto'}} />

## 私有镜像

如果您已经设置好了一个实例的环境，并且希望在更换服务器或创建新实例时能够重新使用这个环境，或者想要为了将来的需要而持续维护这个环境，那么使用私有镜像是一个很好的选择。平台默认赠送 30Gi 私有镜像存储，当私有镜像总量超出 30Gi 后，超出部分将按照0.01元/日/Gi 进行扣费。

### 保存镜像

在算力实例列表详情右侧选择保存镜像，可见实例环境为私有镜像，将完整保存系统盘的所有文件，数据盘等不会被保存在其中。

__NOTE__：只有在运行中的实例才可以保存镜像。

<img src={require('../../../../../static/img/imgmanagement/imagemanagement-3.png').default} alt="保存镜像" style={{width: '800px', height: 'auto'}} />

在保存镜像的弹窗中您可以自定义镜像的名称和版本。镜像保存后可前往**镜像管理 > 私有镜像**处查看镜像信息。

<img src={require('../../../../../static/img/imgmanagement/imagemanagement-4.png').default} alt="保存镜像" style={{width: '800px', height: 'auto'}} />

### 镜像管理

在 **镜像管理 > 私有镜像**页面，可以看到我们保存的私有镜像，在这里我们可以点击**部署**按钮跳转到实例创建页面为实例选择私有镜像进行部署，也可以删除私有镜像。

__NOTE:__ 删除镜像会导致依赖此镜像的实例无法正常运行，请务必谨慎操作。

<img src={require('../../../../../static/img/imgmanagement/imagemanagement-5.png').default} alt="镜像管理" style={{width: '800px', height: 'auto'}} />
