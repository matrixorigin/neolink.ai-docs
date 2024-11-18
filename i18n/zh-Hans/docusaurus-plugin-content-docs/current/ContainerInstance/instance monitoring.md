---
sidebar_position: 5
title: 实例详情
sidebar_label: 实例详情
---

在算力实例界面，点击您想了解的实例即可进入实例详情界面，除了对信息的查看，您还能对实例进行一些操作。

<img src={require('../../../../../static/img/monitoring/monitoring-1.png').default} alt="详情" style={{width: '1000px', height: 'auto'}} />

### 基本信息

在实例的详细信息页面，您可以对实例的基础信息进行编辑，这包括重命名实例、修改描述以及更新 SSH 的连接密码。需要注意的是，修改 SSH 连接密码的操作需要在实例处于关机状态时才能执行。

### 存储

在存储信息页面，您可以查看当前存储资源的详细信息，包括存储类型、容量大小以及存储路径等。此外，您还可以直接在这个页面上进行存储资源的增加的操作。您可以选择挂载七天内已删除实例的数据盘。

<img src={require('../../../../../static/img/monitoring/monitoring-2.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />

### 路由配置

在路由配置页面，您可以对实例增加自定义外部服务配置，允许将容器内服务对外暴露。

<img src={require('../../../../../static/img/monitoring/monitoring-8.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../../../../static/img/monitoring/monitoring-9.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />

### 监控

点击算力实例，在实例监控页面，您可以查看当前实例的各项指标信息，包括数据盘使用率、GPU 和 CPU 利用率、GPU 显存占用情况、内存使用情况、功耗以及温度等参数。

<img src={require('../../../../../static/img/monitoring/monitoring-7.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />

<img src={require('../../../../../static/img/monitoring/monitoring-6.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />

### 快照

在该实例的快照界面，你可以查看快照的状态、保存失败原因等信息。
<img src={require('../../../../../static/img/monitoring/monitoring-10.png').default} alt="存储" style={{width: '1000px', height: 'auto'}} />

### 日志

在该实例的详情界面中，选择**日志**。进入容器实例日志页面，可查看当前容器实例的日志信息，主要会在实例启动时打印 cuda 信息和 jupyter 启动的日志信息。此外，启动完成后，您还可以查看 Jupyter 操作的相关日志信息。

<img src={require('../../../../../static/img/monitoring/monitoring-3.png').default} alt="日志" style={{width: '1000px', height: 'auto'}} />

### 事件

在事件信息页面，我们可以查看前容器实例的事件信息及其事件发生的时间。

<img src={require('../../../../../static/img/monitoring/monitoring-4.png').default} alt="事件" style={{width: '1000px', height: 'auto'}} />

### 进程

在**进程**信息页面。我们可以查看当前容器的进程信息，包括 CPU、物理内存、虚拟内存等。

<img src={require('../../../../../static/img/monitoring/monitoring-5.png').default} alt="进程" style={{width: '1000px', height: 'auto'}} />
