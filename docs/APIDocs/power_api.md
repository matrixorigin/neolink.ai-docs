---
sidebar_position: 1
title: Computing API
sidebar_label: Computing API
---

## API Credentials

### Obtaining API Credentials

Select **API Credentials** from the dropdown menu in the upper-right corner of the platform, and you will be redirected to the API credentials page.

<img src={require('../../static/en-img/apikey/token-1.png').default} alt="Get Token" style={{width: '800px', height: 'auto'}} />

Click **New Token**, enter a custom token name, and the default validity period is 3650 days, which can be adjusted as needed.

<img src={require('../../static/en-img/apikey/token-2.png').default} alt="Get Token" style={{width: '800px', height: 'auto'}} />

After clicking **Confirm**, the newly generated token will appear in the list. Please note that the token is only generated once, so be sure to copy and save it properly! If the token is lost, you can create a new one or **regenerate** it.

<img src={require('../../static/en-img/apikey/token-3.png').default} alt="Get Token" style={{width: '800px', height: 'auto'}} />

## Retrieving `region_id` and `clusterName`

- `region_id`: Region ID
- `clusterName`: Cluster name

### Request

**GET** `https://neolink-ai.com/mdc/api/v1/regions`

### Response

**Python Code:**

```python
import requests
headers = {
    "namespace": "$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/regions"

response = requests.get(url, headers=headers)
print(response.content.decode())
```

**Sample Response:**

```bash
[{"id":"14c5a9e3-0d09-4aa0-99d3-c096b80cceaa","region":"北京一区","clusterName":"host-cluster","harborAddr":"images.neolink-ai.com","howlerID":"69e377a7-99d1-cca0-ef58-cfce14a336b2","createdAt":"2024-07-15T12:00:23.227+08:00","updatedAt":"2024-07-15T12:00:23.227+08:00"}]
```

## Viewing GPU Specifications

### Request

**GET** `https://neolink-ai.com/mdc/api/v1/skus/computings?region_id=$region_id`

### Response

**Python Code：**

```python
import requests
headers = {
     "namespace" "$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/skus/computings?region_id=14c5a9e3-0d09-4aa0-99d3-c096b80cceaa"
response = requests.get(url, headers=headers)

print(response.content.decode())
```

**Sample Response:**

```bash
[{"name":"H20","regionID":"14c5a9e3-0d09-4aa0-99d3-c096b80cceaa","cpuArch":"x86-64","cpuSeries":"Inter Xeon","cpucores":24,"memoryCount":192,"cpuVendor":"Inter","gpuSeries":"H20","gpuProduct":"H20","gpuResourceKey":"nvidia.com/gpu-h20","gpuCounts":1,"gpuMemory":96,"systemstorage":30,"datastorage":50,"skusID":"2","regionName":"北京一区","clusterName":"host-cluster","sellingType":"1","ratio":0.48,"discountID":"10000","discountStartTime":"2024-08-15T15:26:38+08:00","discountEndTime":"2024-10-01T00:05:00+08:00","price":10,"remainGPUCount":8},...]
```

**Parameter Explanation:**

Parameter Description
name GPU model
regionID Region ID
gpuCounts Number of GPUs
sellingType Billing type: 1 - Pay-as-you-go, 2 - Monthly, 3 - Weekly, 4 - Daily

| Parameter   | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| name        | GPU model                                                           |
| regionID    | Region ID                                                           |
| gpuCounts   | Number of GPUs                                                      |
| sellingType | Billing type: 1 - Pay-as-you-go, 2 - Monthly, 3 - Weekly, 4 - Daily |

## Creating a Computing Instance

### Request

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusteName/instances`

**Body Parameters:**

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

**Parameter Explanation:**

| Name            | Type    | Required | Description                                        |
| --------------- | ------- | -------- | -------------------------------------------------- |
| Cost            | object  | YES      | GPU specification information                      |
| CostType        | string  | YES      | Billing type: 1 - Pay-as-you-go, 2 - Monthly, etc. |
| CouponID        | string  | NO       | Discount coupon ID (valid only for pay-as-you-go)  |
| DiskSKUID       | string  | YES      | Disk ID (currently only 1 available)               |
| GPUSKUID        | string  | YES      | GPU SKU ID (retrieved from GPU specifications)     |
| CostTime        | string  | NO       | Payment duration: e.g., 3 days: 3D, extend by +3D  |
| VolumeMount     | object  | YES      | Disk mount information                             |
| PathInContainer | string  | NO       | Default path /root/data                            |
| Size            | integer | NO       | Disk size in GB                                    |
| Type            | string  | NO       | Disk type (e.g., shared-filesystem)                |
| namespace       | string  | YES      | Namespace (same as user ID)                        |
| displayName     | string  | YES      | Instance name                                      |
| image           | string  | YES      | Image name (official or private)                   |
| Region          | string  | NO       | Default: Beijing Zone 1                            |

### Response

**Python Code:**

```python
import requests
import json
headers = {
    "namespace" "$userid",
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

**Response:**

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

## Get Instance List

### Request

**GET** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances`

### Response

**Python Code:**

```python
import requests
import json
headers = {
    "namespace" "$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances"
response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))
```

**Response**

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

## Get Instance List

### Request

**GET** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/$instant_id`

### Response

**Python Code:**

```python
import requests
import json
headers = {
    "namespace" :"$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances/instance-4ca9xxxx"
response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))
```

**Response**

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

## Stop Instance

### Request

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/instance_name/power_off`

**Body Request Parameters:**

```
body = {
    "gracePeriodSeconds": "",
    "needSnapshot": "",
    "imageName": "",
    "tag": ""
}
```

**Description of the body parameter:**

| Name               | Type   | Required | Description                                                                                                                                                                                         |
| ------------------ | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gracePeriodSeconds | string | NO       | Grace period for terminating a pod in seconds. The system sends a stop command first, then waits for processes inside the container to finish before forcefully deleting it. Default is 10 seconds. |
| needSnapshot       | string | NO       | Whether to save the running container as an image upon shutdown. Default is False.                                                                                                                  |
| imageName          | string | NO       | Name of the saved image.                                                                                                                                                                            |
| tag                | string | NO       | Version of the image.                                                                                                                                                                               |

### Response

**Python Code:**

```python
import requests
headers = {
    "namespace" :"$userid",
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

**Response**

```bash
"ok"
```

## Start Instance

### Request

**POST** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances/$instance_id/power_off`

### Response

```python
import requests
headers = {
    "namespace" :"$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances/instance-4ca9xxxx/power_on"

response = requests.post(url, headers=headers)
print(response.content.decode())
```

## Delete Instance

### Request

**DELETE** `https://neolink-ai.com/mdc/api/v1/clusters/$clusterName/instances?name=$instance_id`

### Response

**Python Code:**

```python
import requests
headers = {
    "namespace" :"$userid",
    "Authorization": "bearer $token"
}

url = "https://neolink-ai.com/mdc/api/v1/clusters/host-cluster/instances?name=instance-ccffxxxx"

response = requests.delete(url, headers=headers)

print(response.content.decode())
```

**Response**

```bash
"ok"
```
