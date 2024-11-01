---
sidebar_position: 6
title: experiment
sidebar_label: experiment
---

Experiment is an online interactive platform where users can input data and observe model outputs directly without programming, ideal for quickly testing and understanding model performance.

1. Go to the **Experience** Center in the left sidebar. On the **Experience** Center page, you can see the available models, and filter them by Model.

<img src={require('../../static/img/experience/1.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />

2. In the Prompt section, enter a system prompt, such as “Hello, I am your dedicated AI customer service,” to adjust the model’s output.

<img src={require('../../static/img/experience/2.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />

3. Finally, adjust the Temperature, Top P, and Max_tokens parameters to control the model’s output.

• Temperature controls the randomness and creativity of the generated text. Higher values increase randomness, with a range of 0-1.

• Top P manages the diversity of output tokens. Higher values allow for more variety, with a range of 0-1.

• Max_tokens limits the maximum number of tokens in the output. The default value is 200, with a maximum of 4096.
<img src={require('../../static/img/experience/3.png').default} alt="体验中心" style={{width: '1000px', height: 'auto'}} />

Note:

1. Usage in the Experience Center does not count toward the API call limit on the user’s account.

2. Streaming output is enabled by default, with context memory for up to 10 turns.
