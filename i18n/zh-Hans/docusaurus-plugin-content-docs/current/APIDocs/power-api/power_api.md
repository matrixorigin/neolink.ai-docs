---
sidebar_position: 1
title: 算力API
sidebar_label: 算力API
---

## 鉴权

获取 token：打开“开发者工具”界面，在标头处找到 **Authorization**

<img src={require('../../../../../../static/img/apikey/token.png').default} alt="获取token" style={{width: '800px', height: 'auto'}} />

__NOTE__:token 有效期为24小时，24小时之后需重新获取。

## 获取 region id 和 clusterName

- region_id：地区 id
- clusterName：集群名称

### 请求

**GET** `https://neolink-ai.com/mdc/api/v1/regions`

### 响应

**python代码：**

```python
import requests
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/regions"

response = requests.get(url, headers=headers)
print(response.content.decode())
```

**返回：**

```bash
[{"id":"14c5a9e3-0d09-4aa0-99d3-c096b80cceaa","region":"北京一区","clusterName":"host-cluster","harborAddr":"images.neolink-ai.com","howlerID":"69e377a7-99d1-cca0-ef58-cfce14a336b2","createdAt":"2024-07-15T12:00:23.227+08:00","updatedAt":"2024-07-15T12:00:23.227+08:00"}]
```

## 查看 GPU 规格信息

### 请求

**GET** `https://neolink-ai.com/mdc/api/v1/skus/computings?region_id=$region_id`

### 响应

**python代码：**

```python
import requests
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/skus/computings?region_id=14c5a9e3-0d09-4aa0-99d3-c096b80cceaa"
response = requests.get(url, headers=headers)

print(response.content.decode())
```

**返回：**

```bash
[{"name":"H20","regionID":"14c5a9e3-0d09-4aa0-99d3-c096b80cceaa","cpuArch":"x86-64","cpuSeries":"Inter Xeon","cpucores":24,"memoryCount":192,"cpuVendor":"Inter","gpuSeries":"H20","gpuProduct":"H20","gpuResourceKey":"nvidia.com/gpu-h20","gpuCounts":1,"gpuMemory":96,"systemstorage":30,"datastorage":50,"skusID":"2","regionName":"北京一区","clusterName":"host-cluster","sellingType":"1","ratio":0.48,"discountID":"10000","discountStartTime":"2024-08-15T15:26:38+08:00","discountEndTime":"2024-10-01T00:05:00+08:00","price":10,"remainGPUCount":8},...]
```

**必要参数说明：**

|参数           |说明      |
|--------------|----------|
|name          |GPU 型号    | 
|regionID      |region id    |
|gpuCounts     |GPU 数量    | 
|sellingType   |消费类型，1为按量，2为包月，3为包周，4为包日| 

## 创建算力实例

### 请求

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusteName/instances`

**Body 请求参数：**

```json
{
  "Cost": {
    "CostType": "",
    "CouponID": "",
    "DiskSKUID": "",
    "GPUSKUID": "",
    "CostTime": ""
  },
  "VolumeMount": [
    {
      "PathInContainer": "",
      "Size": ,
      "Type": ""
    }
  ],
  "namespace": "",
  "displayName": "",
  "image": "",
  "Region": "",
}
```

**body 参数说明：**

|名称           |类型      |必选    |说明                                                           |
|--------------|----------|-------|---------------------------------------------------------------|
|Cost          |object    | 是    | GPU 规格信息 |
|CostType      |string    | 是    | 消费类型，1为按量，2为包月，3为包周，4为包日|
|CouponID      |string    | 否    | 优惠券 id，算力券只能用于按量的消费类型            |
|DiskSKUID     |string    | 是    | 磁盘 id ，目前只有 1      |
|GPUSKUID      |string    | 是    | GPU 规则 id，根据章节**查看GPU规格信息**获取 |
|CostTime      |string    | 否    | 付费时长：D，W，M, 例如3天：3D，当更新付费时长时，请在前面加+，例如，新增3天：+3D |
|VolumeMount   | object   | 是    | 磁盘挂载信息  |
|PathInContainer|string   | 否    | 挂载路径，默认是/root/data|
|Size          |integer   | 否    | 磁盘大小，单位G|
|Type          |string    | 否    | 磁盘类型，目前仅支持 shared-filesystem |
|namespace     |string    | 是    | 命名空间，和用户 id 相同|
|displayName   | string   | 是    | 实例名称     |
|image         |string    | 是    | 镜像名，包括官方镜像和私有镜像       |
|Region        |string    | 否    | 地区，默认北京一区|

### 响应

**Python 代码：**

```python
import requests
import json
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances"

body={
  "Cost": {
    "CostType": "1",
    "CouponID": "",
    "DiskSKUID": "1",
    "GPUSKUID": "66",
    "CostTime": ""
  },
  "VolumeMount": [
    {
      "PathInContainer": "/root/data",
      "Size": 50,
      "Type": "shared-filesystem"
    }
  ],
  "namespace": "xxx",
  "displayName": "test1",
  "image": "images.neolink-ai.com/matrixdc/tensorflow:2.15.0-python3.10-cuda12.1.0-cudnn8-devel-ubuntu22.04",
  "Region": ""
}
response = requests.post(url, json=body, headers=headers)

print(json.dumps(response.json(), indent=4))
```

**返回：**
```
{
    "name": "instance-ccffxxxx",
    "namespace": "xxx",
    "Region": "host-cluster",
    "displayName": "test1",
    "description": "",
    "annotations": {
        "neolink.ai/cost-coupon-id": "",
        "neolink.ai/cost-discount-id": "",
        "neolink.ai/cost-disk-sku-id": "1",
        "neolink.ai/cost-gpu-sku-id": "66",
        "neolink.ai/cost-order-id": "94b9e467-9d34-45bf-8e8f-e04115cf58b4",
        "neolink.ai/cost-time": "",
        "neolink.ai/cost-type": "1",
        "neolink.ai/description": "",
        "neolink.ai/display-name": "test1",
        "neolink.ai/gpu.machine": "4090",
        "neolink.ai/gpu.resource.key": "nvidia.com/gpu-4090",
        "neolink.ai/region": "host-cluster",
        "neolink.ai/saveDataEnabled": "false",
        "neolink.ai/unit-price": "250"
    },
    "uid": "8d40c2e6-a0b0-45c2-9b40-a0de065104f5",
    "image": "images.neolink-ai.com/matrixdc/tensorflow:2.15.0-python3.10-cuda12.1.0-cudnn8-devel-ubuntu22.04",
    "replicas": 1,
    "resources": {
        "cpu": "16",
        "memory": "96Gi",
        "GPUNum": "1",
        "GPUType": "4090"
    },
    "volumeMounts": [
        {
            "PathInContainer": "/",
            "Type": "local-filesystem",
            "Size": 30,
            "PVCName": "",
            "displayName": "\u7cfb\u7edf\u76d8",
            "filesystemType": "system"
        },
        {
            "PathInContainer": "/root/data",
            "Type": "shared-filesystem",
            "Size": 0,
            "PVCName": "volume-920020f7",
            "displayName": "\u78c1\u76d8-volume-920020f7",
            "filesystemType": "data"
        }
    ],
    "creationTimestamp": "2024-09-02T18:34:33+08:00",
    "updateTimestamp": "0001-01-01T00:00:00Z",
    "ScheduleStopTimestamp": "0001-01-01T00:00:00Z",
    "status": "Creating",
    "cost": {
        "CostType": "1",
        "CostTime": "",
        "DiscountID": "",
        "GPUSKUID": "66",
        "DiskSKUID": "1",
        "CouponID": ""
    }
}
```

## 获取实例列表

### 请求

**GET** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances`

### 响应

**Python 代码：**

```python
import requests
import json
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances"
response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))
```

**返回：**

```json
{
    "hasNextPage": false,
    "nodes": [
        {
            "name": "instance-ccffxxxx",
            "namespace": "xxx",
            "Region": "host-cluster",
            "displayName": "test1",
            "description": "",
            "annotations": {
                "neolink.ai/cost-coupon-id": "",
                "neolink.ai/cost-discount-id": "",
                "neolink.ai/cost-disk-sku-id": "1",
                "neolink.ai/cost-gpu-sku-id": "66",
                "neolink.ai/cost-order-id": "94b9e467-9d34-45bf-8e8f-e04115cf58b4",
                "neolink.ai/cost-time": "",
                "neolink.ai/cost-type": "1",
                "neolink.ai/description": "",
                "neolink.ai/display-name": "test1",
                "neolink.ai/gpu.machine": "4090",
                "neolink.ai/gpu.resource.key": "nvidia.com/gpu-4090",
                "neolink.ai/region": "host-cluster",
                "neolink.ai/saveDataEnabled": "false",
                "neolink.ai/unit-price": "250"
            },
            "uid": "8d40c2e6-a0b0-45c2-9b40-a0de065104f5",
            "servers": {
                "Jupyterlab": "http://8d40c2e6-a0b0-45c2-9b40-a0de065104f5.gw.neolink-ai.com/jupyter?token=7d27443c5718e75bee2da9f92fe6a50c",
                "Tensorboard": "http://8d40c2e6-a0b0-45c2-9b40-a0de065104f5.gw.neolink-ai.com/monitor",
                "SSH": {
                    "sshAddr": "ssh -p30099 root@8d40c2e6-a0b0-45c2-9b40-a0de065104f5.gws.neolink-ai.com",
                    "sshPassword": "kEyIX5R2dqJD"
                }
            },
            "image": "images.neolink-ai.com/matrixdc/tensorflow:2.15.0-python3.10-cuda12.1.0-cudnn8-devel-ubuntu22.04",
            "replicas": 1,
            "resources": {
                "cpu": "16",
                "memory": "96Gi",
                "GPUNum": "1",
                "GPUType": "4090"
            },
            "volumeMounts": [
                {
                    "PathInContainer": "/",
                    "Type": "local-filesystem",
                    "Size": 30,
                    "PVCName": "",
                    "displayName": "\u7cfb\u7edf\u76d8",
                    "filesystemType": "system"
                },
                {
                    "PathInContainer": "/root/data",
                    "Type": "shared-filesystem",
                    "Size": 50,
                    "PVCName": "volume-920020f7",
                    "displayName": "\u78c1\u76d8-volume-920020f7",
                    "filesystemType": "data"
                }
            ],
            "creationTimestamp": "2024-09-02T18:34:33+08:00",
            "updateTimestamp": "0001-01-01T00:00:00Z",
            "ScheduleStopTimestamp": "0001-01-01T00:00:00Z",
            "status": "Running",
            "cost": {
                "CostType": "1",
                "CostTime": "",
                "DiscountID": "",
                "GPUSKUID": "66",
                "DiskSKUID": "1",
                "CouponID": ""
            },
            "Pods": [
                {
                    "Name": "instance-ccff84c2-dd6nm",
                    "Containers": [
                        {
                            "Name": "worker"
                        }
                    ],
                    "nodeScheduled": "gpu-4090-03",
                    "ip": "172.31.213.79"
                }
            ]
        }
    ],
    "totalCount": 1
}
```

## 获取实例详情

### 请求

**GET** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/$instant_id`

### 响应

**Python 代码：**

```python
import requests
import json
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances/instance-4ca9xxxx"
response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))
```

**返回：**

```bash
{
    "name": "instance-4ca9xxxx",
    "namespace": "xxx",
    "Region": "host-cluster",
    "displayName": "test1",
    "description": "",
    "annotations": {
        "neolink.ai/cost-coupon-id": "",
        "neolink.ai/cost-discount-id": "",
        "neolink.ai/cost-disk-sku-id": "1",
        "neolink.ai/cost-gpu-sku-id": "66",
        "neolink.ai/cost-order-id": "cf4c99ff-cf7f-4c86-8f15-87cf5fb2ba14",
        "neolink.ai/cost-time": "",
        "neolink.ai/cost-type": "1",
        "neolink.ai/description": "",
        "neolink.ai/display-name": "test1",
        "neolink.ai/gpu.machine": "4090",
        "neolink.ai/gpu.resource.key": "nvidia.com/gpu-4090",
        "neolink.ai/region": "host-cluster",
        "neolink.ai/unit-price": "250"
    },
    "uid": "a7d2cbab-591d-4482-95ea-2df994ed1b22",
    "servers": {
        "Jupyterlab": "http://a7d2cbab-591d-4482-95ea-2df994ed1b22.gw.neolink-ai.com/jupyter?token=23a7676a0d18451dee9c08c3649a8288",
        "Tensorboard": "http://a7d2cbab-591d-4482-95ea-2df994ed1b22.gw.neolink-ai.com/monitor",
        "SSH": {
            "sshAddr": "ssh -p30379 root@a7d2cbab-591d-4482-95ea-2df994ed1b22.gws.neolink-ai.com",
            "sshPassword": "RuRbjZLWklIC"
        }
    },
    "image": "images.neolink-ai.com/matrixdc/tensorflow:2.15.0-python3.10-cuda12.1.0-cudnn8-devel-ubuntu22.04",
    "replicas": 1,
    "resources": {
        "cpu": "16",
        "memory": "96Gi",
        "GPUNum": "1",
        "GPUType": "4090"
    },
    "volumeMounts": [
        {
            "PathInContainer": "/",
            "Type": "local-filesystem",
            "Size": 30,
            "PVCName": "",
            "displayName": "\u7cfb\u7edf\u76d8",
            "filesystemType": "system"
        },
        {
            "PathInContainer": "/root/data",
            "Type": "shared-filesystem",
            "Size": 50,
            "PVCName": "volume-ed087526",
            "displayName": "\u78c1\u76d8-volume-ed087526",
            "filesystemType": "data"
        }
    ],
    "creationTimestamp": "2024-09-02T22:15:13+08:00",
    "updateTimestamp": "0001-01-01T00:00:00Z",
    "ScheduleStopTimestamp": "0001-01-01T00:00:00Z",
    "status": "Running",
    "cost": {
        "CostType": "1",
        "CostTime": "",
        "DiscountID": "",
        "GPUSKUID": "66",
        "DiskSKUID": "1",
        "CouponID": ""
    },
    "Pods": [
        {
            "Name": "instance-4ca97f58-6m9nv",
            "Containers": [
                {
                    "Name": "worker"
                }
            ],
            "nodeScheduled": "gpu-4090-03",
            "ip": "172.31.213.103"
        }
    ]
}
```

## 停止实例

### 请求

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/instance_name/power_off`

**body 请求参数：**

```
body = {
    "gracePeriodSeconds": "",
    "needSnapshot": "",
    "imageName": "",
    "tag": ""
}
```

**body 参数说明：**

|名称                 |类型      |必选    |说明                                                           |
|--------------------|----------|-------|---------------------------------------------------------------|
|gracePeriodSeconds |string    | 否    | Pod 体面终止限期，单位秒，系统首先发送停止系统指令，然后在强制删除之前等待容器内进程处理的时间, 默认为10秒|
|needSnapshot       |string    | 否    | 是否需要再关机的时候保存运行 container 为 image，默认为 False    |
|imageName          |string    | 否    | 保存的镜像名称         |
|tag                |string    | 否    | 镜像版本        |

### 响应

**Python 代码：**

```python
import requests
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances/instance-3ba5xxxx/power_off"

body = {
    "gracePeriodSeconds": 10,
    "needSnapshot": True,
    "imageName": "image1",
    "tag": "v1.1.0"
}

response = requests.post(url,json=body,headers=headers)
print(response.content.decode())
```

**返回：**

```bash
"ok"
```

## 启动实例

### 请求

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/$instance_id/power_off`

### 响应

```python
import requests
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances/instance-4ca9xxxx/power_on"

response = requests.post(url, headers=headers)
print(response.content.decode())
```

## 删除实例

### 请求

**DELETE** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances?name=$instance_id`

### 响应

**Python 代码：**

```python
import requests
headers = {
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances?name=instance-ccffxxxx"

response = requests.delete(url, headers=headers)

print(response.content.decode())
```

**返回：**

```bash
"ok"
```
