# Preparing your Miner

Once your Miner is registered in the network you and have Subtensor running locally, your basic setup is complete. Your Miner will begin processing data, generating value for the network, and accruing Tao. 
​

This area of the documentation will guide you through the basic customizations that can be made to your Miner in the form of "arguments," in order to set your Miner up for success in the network.
 
​

## Choosing your Hardware
​

While the current network parameters typically do not demand the computational power of a GPU, larger models may. 
​

To run with GPU:


```bash
--neuron.device cuda
```


To run with CPU: 
```bash
--neuron.device cpu
 ```



## Choosing a Network 
​

This argument specifies which instance of Subtensor you will connect to: a local copy, the public Nakamoto copy, or the test network Nobunaga. 
​

```
--subtensor.network 
```


You can also select a network endpoint: 
​

```bash
--subtensor.chain_endpoint
```
​

## Choosing a Wallet 
​

Every running miner must be connected to a registered hotkey. This code will specify which hotkey you wanted to use, as well as the corresponding coldkey (wallet). 
​

```bash
--wallet.name 
```


```bash
--hotkey.name
```


## Choosing a Port 
​

Specifying a the port to access the network by is important because you will benefit from entering in a low traffic area. This will generally be one above 1024 and below 65535. Each miner needs to have a unique port, so if you have two miners running on the same machine, they will require two separate ports.
 
​
The miner communicates with the network through its communication endpoint, the axon. This is where the argument is made. 
​

```bash
--axon.port
```
​ex.
```bash
--axon.port 8090
```



## Restarting you Miner 
​

Only use this argument when you wish to start your Miner from the beginning. This will delete all progress. 
​

```bash
--neuron.restart
```
