---
sidebar_position: 3
title: Images
sidebar_label: Images
---

## Official Images

Neolink.AI provides a variety of official images. In the sidebar, select **Image Registry** to view a list of official images. Choose the appropriate official image and click **Deploy**.

<img src={require('../../static/en-img/imgmanagement/imagemanagement-1.png').default} alt="Upload Data" style={{width: '700px', height: 'auto'}} />

You will be redirected to the instance creation page with the selected official image.

<img src={require('../../static/en-img/imgmanagement/imagemanagement-2.png').default} alt="Upload Data" style={{width: '700px', height: 'auto'}} />

## Private Images

If you have configured an instance environment and wish to reuse it when switching servers or creating new instances, or if you want to maintain the environment for future needs, using private images is a great option. The platform provides 30 Gi of free private image storage. If the total exceeds 30 Gi, the excess will be charged at 0.01 CNY/day/Gi.

### Save Image

In the compute instance list, select **Save-to-image** on the right side of the instance details. This will save the instance environment as a private image, including all files on the system disk. Note that data disks will not be saved.

**NOTE**: Only running instances can be saved as images.

<img src={require('../../static/en-img/imgmanagement/imagemanagement-3.png').default} alt="Save Image" style={{width: '800px', height: 'auto'}} />

In the pop-up window for saving the image, you can customize the image name and version. After saving, you can view the image details under **Image Registry > Private Images**.

<img src={require('../../static/en-img/imgmanagement/imagemanagement-4.png').default} alt="Save Image" style={{width: '800px', height: 'auto'}} />

### Image Management

In the **Image Registry > Private Images** page, you can see the saved private images. Here, you can click the **Deploy** button to go to the instance creation page and deploy a private image, or delete a private image.

**NOTE**: Deleting an image may affect the normal restart of instances. Please proceed with caution.

<img src={require('../../static/en-img/imgmanagement/imagemanagement-5.png').default} alt="Image Management" style={{width: '800px', height: 'auto'}} />
