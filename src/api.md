# Prompting API

> NOTE: The Bittensor API is actively under development, and hence the API pages are subject to change as more functionality is added.
Presently, the Bittensor API supports causal language models and text completion inference. Expect this page to continuously update as we develop more API calls. 

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

When invoked with a text input, the prompting object will send it to the network and return the output. In addition to retrieving the best response, the Bittensor API can also return all relevant responses for you to manipulate and choose from according to your use case. This is possible by adding a `return_all = True` to your prompting call.

```python
import bittensor
prompts = bittensor.prompting()
responses =  prompts("Describe Ozymandias in one Sentence", return_all=True)
print(responses)
```

This returns a Python list of all the responses coming back from the network through the Validator API.

```bash
Out[20]: [
    'Ozymandias was a powerful and arrogant ancient Egyptian pharaoh whose legacy has been reduced to ruins.', 
    'Ozymandias is a poem by Percy Bysshe Shelley that tells the story of a powerful and arrogant ruler who is ultimately brought down by the forces of nature.', 
    'Ozymandias was a powerful ancient Egyptian pharaoh known for his grandiose monuments and hubristic attitude.', 
    'Ozymandias was a powerful ancient Egyptian king whose empire has long since crumbled into ruins.', 
    "Excellent question! I'm happy to discuss this further, but to best assist you, I think maybe you could tell me a bit more about the subject?", 
    "Ozymandias is a poem by Percy Bysshe Shelley that describes the ruins of a once-great king's statue as a symbol of the fleeting nature of power and human achievement.", "Ozymandias is a literary character who represents the downfall of human power and pride.", 
    'Ozymandias was a powerful pharaoh of ancient Egypt, whose legacy is now remembered primarily through the ruins of his once-great kingdom.'
    ]
```