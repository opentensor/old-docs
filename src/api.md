# Prompting API

Presently, the Bittensor API supports causal language models and text completion inference. 

```python
import bittensor
llm = bittensor.prompting()

response = llm("The sky above the port was the color of television, tuned to a dead channel")

print(response)
```

In following snippet, `bittensor.prompting()` will create a `prompting` class containing two objects: 

1. A `metagraph` object that represents a snapshot of the network. 
2. A `dendrite` object that is responsible for sending queries to the network.

```python
In [28]: bittensor.prompting()
Out[28]:
prompting(
  (_metagraph): Metagraph(netuid:1, n:317, block:373560, network:finney)
  (_dendrite): TextPromptingDendrite()
)
```

When invoked with a text input, the prompting object will send it to the network and return the output.