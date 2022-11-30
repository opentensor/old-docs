# Preparing your miner

Once your miner is registered in the network and you have Subtensor running locally, your basic setup is complete. Your miner will begin processing data, generating value for the network, and accruing Tao. 


This area of the documentation will guide you through the basic customizations that can be made to your miner with flags in order to set your miner up for success in the network. *Pair these flags with calls to ``btcli`` or any other mining start command.*

You may also configure your miner through a config file or environment variables. See [Methods of Configuration](ConfigurationMethods.md) and [Configuration Settings](../Arguments.md) for more.


## Choosing your hardware


To run with GPU or CPU:


```bash
--neuron.device <cuda | cpu>
```




## Choosing a network 


This argument specifies which instance of Subtensor you will connect to: a local copy, the public Nakamoto copy, or the test network Nobunaga. 


```
--subtensor.network <local | nakamoto | nobunaga>
```


You can also select a network endpoint: 


```bash
--subtensor.chain_endpoint <>
```


## Specifying a wallet 


Every running miner must be connected to a registered hotkey. This code will specify which coldkey (wallet) you wanted to use, as well as the corresponding hotkey. 


```bash
--wallet.name <>
```


```bash
--wallet.hotkey <>
```


## Specifying a port 


Specifying a port to which to access the network is important because you will benefit from entering a low traffic area. This will generally be one above 1024 and below 65535. Each miner needs to have a unique port, so if you have two miners running on the same machine, they will require two separate ports.
 

The miner communicates with the network through its communication endpoint, the axon. This is where the argument is made. 


```bash
--axon.port <>
```
ex.
```bash
--axon.port 8090
```



## Restarting you miner 


Only use this argument when if wish to restart your training from the beginning. This will reset all training progress. 


```bash
--neuron.restart
```


## Different ways to start a miner

*This is for advanced or power users of Bittensor*

Sometimes you may want to create your own validator or your own server, in which case btcli will not work as it is pointed at specific files within the Bittensor repository. The following commands demonstrate how to run your own custom script along with the same Bittensor flags. Note that the path of the script that the command examples are using are the same ones that btcli uses currently.

```bash
python3 -u ~/.bittensor/bittensor/bittensor/_neuron/text/<core_server | core_validator>/main.py --no_prompt --subtensor.network local --wallet.name <> --wallet.hotkey <>
```

Process managers like [PM2](https://pm2.keymetrics.io/docs/usage/pm2-doc-single-page/) and [TMUX](https://github.com/tmux/tmux/wiki) are another option, however since they are not a part of Bittensor, they will not be a part of this documentation.
