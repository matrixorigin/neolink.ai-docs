---
sidebar_position: 5
title: Instance Details
sidebar_label: Instance Details
---

In the GPU Instances page, click the instance you want to explore to access the instance details. In addition to viewing information, you can perform various operations on the instance.

<img src={require('../../static/en-img/monitoring/monitoring-1.png').default} alt="Details" style={{width: '1000px', height: 'auto'}} />

### Basic Information

On the instance details page, you can edit basic instance information, such as renaming the instance, modifying the description, and updating the SSH connection password. Note that updating the SSH connection password requires the instance to be powered off.

### Storage

In the storage information section, you can view detailed information about the current storage resources, including the storage type, capacity, and storage path. Additionally, you can increase storage resources directly from this page. You also have the option to mount data disks from instances that were deleted within the past seven days.

<img src={require('../../static/en-img/monitoring/monitoring-2.png').default} alt="Storage" style={{width: '1000px', height: 'auto'}} />

### Configure-Route

On the Configure-Route page, you can add custom external service configurations to expose services running inside the container to external networks.

<img src={require('../../static/en-img/monitoring/monitoring-8.png').default} alt="Routing Configuration" style={{width: '1000px', height: 'auto'}} />
<img src={require('../../static/en-img/monitoring/monitoring-9.png').default} alt="Routing Configuration" style={{width: '1000px', height: 'auto'}} />

### Monitor

By selecting the compute instance, you can access the monitor page to view various metrics, including data disk usage, GPU and CPU utilization, GPU memory usage, memory consumption, power consumption, and temperature.

<img src={require('../../static/en-img/monitoring/monitoring-7.png').default} alt="Monitoring" style={{width: '1000px', height: 'auto'}} />

<img src={require('../../static/en-img/monitoring/monitoring-6.png').default} alt="Monitoring" style={{width: '1000px', height: 'auto'}} />

### Logs

In the instance details page, select **Logs** to access the container instance logs. Here, you can view logs related to the current container instance, including CUDA logs and Jupyter startup logs during initialization. After the instance is running, you can also access logs related to Jupyter operations.

<img src={require('../../static/en-img/monitoring/monitoring-3.png').default} alt="Logs" style={{width: '1000px', height: 'auto'}} />

### Event

In the Event section, you can view the events related to the container instance along with their timestamps.

<img src={require('../../static/en-img/monitoring/monitoring-4.png').default} alt="Events" style={{width: '1000px', height: 'auto'}} />

### Process

In the **Process** section, you can view information about the current container’s processes, including CPU usage, physical memory, and virtual memory.

<img src={require('../../static/en-img/monitoring/monitoring-5.png').default} alt="Processes" style={{width: '1000px', height: 'auto'}} />
