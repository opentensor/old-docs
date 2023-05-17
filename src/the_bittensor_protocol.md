# The Bittensor Protocol

The Bittensor protocol provides access to the Bittensor network, a decentralized ecosystem of machine learning models. Through strategic use of incentives, the network drives the development of efficient and client-aligned models, continuously optimizing value, diversity and low inference latency. The network accommodates a multitude of intelligence modalities, all of which are accessible via the API. The currently accessible modalities include text completion and causal language modelling tasks. 

# Use Cases

The following are examples of network capabilities: 

## ****Text Completion****

The Bittensor network hosts a diverse ensemble of models, including Llama, GPT4all, Vicuna, and others. These models can be collectively or individually queried to perform various natural language tasks, for example, text completion.

``` python
In [4]: llm("Heraclitus was a ")
Out[4]: 'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'
```

## ****Text Classification****

The diversity present within the network allows users to obtain multiple perspectives while addressing a given problem. By aggregating numerous responses, users can gain valuable insights, enhancing their understanding of domain-specific challenges, such as sentiment analysis. 


``` python
In [9]: llm("What is the sentiment of the following: 'I love Bittensor")
Out[9]: 'The sentiment of the statement "I love Bittensor" is positive.'
```
