---
sidebar_position: 2
title: 依赖安装
sidebar_label: 依赖安装
---

### 安装其他版本Python
```bash
# 比如构建一个虚拟环境名为：my-env，Python版本为3.7
conda create -n my-env python=3.7    

# 更新bashrc中的环境变量
conda init bash && source /root/.bashrc

# 切换到创建的虚拟环境：my-env
conda activate my-env
```

### 安装其他框架
```bash
# PyTorch：从https://pytorch.org/get-started/previous-versions/找到合适的版本。比如：
conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=11.3 -c pytorch -c conda-forge

# TensorFlow: 从https://www.tensorflow.org/install/pip找到对应版本链接。比如：
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.6.0-cp38-cp38-manylinux2010_x86_64.whl

```

### Python依赖安装
```bash
# 使用pip，举例
pip install opencv-python scipy numpy Pillow

# 使用conda，举例
conda install numpy

# 如果不确定包名，通过搜索来查找
pip search xxxx
conda search xxxx

如果在用pip时不知道某个依赖有什么版本号，那么以下trick可以查看：随便写一个版本号，pip会报错出所有可安装的版本号
$ pip install xxx=9.9
```

### 系统依赖安装
```bash
# 以安装zip为例
apt-get update    # 只需要执行一次，不用每次都执行
apt-get install -y zip

# 如果不知道包名
apt-get update    # 只需要执行一次，不用每次都执行
apt-cache search xxxxx
```