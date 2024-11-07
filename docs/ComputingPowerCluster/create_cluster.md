---
sidebar_position: 3
title: Create Cluster
sidebar_label: Create Cluster
---

The platform offers dedicated host leasing services, including models such as H20, 3090, 4090, and H100. Multiple hosts of the same specification can form a compute cluster, with interconnected hosts within the cluster. This is ideal for users with security requirements, those needing dedicated resources, and users seeking discounts.

## Create a Cluster

Navigate to **Compute Clusters** from the left sidebar, click **Create Cluster**, select the cluster network, GPU model, and cluster name, and click **Confirm**.

<img src={require('../../static/en-img/powercluster/create-cluster-1.png').default} alt="Create Cluster" style={{width: '1000px', height: 'auto'}} />

Once created, the newly created cluster will appear in the cluster list.

<img src={require('../../static/en-img/powercluster/cluster-3.png').default} alt="Create Cluster" style={{width: '1000px', height: 'auto'}} />

## Operations

After the cluster is created, you can perform scaling operations, view host details within the cluster, edit the cluster configuration, and manage cluster dissolution.

**NOTE**: During scaling, only hosts in the same region, with the same model, on the same network, and not already part of a cluster will appear in the dropdown list.

<img src={require('../../static/en-img/powercluster/cluster-2.png').default} alt="Cluster Scaling" style={{width: '1000px', height: 'auto'}} />
