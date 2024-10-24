---
sidebar_position: 3
title: How to Install Software Offline on H100 Instances
sidebar_label: How to Install Software Offline on H100 Instances
---

To address the issue of H100 GPU instances being unable to connect to the internet, we provide specialized official images for these instances (with the **-h100** suffix). When creating an instance, simply select one of these images, and both `apt` and `pip` will be configured to use local mirrors for software and dependency installation, enabling software deployment in an offline environment. The local mirrors currently contain the same package list as the Tsinghua repository.

<img src={require('../../static/img/getstarted/getstarted-create-instance-1.png').default} alt="Rent Instance" style={{width: '900px', height: 'auto'}} />
