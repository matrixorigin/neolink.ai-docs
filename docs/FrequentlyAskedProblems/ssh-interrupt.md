---
sidebar_position: 4
title: SSH Connection Interruption Issues
sidebar_label: SSH Connection Interruption Issues
---

In Neolink.AI, the server's default timeout for SSH connections is set to 30 minutes. If you experience frequent disconnections during this period, it may be due to an unstable network connection. To reduce interruptions, it is recommended to switch to a more stable network environment. Additionally, you can use JupyterLab for connections, which provides a more persistent working environment. Even if network issues occur, it helps avoid disruptions to your operations.

Click the **JupyterLab** button on the right side of the instance list to access the JupyterLab interface.

<img src={require('../../static/img/qa/ssh-interrupt-1.png').default} alt="" style={{width: '600px', height: 'auto'}} />

Then, click the terminal icon to directly access the instance's terminal interface. JupyterLab does not terminate processes by default when you close terminal or notebook tabs.

<img src={require('../../static/img/qa/ssh-interrupt-2.png').default} alt="" style={{width: '600px', height: 'auto'}} />

<img src={require('../../static/img/qa/ssh-interrupt-3.png').default} alt="" style={{width: '600px', height: 'auto'}} />

For more details on using JupyterLab, refer to the [JupyterLab Connection Guide](../Built-in_tools/jupyterlab.md).
