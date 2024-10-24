---
sidebar_position: 3
title: Create API Key
sidebar_label: Create API Key
---

API Keys allow access to all models in the Model Hub. API Keys are valid long-term, so please do not share the key in public environments and store it securely. Follow the steps below to create an API Key:

1. Go to **API Management** in the left sidebar and click **API KEY**.  
   <img src={require('../../static/img/apikey/apikey1.png').default} alt="Model Hub" style={{width: '1000px', height: 'auto'}} />

2. Click **Create API KEY**.  
   <img src={require('../../static/img/getstarted/modelservice4.png').default} alt="Model Hub" style={{width: '1000px', height: 'auto'}} />

3. In the **Model Hub**, select the model you want to use and copy its model ID. Use this model ID in the "model" field of the API request header to call the corresponding model. For more details, please refer to the [Model API Documentation](/APIDocs/model-api/overview).
