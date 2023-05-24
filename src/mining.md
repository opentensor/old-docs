# Mining

Before running a miner on bittensor you must [register](registration.md) a hotkey on one of bittensor's [subnetworks](subnetworks.md). Once a hotkey is registered it is possible mine from that slot by coding your own miner, or by selecting and hosting one of Bittensor's many [pre-built miners](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners). 

Bittensor miners must service the task loads that are required by validators on each subnetwork. For instance, by generating responses to prompts on Bittensor text-to-text subnetwork 1. In all cases, miners implement 3 core methods which determine how they respond to requests and in what order those are processed. 

1. A function which returns true if the miner will not process the request.
    ```python
        def blacklist( self, forward_call: bittensor.Call ) -> bool:
    ```

2. A function which returns the priority of the request to be processed by the request.
    ```python
        def priority( self, forward_call: bittensor.Call ) -> float:
    ```

3. A function which returns the task output from the passed request.
    ```python
        def forward( self, inputs: Any ) -> Any:
    ```

To run one of Bittensor's [pre-built miners](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners), you must clone and install bittensor from [source](https://github.com/opentensor/bittensor.git). 
```bash 
$ git clone https://github.com/opentensor/bittensor.git
$ python3 -m pip install -e bittensor/
$ tree bittensor
    bittensor/                             
        neurons/                            # Miners and Validators across all subnetworks.
            text_prompting/                 # Miners and Validators for the text_prompting subnetwork.
                miners/                     # Miners.
                    GPT4ALL/                # The root folder for the GPT4ALL miner.
                        neuron.py           # GPT4ALL miner main script.
                        requirements.txt    # GPT4ALL requirements.
                        README.md           # GPT4ALL instructions.
                    ...
```
The miner associated with each subnetwork is stored within its own directory within ```bittensor/neurons/<subnetwork>/miners/```` with unqiue requirements and instructions. For instance, you can run the GPT4ALL miner on subnetwork 1 as follows. 
```bash
python3 -m pip install -r bittensor/neurons/text_prompting/miners/GPT4ALL/requirements.txt
python3 bittensor/neurons/text_prompting/miners/GPT4ALL/neuron.py --netuid 1 --wallet.name YOUR_WALLET_NAME --wallet.hotkey YOUR_HOTKEY_NAME --logging.debug
```

We recommend reading detailed instructions about each miner through their ```--help``` commands, since each miner may contains unique setup and hyperparameterization instructions
```bash
python3 bittensor/neurons/text_prompting/miners/GPT4ALL/neuron.py --help
```

