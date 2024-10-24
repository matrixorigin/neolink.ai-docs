---
sidebar_position: 2
title: dependent installaion
sidebar_label: dependent installaion
---

### Install Other Versions of Python

```bash
# For example, create a virtual environment named `my-env` with Python version 3.7
conda create -n my-env python=3.7

# Update the environment variables in bashrc
conda init bash && source /root/.bashrc

# Switch to the created virtual environment: my-env
conda activate my-env
```

### Install Other Frameworks

```bash
# PyTorch: Find the appropriate version from https://pytorch.org/get-started/previous-versions/Find the Appropriate Version. For example:
conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=11.3 -c pytorch -c conda-forge

# TensorFlow: Find the corresponding version link from https://www.tensorflow.org/install/pip Find the Corresponding Version Link. For example:
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.6.0-cp38-cp38-manylinux2010_x86_64.whl

```

### Python Dependency Installation

```bash
# Using pip, for example
pip install opencv-python scipy numpy Pillow

# Using conda, for example
conda install numpy

# If you are unsure about the package name, use search to find it
pip search xxxx
conda search xxxx

If you don't know the available versions of a dependency when using pip, the following trick can help: specify a random version number, and pip will return all available versions with an error message.
$ pip install xxx=9.9
```

### System Dependency Installation

```bash
# Installing `zip` as an example
apt-get update    # Only needs to be run once, no need to run it every time
apt-get install -y zip

# If you are unsure about the package name
apt-get update    # Only needs to be run once, no need to run it every time
apt-cache search xxxxx
```
