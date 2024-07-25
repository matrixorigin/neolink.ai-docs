---
sidebar_position: 1
title: 概要
sidebar_label: 概要
---
## 介绍

您可以通过任何语言的 HTTP 请求与我们的大模型 API 进行交互，比如文本生成、Embedding类型等。

## 鉴权

使用API Keys进行鉴权。您可以在以下界面上创建API Keys。所有的API请求都需要在请求头中添加`Authorization`字段:
```http
Authorization: Bearer $YOUR_API_KEY
```