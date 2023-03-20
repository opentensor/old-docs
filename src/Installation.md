# Getting started

This section will guide you through the basic steps necessary to run a miner in the Bittensor network. Considering the rapid expansion of - and competition within - the network since its launch in November 2021, registration difficulty is constantly shifting and there is no guarantee that the same caliber of hardware will always be sufficient. As of now, the bare minimum hardware requirement to register in the network is:

- NVIDIA GPU
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection

To run a functional Server:

- NVIDIA GPU 
- 8GB of VRAM
- 32 GB of RAM
- 200GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection

To run a Validator:

- 16 dedicated CPU cores
- 16 GB of RAM
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection 

*as of March 20, 2023*
*these requirements are subject to increase*



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
