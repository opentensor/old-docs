# Miners

Running a Bittensor Neuron consists of two steps: [Registration](registration.md) and [Serving a Neuron](neuron.md).

# Serving a Neuron

Once a hotkey is registered, it is now possible to serve a model on the Bittensor protocol and use it to compete with peers and contribute to the network’s overall intelligence. There is a pre-defined list of example neurons that [can be found here](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners). They can be run with the following command. For example, to run an OpenAI miner: 

```bash
python3 ~/.bittensor/bittensor/neurons/text/prompting/miners/openai/neuron.py --openai.api_key <your_openai_api_key> --netuid 1
```

This will run the OpenAI miner [found here](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners/openai) on subnet 1. Similarly to the other commands, you can also run the help command for a list of flags to specify: