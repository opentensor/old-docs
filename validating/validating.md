
## Validating

Network validation is thus open to participants who have [registered](../subnetworks/registration) a UID on any subnetwork **and** who have enough TAO staked on their hotkey to be considered a [top 128 validator](../validating/validator-permit).

### Staking

Attaching TAO on your validator can be achieved in two ways.
1. By staking TAO to your miners directly.
```bash dark
# Stake funds to your hotkey account within the bittensor incentive mechanism.
btcli stake
    --wallet.name YOUR_WALLET_NAME
    --wallet.hotkey YOUR_HOTKEY_NAME
```
2. By attracting delegated stake by nominating (and then advertising) your hotkey.
```bash dark
# Nominate your hotkey as a delegate, making it available for delegated stake.
btcli nominate
    --wallet.name YOUR_WALLET_NAME
    --wallet.hotkey YOUR_HOTKEY_NAME

# Delegate funds to the hotkey of a delegate (your own or others)
btcli delegate
    --delegate_ss58key DELEGATE_SS58KEY
```
### Running a Validator

After attaining enough TAO for a [validator permit](../validating/validator-permit) we recommend running Bittensor's [core validator](https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/validators). You can run and install the core validator from [source](https://github.com/opentensor/bittensor.git).
```bash dark
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
When running, specify the `--netuid 1` parameter to select the appropriate subnetwork for your validator, e.g. Subnetwork 1.
```bash dark title=neurons/text_prompting/validators/core link=https://github.com/opentensor/bittensor/tree/text_prompting/neurons/text/prompting/validators/core
python3 ~/.bittensor/bittensor/neurons/text_prompting/validators/core/neuron.py
    --netuid 1
    --wallet.name YOUR_WALLET_NAME
    --wallet.hotkey YOUR_HOTKEY_NAME
    --logging.trace
```

### Running with PM2
It is recommended that you run validator using a process manager such as [PM2](https://pm2.io/).
```bash dark
sudo apt-get install npm
npm install pm2
pm2 start <path to validator.py>
    --name my_validator
    --interpreter python3
    -- ... your args i.e. --wallet.name ...
```

### Validator Permit

Only the largest 128 validators, in terms of stake, on any particular subnetwork are considered to have `validator permit`. Validators with permit are considered active within Bittensor's mining mechanism, Yuma Consensus, can validate the network, and get `dividends`.

### How do I check to see if my validator has permit?
The amount can be pulled from the metagraph based on your uid.
```python numbered dark
import bittensor as bt
subnet = bt.metagraph(1)
wallet = bt.wallet( name = 'my_wallet_name', hotkey = 'my_validator_hotkey_name' )
my_uid = subnet.hotkeys.index( wallet.hotkey.ss58_address )
print ('validator permit', subnet.validator_permit[ my_uid ])
```

### How much TAO is required to attain a validator permit?
The amount of TAO required is depends on how the other largest 128 wallets distribute TAO across themselves. You can calculate the minimum using `bt.metagraph`:
```python numbered dark
import bittensor as bt
subnet = bt.metagraph(1)
stake_requirement = subnet.S.sort()[0][-128:]
print ('validator permit requirement', stake_requirement)
```
