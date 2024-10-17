---
sidebar_position: 6
title: 无卡模式
sidebar_label: 无卡模式
---

在编写和调试代码、上传下载数据到实例、或进行代码展示等不需要使用 GPU 的场景下，可以选择无卡模式启动。无卡模式下，实例将使用 2 核 CPU、4GB 内存，并不配置 GPU。该模式的费用为￥ 0.1/小时。使用无卡模式不会影响实例之前或之后的数据，今后仍然可以在实例列表处切换回正常模式进行开关机操作。

<video controls width="640">
  <source src="https://community-shared-data-1308875761.cos.ap-beijing.myqcloud.com/artwork/neolinkdocs/video/%E6%97%A0%E5%8D%A1%E6%A8%A1%E5%BC%8F%E4%BD%BF%E7%94%A8demo.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 无卡模式启动

在实例创建时选择**无卡模式**，实例将以无卡规格启动，无卡模式仅支持按量计费。

<img src={require('../../../../../static/gpuless/gpuless-1.png').default} alt="无卡启动" style={{width: '700px', height: 'auto'}} />

可以看到，新创建的实例状态带有**无卡模式**标识。

<img src={require('../../../../../static/gpuless/gpuless-2.png').default} alt="无卡实例" style={{width: '700px', height: 'auto'}} />

## 无卡模式开机

在实例列表中，实例关机后，可以选择**无卡模式开机**。

<img src={require('../../../../../static/gpuless/gpuless-3.png').default} alt="无卡开机" style={{width: '700px', height: 'auto'}} />
