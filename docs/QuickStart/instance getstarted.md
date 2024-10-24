---
sidebar_position: 1
title: Using Compute Instances
sidebar_label: Using Compute Instances
---

## Create an Instance

Go to the Overview page, navigate to **My Compute Instances** in the sidebar, and click **Create Instance**.  
<img src={require('../../static/img/getstarted/getstarted-1.png').default} alt="Create Instance" style={{width: '600px', height: 'auto'}} />

## Renting an Instance

On the **Create Instance** page, select the **Region**, **Billing Method** (pay-as-you-go, daily, weekly, or monthly), **GPU Model**, **Quantity**, and **Specification**. Choose the **Image** (pre-installed with different deep learning frameworks), and then click **Create**. If you need more disk space to store data, set the desired expansion size.

<img src={require('../../static/img/getstarted/getstarted-create-instance3.png').default} alt="Rent Instance" style={{width: '1000px', height: 'auto'}} />

After the instance is created, wait for it to start. The primary operation entry points are shown below.

![Quick Start - Rent Instance - Diagram](../../static/img/getstarted/getstarted-create-instance4.png)

## Uploading Data

Go to the Overview page. After the instance is running, find the **JupyterLab** shortcut tool on the instance and open it. In the screenshot below, locate the **Upload** button to upload your data.  
<img src={require('../../static/img/jupyterlab/jupyterlab-4.png').default} alt="Upload Data" style={{width: '250px', height: 'auto'}} />

If you need to upload folders or use more advanced upload methods, go to **Storage Management** in the sidebar, click **Upload Files**, and select the code or data you want to upload. It is recommended to place the data disk in the `/root/data` path of the instance.  
<img src={require('../../static/img/getstarted/getstarted-data1.png').default} alt="Upload Data" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../static/img/getstarted/getstarted-data2.png').default} alt="Upload Data" style={{width: '400px', height: 'auto'}} />

## Terminal Training

Go to **Compute Instances** in the sidebar, click on a specific instance to access the instance details page, and click **Terminal** to enter the terminal interface. You can execute your code here to complete the training.  
<img src={require('../../static/img/getstarted/getstarted-terminal1.png').default} alt="Terminal Interface" style={{width: '600px', height: 'auto'}} />
<img src={require('../../static/img/getstarted/getstarted-terminal2.png').default} alt="Terminal Interface" style={{width: '1000px', height: 'auto'}} />

You can also use [JupyterLab](../Built-in_tools/jupyterlab.md) or [SSH Connection](../ContainerInstance/ssh.md) to complete code training.
