# Getting started

This section will guide you through the basic steps necessary to run a miner in the Bittensor network. Considering the rapid expansion of - and competition within - the network since its launch in November 2021, registration difficulty is constantly shifting and there is no guarantee that the same caliber of hardware will always be sufficient. As of now, the bare minimum hardware requirement to register in the network is:

- NVIDIA GPU
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection 

To run a competitive Server:

- NVIDIA GPU 
- 8GB of VRAM
- 32 GB of RAM
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection 

To run a Validator:

- 16 dedicated CPU cores
- 16 GB of RAM
- 100GB of disk space
- Ubuntu LTS releases or Macintosh 
- A good and stable internet connection 

*as of August 23, 2022*



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


## Registering a hotkey

Before you can begin mining Tao, you must first register a hotkey to the network by solving the proof of work (POW). The Bittensor network is comprised of 4096 miners, and each time a new hotkey is registered to the network, the lowest ranked miner is kicked off of the network. Unless otherwise specified, registration will utilize your CPU, however, a GPU is often a minimum requirement to register depending on the current difficulty.

## Registering with a GPU

Before you can utilize the CUDA registration, you must first install CUDA-toolkit and cubit. Please note that CUDA registration only supports sm_86 enabled CUDA GPU (30XX series, Axxxx series or higher) Other GPUs may require additional configuration for registration.

### Installing CUDA-toolkit

Install [CUDA-toolkit 11.3](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local) or higher in accordance with your operating system and version if you have yet to do so. deb(local), deb(network), and runfile(local) should each be sufficient installer types.

<img src="toolkit.png" width="66%" height="66%" />


### Enter the Bittensor directory

```bash
cd ~/.bittensor/bittensor
```

### Install cubit

```bash
pip install -e .[cubit]
```

### Troubleshooting and testing

Should the previous installation fail, you may install from source or the wheel: [cubit installation](https://github.com/opentensor/cubit/#install)

You can check if your GPU is being seen through torch:
```python
python3
>>> import torch
>>> torch.cuda.is_available()
```

A quick way to test if the GPU registration process is working properly is by choosing the test network, Nobunaga, upon the miner startup described below. Registration to the Nobunaga network should only take a few minutes. Additional configurations may optimize your registration speed. Please see [here](Arguments.md#cuda) for a full list of CUDA registration flags.

With your keys created and CUDA registration installed, you can now run your miner. 

```bash
btcli run --cuda
```

You will be immediately prompted to: 


## Enter a network


To immediately gain access to Subtensor - our network blockchain - choose “nakamoto.” Nakamoto is useful for quick connections to the network like checking your wallet balance, however it is not reliable for mining. For serious miners we recommend running an instance of [Subtensor locally](cli/Subtensor.md) in order to maximize speed and connection. Should you be running Subtensor locally, choose “local.”

To familiarize yourself with the protocol without mining, choose our test network,Nobunaga


## Enter your wallet

Enter the name of your coldkey and hotkey credentials. *note: you will need a separate hotkey for each miner you run.*


## Choosing a miner

From here, you may choose: ``core_validator/core_server``

Should your miner become deregistered, your miner will automatically begin the registration process again.

**Mining Tao is highly competitive so only the best miners outfitted with the best models will do well. The challenge of optimizing your miner is the responsibility of the user.**

## [Learn more about optimizing a Server](css/ServerCustomization.md)
