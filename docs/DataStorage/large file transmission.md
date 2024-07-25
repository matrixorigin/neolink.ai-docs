---
sidebar_position: 5
title: 大文件传输
sidebar_label: 大文件传输
---
              ## 获取 bucket 信息
> 页面获取，对外的 s3 gateway 访问地址  https://file.gw.neolink.com
``` url
 https://file.gw.neolink.com
```
## 获取认证信息 
> 页面获取，保存在用户空间的secret
``` yaml
  accessKey: YnVja2V0LTE4NDM3MDc3NTA4
  secretKey: dklIZEJYU1ZnYkRmMUhETGRnaExGRXhHVUMwQVZhUXFwaFpaRUJnUg==
```
## 获取 mc 客户端
为避免兼容性问题，我们推荐采用的 mc 的版本为 RELEASE.2021-04-22T17-40-00Z，你可以在这个[地址](https://dl.min.io/client/mc/release)找到历史版本和不同架构的 mc，比如这是 amd64 架构 RELEASE.2021-04-22T17-40-00Z 版本的 mc 的[下载地址](https://dl.min.io/client/mc/release/linux-amd64/archive/mc.RELEASE.2021-04-22T17-40-00Z)

> 页面可以提供下载的
1. 下载安装完成 mc 后添加一个新的 alias：

``` shell
mc alias set bucket-18437077508 https://file.gw.neolink.com YnVja2V0LTE4NDM3MDc3NTA4 dklIZEJYU1ZnYkRmMUhETGRnaExGRXhHVUMwQVZhUXFwaFpaRUJnUg==

```
然后，你可以通过 mc 客户端向项目下的存储上传下载文件了。
## mc 上传、下载文件示例
``` shell
# 获取存储名称，名称为 pvc 前缀
mc ls  bucket-18437077508 
# 上传文件
mc cp ./sources.file  bucket-18437077508/pvc-d8f5994f-9207-4453-9461-d856c24b1d35
#下载文件
mc  bucket-18437077508/pvc-d8f5994f-9207-4453-9461-d856c24b1d35/target.file sources.file
```

_Originally posted by @LIENZHIADMIN in https://github.com/matrix-dc/gpu-portal/issues/298#issuecomment-2249233701_
            