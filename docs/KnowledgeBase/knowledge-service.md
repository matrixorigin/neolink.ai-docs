---
sidebar_position: 1
title: Knowledge Service
sidebar_label: Knowledge Service
---

## Create a Knowledge Base

Click **Knowledge Service** in the left navigation bar of the Neolink.AI platform to enter the **My Knowledge Base** page. Click **Create Knowledge Base** in the upper-right corner, and fill in the relevant information in the pop-up dialog box, including the data type (such as text or table), knowledge base name, description, embedding model, and knowledge tags. Finally, click **Confirm** to complete the creation.

<img src={require('../../static/img/knowledge/create-knowledgebase.png').default} alt="Create Knowledge Base" style={{width: '600px', height: 'auto'}} />

## Add Content

### Upload Files

In the knowledge base list, click the desired knowledge base to access its details page. Then, click the **Add Content** button in the upper-right corner to upload local files and add content.

<img src={require('../../static/img/knowledge/add-content.png').default} alt="Add Content" style={{width: '600px', height: 'auto'}} />

On the file upload page, you can upload documents. Supported file formats include TXT, PDF, DOC, and DOCX. You can upload up to 10 files at a time, with a cumulative total of no more than 300 files. Each file must not exceed 20MB, and files with duplicate names are not allowed.

<img src={require('../../static/img/knowledge/add-content-1.png').default} alt="Add Content" style={{width: '600px', height: 'auto'}} />

### Content Segmentation

You can segment the text content after uploading. On the segmentation settings page, you can either use the default automatic segmentation or customize it.

<img src={require('../../static/img/knowledge/add-content-4.png').default} alt="Segmentation" style={{width: '600px', height: 'auto'}} />

- **Segmentation Identifiers:** These identifiers are used to split long texts or complex data into smaller sections so that each paragraph, sentence, or data block can generate independent embedding vectors. The following identifiers are supported:

  - Line Break
  - Chinese Period
  - Chinese Exclamation Mark
  - Chinese Question Mark
  - English Period
  - English Exclamation Mark
  - English Question Mark

- **Maximum Segmentation Length:** The supported range is [100, 800].

- **Text Preprocessing Rules:** Preprocessing the text before generating embeddings is a key step to ensure the input is suitable for generating high-quality vector representations. The following rules are currently supported:
  - Replace consecutive spaces, line breaks, and tabs.
  - Remove all URLs and email addresses.

After segmentation, you can view the segmented content on the knowledge base page.

<img src={require('../../static/img/knowledge/add-content-3.png').default} alt="Add Content" style={{width: '800px', height: 'auto'}} />

If re-segmentation is needed, click the settings icon in the upper-right corner of the knowledge base page to enter the re-segmentation page.
