---
sidebar_position: 1
title: overview
sidebar_label: overview
---

### Directories in Compute Instances

When using server instances, different storage disks have varying purposes and characteristics. Understanding the usage and performance of these disks can help allocate resources efficiently and improve productivity. Below is a detailed explanation of the different storage disks and how to use them.

To check disk usage within the instance, execute the following command in the terminal:  
`source /root/.bashrc`

| Name         | Path                                                                             | Size               | Performance | Type                           | Description                                                                                                                                                                                                                                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------- | ------------------ | ----------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System Disk  | Root directory `/` and all paths under it (excluding special paths listed below) | 30GB               | High        | High-performance local storage | Data will not be lost when the instance is shut down. System dependencies and Python packages are typically installed on the system disk, and small-capacity data, such as code, can also be stored here. You can choose to save the existing environment and data as an image when the instance is shut down, allowing the data to be restored on the next startup. |
| Data Disk    | Customizable, recommended to set as `/root/data`                                 | Starting from 50GB | Standard    | Shared storage                 | Can be mounted across different compute instances.                                                                                                                                                                                                                                                                                                                   |
| File Storage | User-defined mount paths in **Storage Management**                               | Custom             | Standard    | Shared storage                 | Can be mounted across different compute instances. **(Not yet available)**                                                                                                                                                                                                                                                                                           |
