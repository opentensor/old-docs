# Getting started

This section will guide you through the basic steps necessary to run a miner in the Bittensor network. Considering the rapid expansion of - and competition within - the network since its launch in November 2021, registration difficulty is constantly shifting and there is no guarantee that the same calibre of hardware will always be sufficient. As of now, the bare minimum hardware requirement to register in the network is:

- 16 dedicated CPU cores 
- 32GB of RAM
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection 

*as of July 25, 2022*



## Installing Bittensor


To begin, paste this script into your macOS Terminal or Linux shell prompt:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
```


You will be notified when the installation is complete, and the next step will be to create your keys.


## Creating your keys
### Creating your coldkey


Your coldkey remains on your device and holds your "cold storage". Currency in cold storage cannot be used for immediate activity in the network 


```
btcli new_coldkey
```


You will be prompted to name your wallet (which refers to the coldkey in this instance) and choose a password, before being provided with a unique mnemonic device. Record this information privately and securely.


#### Creating your hotkey


This key contains your "hot storage": currency that can be used for immediate activity in the network. Your coldkey can have multiple hotkeys attached to it,  while each hotkey can only be associated with one coldkey. 


```
btcli new_hotkey
```


You will be prompted to complete the same steps as with the last key, in addition to specifying which coldkey you would like to connect your hotkey to. 


## Running a miner



With your keys created, you can now run your miner. 


```bash
btcli run
```


You will be immediately prompted to: 


## Enter a network


To immediately gain access to Subtensor - our network blockchain - choose “nakamoto.” Nakamoto is useful for quick connections to the network like checking your wallet balance, however it is not reliable for mining. For serious miners we recommend running an instance of [Subtensor locally](cli/Subtensor.md) in order to maximize speed and connection. Should you be running Subtensor locally, choose “local.”

To familiarize yourself with the protocol without mining, choose our test network, [Nobunaga](https://www.notion.so/Nobunaga-Guide-caa0b84ae45840d6ae0eceacfa98d028).


## Enter your wallet

Enter the name of your coldkey and hotkey credentials. *note: your will need a separate hotkey for each miner you run.*


## Choosing a miner

From here, you may choose: ``core_validator/core_server``

Your miner is now running and solving the proof of work to register to the network. 
Registering on the network can take some time, depending on the calibre of your hardware. Please note that registration is CPU intensive, and GPU registration is not currently supported. Generally the more CPU power you have, the faster your will miner will become registered.

Once the proof of work is solved, your miner will automatically begin mining Tao.

Should your miner become deregistered, your miner will automatically begin the registration process again.

**Mining Tao is highly competitive so that only the best miners outfitted with the best models will do well. The challenge of optimizing your miner is the responsibility of the user.**
