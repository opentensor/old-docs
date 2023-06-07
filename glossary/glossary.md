
## Glossary



### Subnetworks
Self-contained economic markets incentivizing access to different forms of machine intelligence access, for instance; subnetwork 1 produces completions from text prompts and subnetwork 2 incentivizes the production of informationally dense embeddings from text. These economic domains are called "subnetworks".


### UIDS
The set of positions available in each [subnetwork](#subnetworks). UIDs increment like indices from 0 to the size of the network. i.e. 0 to 1023 for a 1024 sized subnetwork. UIDs can be owned by a wallet who has registered into the position within side each [subnetwork](#subnetworks).


### Miners
Computers which service requests described by the [`bittensor protocol`](#bittensor-protocol) via an Axon endpoint. [`Miners`](#miners) attempt to service the requests sent by [`validators`](#validators) to maximize their [`incentive`](#incentive) within a [`subnetwork`](#subnetworks)


### Validators
Computers holds [`TAO`](#tao) who verify the abilities of [`Miners`](#miners)  to perform the machine learning tasks required of their subnetwork. Validators run the continous process of validation in the classical machine learning train-test-validation process.


### Incentive
The proportion of [`emission`](#emission) a [`miner`](#miners)  recieves every [`epoch`](#epoch) across other [`miners`](#miners) within the subnetwork.


### Emission
The absolute number of tokens, usually measured in [`RAO`](#rao), a [`miner`](#miners) recieves every [`epoch`](#epoch).


### Epoch
The number of [`blocks`](#blocks) that progress between moments when [`Yuma consensus`](#yuma-consensus) is run and newly minted [`TAO`](#tao) are [`emitted`](#emission) into a [`subnetwork`](#subnetworks)


### Epoch Emission
The amount of [`TAO`](#tao) emitted into a [`subnetwork`](#subnetworks) on an [`epoch`](#epoch).


### RAO
The smallest denomination of [`TAO`](#tao). `1 TAO` is eqvuivalent to 100,000,000 [`RAO`](#rao).


### TAO
Bittensor unit of intelligence and value. TAO [`inflation`](#incentive) occurs continuously with block production.
The digital token that functions as currency in the network. Tao uses the same tokenomics as Bitcoin with a 4 year halving cycle and a max supply of 21 millions tokens.


### Blocks
Fundemental incremnets of state on [`subtensor`](#subtensor) Bittensors [`blockchain`](#blockchain). New block are created and added to the chain every 12 seconds.


### Subtensor
Bittensor's [`blockchain`](#blockchain) build on [`Polkadot`](#pol) blockchain infrastructure [`substrate`](#substrate)


### Substrate
An API build by [`Polkadot`](#polkadot) allowing the fast development of modular upgradable [`blockchains`](#blockchain).


### Polkadot
Polkadot is a blockchain platform and cryptocurrency. The native cryptocurrency for the Polkadot blockchain is the DOT. It is designed to allow blockchains to exchange messages and perform transactions with each other without a trusted third-party.


### Blockchain
A technology for building decentralized append only databases. Blockchains increase in size by appending blocks containing many [`extrinsics`](#extrinsics) which are unique function calls on the underlying state.


### Extrinsics
Functions called on a [`blockchain`](#blockchain) which append state and usually signed by a [`wallet`](#wallet)


### Bittensor Protocol
The over the wire encoding of requests and responses subscribed to by [`Miners`](#miners), [`validators`](#validators) and `clients` of the Bittensor network.


### Stake
Equivalent to the amount of [`Tao`](#tao) attached to the [`Miner's`](#miners) [`hotkey`](#hotkey). For [`Validators`](#validators), more [`stake`](#stake) translates to [`rankings`](#ranks) being worth more in [`Yuma Consensus`](#yuma-consensus).


### Weights
Vector lists of weights `w_i = [w_ij]` which are trained by [`validators`](#validators) while verifying the outputs of [`Miners`](#miners). The weights from all validators on a [`subnetwork`](#subnetworks) aggregate into a single matrix [`W`](#weights) over which [`Yuma Consensus`](#yuma-consensus) is run.
```python dark
subnet = bittensor.metagraph(1)
subnet.W
```


### Bonds
The moving average of the weights `B = alpha * W + (1 - alpha) * B`. Historical assessment of weights maintained on chain used for computing [`dividends`](#dividends).


### Ranks
The column sum of the weight matrix [`W`](#weights) representing each miner's stake weighted rating according to the validators withing a [`subnetwork`](#subnetworks).
```python dark
subnet = bittensor.metagraph(1)
subnet.R
```


### Trust
The average number of non-zero weights in the weight matrix [`W`](#weights) in a [`subnetwork`](#subnetworks)
```python dark
subnet = bittensor.metagraph(1)
subnet.T
```


### Consensus
The thresholded trust score via a shifted sigmoid activation. Miners with >50% [`trust`](#trust) have consensus values close to 1 and close to 0 otherwise.
```python dark
subnet = bittensor.metagraph(1)
subnet.C
```


### Incentive
Miner ranks shifted by consensus, `I = R * C`. Miners rate of inflation modulated by this term in the mechanism.


### Dividends
Proportion of emission passed to validators based on their share of [`Bonds`](#bonds) held in a miner based on the matrix `B`. `D = 0.5 * I * CB` where `CB` represents the normalized column sum of the bonds matrix ('temporal trust').


### Emission
Normalized sum of [`Incentive`](#incentive) and [`Dividends`](#dividends) multiplied by the [`epoch emission`](#epoch-emission), `E = 100,000,000 * I * D`. The amount of [`TAO`](#tao) emitted to each UID ever [`epoch`](#epoch).


### Yuma Consensus
The incentive mechanism detailed in the Bittensor Whitepaper around which [`emission`](#emission) is distributed.


### Miner/Neuron/Peer/Node
Used interchangeably to refer to a participant in the [`subnetwork.`](#subnetworks)


### Hotkey
The part of the miner that contains "hot storage". It is loaded into the network and gives ability to set weights (for Validators).


### Coldkey
The part of the miner that contains cold storage. Remains on device.


### Wallet
The logical pairing of one [`coldkey`](#coldkey) with 1 or more [`hotkeys`](#hotkey) for the separation of security layers within side Bittensor.


### Axon
Servers receive requests from other peers in the network via the [`dendrite`](#dendrite).


### Dendrite
Servers send requests to other peers in the network via the [`axon`](#axon).


### Metagraph
A Python torch object that produces a view into the network. This tool is used internally by [`Miners`](#miners)  and also for network analysis.


### Nakamoto
Bittensor current main blockchain network post-March 2023.


### Nakamoto
Bittensor's legacy network pre-March 2023


### Nobunaga
Bittensor's legacy test-network pre-March 2023


### Forward Requests
The first stage of the transaction in which a [`Validator`](#validators) sends a task a [`miner`](#miners) and the the [`miner`](#miners) sends task outputs back to the [`validator`](#validators)


### Backward Requests
The second stage of the transaction in which the [`Validator`](#validators) sends feedback (in the form of gradients or reward signal) to the [`miner`](#miners).


### Embeddings
Also referred to as representations, embeddings are a way of expressing information (i.e the comprehensible meaning of a word) as a very high-dimensional vector.


### Logits
The probability of a word in NTP (next token prediction) or MTP (masked token prediction).


### Next Token Prediction
Predicting an answer given a context before the place of prediction (i.e. predicting the next word in a sentence).


### Masked Token Prediction
Predicting an answer given a context before and after the place of prediction (i.e. predicting the next word in a sentence).


### Shapely Value
A measure of individuals' contributions in a cooperative game.


### Mountain Dataset
Bittensor uses a 1.5 Terrabyte corpus dataset for training known as the Mountain.


### Sigmoid Function
The sigmoid produces a threshold-like scaling that rewards connected peers and punishes the non-trusted.


### Chain Security
Connecting to the [`Polkadot`](#polkadot) infrastructure will offer greater network security. [`Polkadot`](#polkadot) takes the concept of validation security away from the chain so that the Polkadot relay chain is now responsible for security. Read more about [Polkadot security.](https://wiki.polkadot.network/docs/learn-security)




