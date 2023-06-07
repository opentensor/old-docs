
## Mining

Before mining you must [register](subnetworks/registration) the [hotkey of your wallet](getting-started/wallets) into a UID slot on one of Bittensor's [subnetworks](subnetworks/subnetworks), once this UID is yours you can run [your own miner](mining/custom_miners), or select one of Bittensor's many [pre-built miners](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners).


### Running Pre-Built Miners


Bittensor's [pre-built miners](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners) are installed from [source](https://github.com/opentensor/bittensor.git). For instance,
```bash dark title=bittensor/neurons/text_prompting/miners/GPT4ALL link=https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/miners/GPT4ALL
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
Each miner comes with unqiue requirements and instructions in their source directory `bittensor/neurons/<subnetwork>/miners/<miner name>`.
```bash dark
# Installing miner requirements
python3 -m pip install -r bittensor/neurons/text_prompting/miners/GPT4ALL/requirements.txt
```
Each miner contains unique setup and hyperparameterization instructions. We recommend reading detailed instructions about each miner through their `--help` commands.
```bash dark
# Reading miner --help.
python3 bittensor/neurons/text_prompting/miners/GPT4ALL/neuron.py
    --help
```
Runing the miner.
```bash dark
python3 bittensor/neurons/text_prompting/miners/GPT4ALL/neuron.py
    --netuid SUBNETWORK_TARGET_UID
    --wallet.name YOUR_WALLET_NAME
    --wallet.hotkey YOUR_HOTKEY_NAME
    --logging.debug
```

### Running with PM2


It is recommended that you run miners using a process manager such as [PM2](https://pm2.io/).
```bash dark
sudo apt-get install npm
npm install pm2
pm2 start <path to neuron.py>
    --name my_miner
    --interpreter python3
    -- ... your args i.e. --wallet.name ...
```
