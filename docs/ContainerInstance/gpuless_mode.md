---
sidebar_position: 6
title: GPU-less Mode
sidebar_label: GPU-less Mode
---

For tasks such as writing and debugging code, uploading or downloading data to the instance, or presenting code that do not require GPU usage, you can choose to start the instance in GPU-less Mode. In GPU-less Mode, the instance will use a 2-core CPU and 4GB of memory without a GPU. The cost for this mode is ¥0.1/hour. Switching to GPU-less Mode will not affect your instance data before or after use, and you can still switch back to normal mode from the instance list for regular operations such as powering on and off.

<iframe width="640" height="360" 
  src={require('../../static/video/demo/gpuless_mode.mp4').default}
  frameborder="0" allowfullscreen>
</iframe>

## Starting in GPU-less Mode

When creating an instance, select **GPU-less Mode** to start the instance with GPU-less specifications. GPU-less Mode is only available with pay-as-you-go billing.

<img src={require('../../static/gpuless/gpuless-1.png').default} alt="Start in GPU-less Mode" style={{width: '700px', height: 'auto'}} />

You will see that the newly created instance is labeled with the **GPU-less Mode** indicator.

<img src={require('../../static/gpuless/gpuless-2.png').default} alt="GPU-less Instance" style={{width: '700px', height: 'auto'}} />

## Powering On in GPU-less Mode

In the instance list, after an instance is powered off, you can select **Power On in GPU-less Mode**.

<img src={require('../../static/gpuless/gpuless-3.png').default} alt="Power On in GPU-less Mode" style={{width: '700px', height: 'auto'}} />
