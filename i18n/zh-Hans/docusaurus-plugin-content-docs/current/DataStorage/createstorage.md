---
sidebar_position: 3
title: 存储管理
sidebar_label: 存储管理
---
存储管理为网络共享存储，可挂载至不同实例中。用于实例间的数据共享。实例间共享，可以多点读写，不受实例释放的影响；此外存储后端有多冗余副本，数据可靠性非常高（本地数据盘无冗余备份，有一定概率出现磁盘故障影响数据）

## 添加存储

进入**算力实例**页面，点击具体的实例，在**存储**中可添加存储，并设置该存储在实例中的具体路径，确定后即可在实例中用该挂载路径访问该存储中的文件。

## 上传文件

在左侧侧边栏，选择**存储管理**，默认进入存储管理页面。点击**上传文件**，选择所需的代码或数据上传。数据盘建议放在实例下的/root/data路径。

<img src={require('../../../../../static/img/getstarted/getstarted-data1.png').default} alt="上传数据" style={{width: '1000px', height: 'auto'}} />

### 普通上传

对于小于 200 MiB 的文件，可以通过拖拽或点击上传的方式进行操作，每次仅可上传1个文件。

<img src={require('../../../../../static/img/getstarted/getstarted-data2.png').default} alt="普通上传" style={{width: '400px', height: 'auto'}} />

### 超大文件上传

对于超过 200 MiB 的文件，我们提供了大文件上传的解决方案。

<img src={require('../../../../../static/img/datastorage/data-2.png').default} alt="超大文件上传" style={{width: '400px', height: 'auto'}} />

1. 安装 MinIO Client(mc)

    MinIO Client (mc) 是一个命令行工具，用于与 MinIO 及其他兼容 S3 的存储服务进行交互操作。当前支持以下版本的功能使用：

    | 系统架构         | 二进制文件                       |
    |----------------|--------------------------------|
    |  mac-amd64     | https://dl.min.io/client/mc/release/darwin-amd64/archive/mc.RELEASE.2021-04-22T17-40-00Z|
    |  mac-arm64     | https://dl.min.io/client/mc/release/darwin-arm64/archive/mc.RELEASE.2021-04-22T17-40-00Z |
    |  windows-amd64 | https://dl.min.io/client/mc/release/windows-amd64/archive/mc.RELEASE.2021-04-22T17-40-00Z  |
    |  linux-arm64   | https://dl.min.io/client/mc/release/linux-arm64/archive/mc.RELEASE.2021-04-22T17-40-00Z|
    |  linux-amd64   | https://dl.min.io/client/mc/release/linux-amd64/archive/mc.RELEASE.2021-04-22T17-40-00Z |

    以下给出部分架构安装步骤，更详细的安装方式可参考官方文档：https://min.io/docs/minio/linux/index.html

    - mac-arm64

    ```bash
    curl -O https://dl.min.io/client/mc/release/darwin-arm64/archive/mc.RELEASE.2021-04-22T17-40-00Z
    chmod +x mc.RELEASE.2021-04-22T17-40-00Z
    sudo mv mc.RELEASE.2021-04-22T17-40-00Z /usr/local/bin/mc
    mc -version
    ```

    - windows-amd64
      - 点击下载二进制文件 。
      - 将下载好的二进制文件名称改为`mc.exe`。
      - 进入到 mc.exe 目录执行相应操作，注意，示例中的 `mc` 命令在 windows下 需替换成 `mc.exe`。
    
    - linux-arm64

    ```bash
    wget https://dl.min.io/client/mc/release/linux-arm64/archive/mc.RELEASE.2021-04-22T17-40-00Z
    chmod +x mc.RELEASE.2021-04-22T17-40-00Z
    sudo mv mc.RELEASE.2021-04-22T17-40-00Z /usr/local/bin/mc
    mc -version
    ```

2. 添加 alias

    ```bash
    mc config host add <桶名> <URL> <Access key> <Secret access key>
    ```

    示例：

    ```bash
    mc config host add bucket-xx https://file.gw.neolink-ai.com bucket-xx sCKPcR5HNve86pqUC7k133LD25BgSE2dAZ5zxxxx
    ```

    <img src={require('../../../../../static/img/datastorage/data-1.png').default} alt="超大文件上传" style={{width: '500px', height: 'auto'}} />

3. 上传

   - 单个文件上传

   ```bash
   mc cp <需要上传的文件路径> <桶名>/<命名空间>
   ```

   示例：

   ```bash
   mc cp <需要上传的文件路径> bucket-xx/pvc-35e6fa13-802a-4e93-8e55-05b13724xxxx
   ```

    <img src={require('../../../../../static/img/datastorage/data-3.png').default} alt="超大文件上传" style={{width: '700px', height: 'auto'}} />

    __NOTE__:上传速度快慢跟本地网络有关系。

   - 目录上传
  
    ```bash
    mc cp --recursive <需要上传的目录路径> <桶名>/<命名空间>
    ```

    示例：

    ```bash
    mc cp --recursive <需要上传的目录路径> bucket-xx/pvc-35e6fa13-802a-4e93-8e55-05b13724xxxx
    ```

4. 下载
   
   - 单个文件下载

   ```bash
   mc <桶名>/<命名空间>/<存储文件路径> <本地路径>
   ```

   示例：

   ```bash
   mc bucket-xx/pvc-35e6fa13-802a-4e93-8e55-05b13724xxxx/<存储文件路径> <本地路径>
   ```

   - 目录
     
   ```bash
   mc cp --recursive <桶名>/<命名空间>/<存储目录路径> <本地路径>
   ```

    示例：

    ```bash
    mc --recursive bucket-xx/pvc-35e6fa13-802a-4e93-8e55-05b13724xxxx/<存储目录路径> <本地路径>
    ```



