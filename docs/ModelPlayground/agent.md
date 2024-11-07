---
sidebar_position: 4
title: Agent Application
sidebar_label: Agent Application
---

Users can use the Agent tool to build Agent applications based on a chat dialogue model. These applications support access to knowledge bases and provide contextual information for conversations. Users can connect through either a public access link or API integration.

## Create an Agent

In the platform’s left sidebar under **Model Service**, find **Agent App** and click **Create Agent** on the right.

<img src={require('../../static/en-img/knowledge/agent-1.png').default} alt="Create Agent" style={{width: '600px', height: 'auto'}} />

## Publish an Agent

Click on the Agent you want to publish from the Agent list to access the details page. To create a complete Agent, you need to configure the following:

- **Prompt word**: Define the role, responsibilities, and skills of the Agent to control the tone and direction of the conversation.
- **Knowledge base**: By default, the knowledge base is empty. You can import a knowledge base as needed to provide contextual references. For more details on how to use knowledge bases, refer to the [Knowledge Service](../KnowledgeBase/knowledge-service.md) section.
- **Model**: Select the large language model to be used for the Agent’s conversations. Neolink and OpenAI model services are supported, but note that OpenAI may have network connectivity issues. If using OpenAI, you must enter a proxy address in the API Base field, as direct connections to the official OpenAI endpoint are currently unavailable.

Once the configuration is complete, you can test the Agent in the **Debugging and Preview** interface on the right to validate and fine-tune its performance.

<img src={require('../../static/en-img/knowledge/agent-2.png').default} alt="Create Agent" style={{width: '600px', height: 'auto'}} />

After debugging, click the **Release** button in the upper-right corner to publish the Agent. Return to the Agent list, and you will see the Agent status marked as **Published**.

<img src={require('../../static/en-img/knowledge/agent-3.png').default} alt="Create Agent" style={{width: '600px', height: 'auto'}} />

You can modify and update the Agent at any time.

## Access Statistics

On the **Access Statistics** page, we provide data on the number of messages and token usage for the Agent application, including data from the debug and preview stages.

<img src={require('../../static/en-img/knowledge/agent-4.png').default} alt="Create Agent" style={{width: '800px', height: 'auto'}} />

Copy the access URL and open it in a browser to run the Agent directly. The URL can be shared, allowing external users to access and use the Agent without logging in.

<img src={require('../../static/en-img/knowledge/agent-5.png').default} alt="Create Agent" style={{width: '600px', height: 'auto'}} />
