# Server Customization
---
When you first enter the network, you will be running a Server. Until you have accrued ~1000 Tao, serving is the only way to mine a significant amount of Tao, and the ultimate goal is to upgrade, customize and design your model in such a way as to optimize this. 
​


## Choosing a Model 
​

By default, your miner is outfitted with the gpt2 model. While the ultimate goals is to upgrade, customize, and design your own model from scratch, choosing one from [Hugging Face](https://huggingface.co/models) is a good place to start. 
​

The argument that downloads a Hugging Face model is:
​

```bash
--neuron.model_name 
```


For example: 
​

```bash
--neuron.model_name distillgpt2
```


These are some popular models, however you are not limited to only these:
​

- distilgpt2
- gpt2
- distilbert-base-uncased-finetuned-sst-2-english
- roberta-base
- distilbert-base-uncased
- bert-base-cased
- xlm-roberta-large-finetuned-conll03-english

As expected, the larger the model is, the more computational resources it will need to run smoothly on the network. 

​*View [Hugging Face](https://huggingface.co/models) for more options or fintune your own!*



## Choosing Peers 
​

By associating only with high-stake Validators, Servers are able to optimize their inflation. Using the "blacklist" argument, you can decide the minimum stake a Validator must have to send a forward request. By default, server only interact with Validator with stake above 1000, but you can increase that even further if you like. 
​

```bash
--neuron.blacklist.stake.forward <>
```



## Padding 
​

The padding parameter adjusts the embedding dimensions for your model to match the network dimension, which is currently set to 1024. By default, the padding is turned on, however, while this useful for smaller models, it is useful to turn it off for larger models. This command only works for advanced servers
​

```bash
neuron.padding false
```



## Staking Tao
​

The more Tao you have staked to a hotkey, the more protection that hotkey has from getting deregistered in the network. However, Tao staked in your hotkey, as a Server, does not increased your dividends. 
​


## Timeouts 
​

Optimizing request speed is essential for mining. The faster your Server can process Validator requests, the better its earnings will be. A server must be able to process a request within one blockstep, or else a timeout will occur. If this happens, you will need to improve your connection, or your hardware. As a server, you are only concerned with forward requests, and timeouts here mean your Server cannot computational keep up with the demands of the network. 
​

Check your timeouts on your "logs" that pop up the moment your miner starts to run. You can also access it this way: 
​

```bash
--logging.debug
```


This will show you requests on the [axon](src/../Glossary.md#axon) and the [dendrite](src/../Glossary.md#dendrite) as well as weights set on the chain. 
