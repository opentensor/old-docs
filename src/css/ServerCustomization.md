# Customizing your miner - Server
---
When you first enter the network, you will likely be running a Server. Until you have accrued ~700 Tao, serving is the only way to mine a significant amount of Tao, and the ultimate goal is to upgrade, customize and design your model in such a way as to optimize this. 



## Choosing a model 


By default, your miner is outfitted with the gpt2 model. While the ultimate goals is to upgrade, customize, and design your own model from scratch, choosing one from [Hugging Face](https://huggingface.co/models) is a good place to start.

*String to ``btcli run`` or any other mining start command.*

The argument that downloads a Hugging Face model is:


```bash
--neuron.model_name 
```


For example, if you want to run Eleuther AI's gpt-j-6B model: 


```bash
--neuron.model_name EleutherAI/gpt-j-6B
```

*Choose ``advanced_server`` when using a pretrained model.*

As expected, the larger the model is, the more computational resources it will need to run smoothly on the network. 

*View [Hugging Face](https://huggingface.co/models) for more options or [finetune](../nested/FineTuning.md) your own!*



## Choosing peers 


By associating only with high-stake Validators, Servers are able to optimize their inflation. Using the "blacklist" argument, you can decide the minimum stake a Validator must have to send a forward request. 


```bash
--neuron.blacklist.stake.forward <>
```



## Padding parameter


The padding parameter adjusts the embedding dimensions for your model to match the network dimension, which is currently set to 1024. By default, the padding is turned on, however, while this is useful for smaller models, it might be useful to turn it off for larger models. This command only works for advanced servers.


```bash
--neuron.padding false
```



## Allocating Tao


The more Tao you have staked to a hotkey, the more protection that hotkey has from getting deregistered in the network. However, Tao staked in your hotkey, as a Server, does not increase your dividends. 



## Preventing timeouts 


Optimizing request speed is essential for mining. The faster your Server can process Validator requests, the better its earnings will be. A Server must be able to process a request within one blockstep, or else a timeout will occur. If this happens, you will need to improve your connection, or your hardware. As a server, you are only concerned with forward requests, and timeouts here mean your Server cannot computationally keep up with the demands of the network. 


View your timeouts on your "logs" that pop up the moment your miner starts to run when using:


```bash
--logging.debug
```


This will show you requests on the [axon](src/../../nested/Glossary.md#axon) and the [dendrite](src/../../nested/Glossary.md#dendrite) as well as weights set on the chain.