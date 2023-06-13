
## [api]


The Bittensor API allows clients to query the network through endpoints that have been made accessible by network validators. Clients using the network do not have to be otherwise involved in the incentive mechanism of the network. The default endpoint that is accessed through the API belongs to the [Opentensor Foundation](https://opentensor.ai/), however, any network validator is able to provide a unique entrypoint.

All entrypoints can be viewed using **btcli list_delegates**:

```bash dark
0      Openτensor Foundaτion
            https://opentensor.ai/

1      Foundry
            https://foundrydigital.com/

3      τaosτaτs
            https://taostats.io/
...
```



### _querying the network

Text prompting requests can be sent via **bt.prompt**.
```python numbered dark
import bittensor as bt
print ( bt.prompt( "Heraclitus was a " ) )
'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'
```

**bt.prompt** follows a role + message prompting format which allows system prompts and sequential followups.

```python numbered dark
import bittensor as bt
content = [
	{ 'role': 'system', 'content': 'You are my advisor' },
	{ 'role': 'user', 'content': 'Should I buy a boat?' },
	{ 'role': 'assistant', 'content': 'Willing to bring out another thousand?' },
	{ 'role': 'user', 'content': 'Yes, where should I buy a boat?' },
]
should_I_buy_a_boat = bt.prompt( content = content )
```


### _langchain integration

The BittensorLLM object can be integrated with langchain.

```python numbered dark removed=2,4 added=1,3
import bittensor as bt
from langchain import openai
llm = bt.BittensorLLM()
ll = openai.llm( api_key = **** )
llm( 'prompt me' )
```


### _multiple responses

You can return multiple responses for a single prompt.
```python numbered dark
bt.prompt( "What should I do today?", return_all = True )
[
	'You should buy a boat.',
	'As a language model I cannot answer that question.',
	'You should write in your journal.',
	'Mine bittensor.'
	...
]
```


### _specifying entrypoint

You can specify a unique entrypoint endpoint to query by its hotkey.
> NOTE: Note, unless that endpoint has specifically opened up access to this form of query, you are likely to have your messages blacklisted.
```python numbered dark
# Specify a separate entrypoint based on the delegate key.
open_endpoint_hotkey = "5F4tQyWrhfGVcNhoqeiNsR6KjD4wMZ2kfhLj4oHYuyHbZAc3"
print ( bt.prompt( "Heraclitus was a ", hotkey = open_endpoint_hotkey ) )
'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'
```


### _validator key

Power users who have a validator key registered on the network already do not need to access the network indirectly, and can instead make RPC connections directly to miners like so:
```python numbered dark
import bittensor as bt
wallet = bt.wallet() # Your validator wallet.
metagraph = bt.metagraph( netuid = 1 ) # Get state from subnetwork 1.
dendrite = bt.text_prompting( keypair = wallet.hotkey, axon = metagraph.axons[ 10 ] ) # Connection to uid 10
dendrite.forward( roles = ['system', 'user'], messages = ['you are my financial advisor', 'should I buy a boat?'] )
```
