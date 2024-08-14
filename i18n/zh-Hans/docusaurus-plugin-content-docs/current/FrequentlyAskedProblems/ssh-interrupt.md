---
sidebar_position: 4
title: ssh 连接中断问题
sidebar_label: ssh 连接中断问题
---
在 Neolink.AI 中，服务端默认将 SSH 连接的超时时间设置为半小时。如果您在此期间频繁断开连接，可能是由于网络不稳定导致的。为减少中断，建议切换到更稳定的网络环境。此外，您还可以使用 Jupyterlab 进行连接，这可以提供更持久的工作环境，即使网络出现问题，也能避免操作被中断。

点击实例列表右侧的 **Jupyterlab**  按钮即可进入到 Jupyterlab 操作界面。

<img src={require('../../../../../static/img/qa/ssh-interrupt-1.png').default} alt="" style={{width: '600px', height: 'auto'}} />

随后点击终端图标即可直接进入到实例终端界面。Jupyterlab 在关闭终端或 Notebook 选项卡后，默认不会终止运行。

<img src={require('../../../../../static/img/qa/ssh-interrupt-2.png').default} alt="" style={{width: '600px', height: 'auto'}} />

<img src={require('../../../../../static/img/qa/ssh-interrupt-3.png').default} alt="" style={{width: '600px', height: 'auto'}} />

有关 Jupyterlab 的更多使用说明，可查看[JupyterLab连接说明](../ContainerInstance/jupterlab.md)