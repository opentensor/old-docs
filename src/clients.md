# Clients

Without participating directly in Bittensor’s incentive mechanism, i.e. before holding TAO, becoming a miner, or being a validator, the only way to access Bittensor is by relaying queries through endpoints who have opened exterior access to developers. By default, Bittensor’s api uses the [Opentensor Foundation's](https://opentensor.ai/) endpoint which acts as a bridge onto the network. To access other validators endpoints you must specify their hotkey, found by running:

```btcli list_delegates```. 
```
0      Openτensor Foundaτion 
            https://opentensor.ai/      

1      Foundry                      
            https://foundrydigital.com/      

3      τaosτaτs                     
            https://taostats.io/
...      
```
The exact method of interacting with Bittensor through these endpoints may be distinct to them and we recommend visiting their website to see how. However, by default the bittensor API is designed to work with the Opentensor Foundations entrypoint onto Bittensor which can be queried out of the box.

```python
import bittensor as bt

# Query through the foundation endpoint.
print ( bt.prompt( "Heraclitus was a ") )
'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'

# The API also contains BittensorLLM which can be integrated with langchain.
llm = bt.BittensorLLM()
llm( 'prompt me' )

# Return multiple responses for a single prompt.
bt.prompt( "What should I do today?", return_all = True )
[
	'You should buy a boat.',
	'As a language model I cannot answer that question.',
	'You should write in your journal.',
	'Mine bittensor.'
	...
] 
```
Note in order to specify a differnent entrypoint you must retrieve the hotkey of the validator endpoint to use. For example, to specify the endpoint owned by the hotkey
```5F4tQyWrhfGVcNhoqeiNsR6KjD4wMZ2kfhLj4oHYuyHbZAc3```, you can run the following. Note, unless that endpoint has specifically opened up access to this form of query, you are likely to have your messages blacklisted. 

```python
# Specify a separate entrypoint based on the delegate key.
print ( bt.prompt( "Heraclitus was a ", hotkey = "5F4tQyWrhfGVcNhoqeiNsR6KjD4wMZ2kfhLj4oHYuyHbZAc3" ) )
'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'
```

Power users who have a validator key registered on the network already do not need to access the network indirectly, and can instead make RPC connections directly to miners like so:

```python
import bittensor as bt
wallet = bt.wallet() # Your validator wallet.
metagraph = bt.metagraph( netuid = 1 ) # Get state from subnetwork 1.
dendrite = bt.text_prompting( keypair = wallet.hotkey, axon = metagraph.axons[ 10 ] ) # Connection to uid 10
dendrite.forward( roles = ['system', 'user'], messages = ['you are my financial advisor', 'should I buy a boat?'] )
```