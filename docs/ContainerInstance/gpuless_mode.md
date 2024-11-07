---
sidebar_position: 6
title: No-GPU Mode
sidebar_label: No-GPU Mode
---

For tasks such as writing and debugging code, uploading or downloading data to the instance, or presenting code that do not require GPU usage, you can choose to start the instance in No-GPU Mode. In No-GPU Mode, the instance will use a 2-core CPU and 4GB of memory without a GPU. The cost for this mode is ¥0.1/hour. Switching to No-GPU Mode will not affect your instance data before or after use, and you can still switch back to normal mode from the instance list for regular operations such as powering on and off.

## Starting in No-GPU Mode

When creating an instance, select **No-GPU Mode** to start the instance with No-GPU specifications. No-GPU Mode is only available with pay-as-you-go billing.

<img src={require('../../static/en-img/gpuless/gpuless-1.png').default} alt="Start in No-GPU Mode" style={{width: '700px', height: 'auto'}} />

You will see that the newly created instance is labeled with the **No-GPU Mode** indicator.

<img src={require('../../static/en-img/gpuless/gpuless-2.png').default} alt="No-GPU Instance" style={{width: '700px', height: 'auto'}} />

## Powering On in No-GPU Mode

In the instance list, after an instance is powered off, you can select **Power On in No-GPU Mode**.

<img src={require('../../static/en-img/gpuless/gpuless-3.png').default} alt="Power On in No-GPU Mode" style={{width: '700px', height: 'auto'}} />
