### [overview]


Bittensor is a mining network, similar to Bitcoin, that offers censorship-resistant access to a decentralized network of machine learning models. By leveraging digital incentives and rewarding participants directly for their contributions of computational resources, expertise and innovation, Bittensor establishes a comprehensive,  open-source ecosystem of artificial intelligence competencies. The native currency, TAO, constitutes both reward and access token to the network.

This documentation covers the three primary ways that users can interact with Bittensor: mining, validating, and through the API as a client.



### _mining

Individuals contributing value to the network in return for compensation in the form of TAO. Start [here](mining/mining).

Follow [this](mining/mining) link to begin.

```bash
bittensor/
    neurons/
        text/
            prompting/
                miners/
                    GPT4ALL/
                        neuron.py
```


### _validating

Tao holders who wish to govern Bittensor directly and use the network at its full capactiy bandwidth and fidelity.  Start [here](validating/validating).

```bash
bittensor/
    neurons/
        text_to_embedding/
        text_prompting/
            validators/
                core/
                    neuron.py
```
### _api

Users, researchers or companies, seeking to access bittensor directly using client facing APIs. Start [here](clients/clients).

```bash
In [4]: llm( "Heraclitus was a ?" )
Out[4]: 'Greek philosopher known for his doctrine of change and the famous quote, "No man ever steps in the same river twice."'
```
