# Glossary


## Miner Architecture 
​

**Miner/Neuron/Peer/Node**

Used interchangeably to refer to a participant in the network. 
​

**Hotkey**

The part of the miner that contains "hot storage". It is loaded into the network and gives ability to set weights (for Validators). 
​

**Coldkey**

The part of the miner that contains cold storage. Remains on device.
​

**Axon**

Miners receive requests from other peers in the network via the axon.
​

**Dendrite** 

Miners send requests to other peers in the network via the dendrite. 
​

**Metagraph**

A Python torch object that produces a view into the network. This tool is used internally by miners and also for network analysis. 

---
# Network 


## Tao 

The digital token that functions as currency in the network. 
​

**Subtensor**

The network blockchain. 
​

**Nakamoto** 

Our main network. 
​

**Nobunagu** 

Our test network. 
​

**Block step** 

Occurs every 12 seconds. The blockchain is updated, and newly minted Tao is distributed to the system. 
​

**UID** 

The unique identifying number for each Miner. Represents its position in the network. There are currently 4096 UID's available in the network. 
​

**Forward Requests** 

The first stage of the transaction in which a Validator sends data to a Server in the form of tokens, and the the Server sends embeddings back. 
​

**Backward Requests**

The second stage of the transaction in which the Validator sends feedback (in the form of gradients) to the Server.

---

## Consensus Mechanism


**Stake**

Equivalent to the amount of Tao attached to the Miner's hotkey. For Validators, more stake translates to rankings being worth more. For Servers, more stake translates to a lower likelihood of being deregistered from the network. 
​

**Rank**

The raw score given to a Server by a Validators, combined with the Stake of the Validator. 
​

## Trust

This score represents the number of non-zero (approval) rankings that Servers receives from Validators. The trust score is used to determine whether a Server has achieved consensus in the network. The more stake a Validator has, the more trust scores it can distribute. 
​

## Consensus


Achievement of a Server who has received a non-zero ranking from more than 50% of the stake in the network. Servers who reach consensus receive significantly higher rewards than those who have not. 
​

**Incentive** 

The inflation achieved by a Server before dividends are distributed. The incentive is a combination of the rank and consensus scores. 
​

**Inflation**

The amount of currency (1 tao) released into the network at each block step. The single Tao is distributed amongst all peers in the network according to their performance.
​

**Emissions**

Refers the portion of the one Tao distributed to a single peer each block step.

​
**Dividends**

When Validators rank Servers, they take on part ownership of them through the bonding matrix. When a Server's incentive is calculated, a portion of this is distributed to Validators who have bonds.

​
## Bonding Matrix

Refers to the bonds that Validators hold in Servers. The higher the stake the Validator has, and the more staked in the Server, the larger the dividend the Validator will receive. 
​
​