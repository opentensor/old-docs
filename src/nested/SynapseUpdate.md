# Updating to Synapses

Synapses is the latest update to Bittensor, and updating to Synapses will be required of everyone running a miner on the Bittensor network. This page will take you through everything you need to do to transition you and your miners to the Synapse update.

1. Pull the latest master and install.

```bash
git -C ~/.bittensor/bittensor pull origin master
python3 -m pip install -e ~/.bittensor/bittensor
```

2. Restart your miners.

Stop and restart all your Servers and Validators. Anyone running an ``advanced_server``, ``template_miner``, or ``template_server`` before the update will need to call upon ``core_server`` instead. 

## That’s it!


---
# Things to keep in mind:


## Size Matters

Synapses enable more direct and accurate neuron evaluation than before, with validation losses measured directly and converted to a parameter count estimate via scaling laws of neural language models. **Size matters** and it is expected that Servers will need large GPUs to run larger models so as to remain competitive.

## Does my Validator now need a GPU?

On the old network Validators did not require a GPU to function adequately. A CPU Validator may still suffice, but as the network scales with a more powerful growing network of GPU-based Servers, Validators will eventually likely require GPU acceleration to perform more sophisticated validation. Keep an eye on what the network is demanding when deciding what hardware your Validator might need. 

## Very large models

Models larger than a single 80GB A100 GPU will take extra configuration not currently provided in core_server, since parameters would have to be split across more than one device. This parameter distribution over multiple GPUs tends to be model specific to obtain the most streamlined pipeline parallelism and requires careful consideration.

## New arguments

```
--neuron.local_train
neruon.local_train:
```
- If true, allow local training.
```
--neuron.remote_train
neuron.remote_train:
```
- If true, allow remote training.
```
--neuron.validation_synapse
neuron.validation_synapse:
```
- For Validators only. Synpase used for validation <TextCausalLMNext | TextCausalLM>. Default TextCausalLMNext. This should generally not be used.
