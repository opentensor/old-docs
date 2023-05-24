# Validating

Under the hood, Bittensor's validation uses a dual proof-of-stake, proof-of-work mechanism called Yuma Consensus which you can read about here. Yuma consensus rewards validators with ```dividends``` for producing evaluations of miner-value which are in agreement with the subjective evaluations produced by other validators weighted by ```stake```, TAO which has been locked into Bittensor's incentive mechanism and attached to a validator. 

Network validation is thus open to participants who hold TAO and have [registered](registration.md) a uid on any subnetwork. Attaching TAO on your validator can be achieved in two ways.

1. By staking fund to your miners directly by yourself
```bash
# Stake funds to your hotkey account within the bittensor incentive mechanism.
btcli stake --wallet.name YOUR_WALLET_NAME --wallet.hotkey YOUR_HOTKEY_NAME
```
2. Or by attracting delegated stake by nominating (and then advertising) your hotkey.
```bash
# Nominate your hotkey as a delegate, making it available for delegated stake.
btcli nominate --wallet.name YOUR_WALLET_NAME --wallet.hotkey YOUR_HOTKEY_NAME

# To delegate funds to the hotkey of a delegate (your own or others)  
btcli delegate --delegate_ss58key DELEGATE_SS58KEY
```

Bittensor's API is designed to allow Validators to write their own validation mechanisms and express their own subjective prefrences about what the network should learn. However, going too far outside consensus reduces the rewards validators attain while performing validation. To ensure your validator remains in alignment with others we recommend you run the core validator built for each subnetwork. Like with running mienrs, in order to run one of Bittensor's [core validators](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/validators), you must clone and install bittensor from [source](https://github.com/opentensor/bittensor.git). 
```bash 
$ git clone https://github.com/opentensor/bittensor.git
$ python3 -m pip install -e bittensor/
$ tree bittensor
    bittensor/                             
        neurons/                            # Miners and Validators across all subnetworks.
            text_prompting/                 # Miners and Validators for the text_prompting subnetwork.
                validators/                 # Validators.
                    core/                   # The root folder for the core validator.
                        neuron.py           # Core validator miner main script.
                        requirements.txt    # Core validator requirements.
                        README.md           # Core validator instructions.
                    ...
```
You can run the core validator using the following, where `--netuid 1` specifies the validator to be run on Subnetwork 1.
```bash
python3 ~/.bittensor/bittensor/neurons/text_prompting/validators/core/neuron.py --netuid 1
```