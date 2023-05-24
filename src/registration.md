# Registration

Prior to participating in the Bittensor network as a miner or a validator you must attain a slot within one of bittensor's sub-networks called a UID. Each subnetwork contains a limited set of UIDs, at the time of writing, 1024 on subnetwork 1 and 4096 on subnetwork 3, into which miners and validators must register into before they are considered eligible to accumulate TAO in any fashion, or validate knowledge production.

Since UIDS are the prerequisite for individuals to participate in Bittensor's economoy and are limited in number, they fill up fast through continuous registrations. At this point older underperforming miners (ranked via rate of reward 'emission') are dropped from the network based on performance each time a new hotkey is registered to the subnet. The process of registering a miner is competitive, and uses two mutually adaptive method to determine the price to entry, both cases, requiring a ```--netuid`` parameter which specifies which subnetwork the miner is entering, those are:

1. Via proof of work based registration (cost in compute)
      ```bash
      btcli register --netuid SELECTED_NETUID --wallet.name YOUR_COLDKEY --wallet.hotkey YOUR_HOTKEY
      ```
2. Via recycling registration (cost in TAO)
      ```bash
      btcli recycle_register --netuid SELECTED_NETUID --wallet.name YOUR_COLDKEY --wallet.hotkey YOUR_HOTKEY
      ```

The proof-of-work method of registration is recommmended for miners contributing raw compute power to bittensor and are seeking a method of attaining a slot without token supply. Whereas, recycle based registrations are recommended for anyone seeking to attain slots and already have a small amount of TAO at their disposal. NOTE: If you opt for a POW registration it is suggested that you use a Nvidia GPU to register for a faster hash rate. To do this, you must [install Cubit](https://github.com/opentensor/cubit).

Once a miner or validator has registered UID it is thiers to mine under however it is important to move quickly since this UID can be taken after a shot period if the miner does not accumulate value in under the mechanism. To view your uid and its performance you can run ```btcli overview```. Some example outputs of running that command can be seen below with summary descriptions, however, to read a more involved description of each term presented in the above chart, see yuma consensus.                   

| Parameter         | Value | Description |
| :---------------- | :------: | ----: |
| COLDKEY        |   my_coldkey   | The name of the coldkey associated with the won slot. |
| HOTKEY      | my_first_hotkey      |    The name of the hotkey associated with the won slot.                          |
| UID         | 5                    |    The index of the uid out of available uids.                                   |
| ACTIVE      | True                 |    Whether or not the uid is considered active.                                  |
| STAKE(τ)    | 71.296               |    The amount of stake on this miner.                                            |     
| RANK        | 0.0629               |    This miner's absolute ranking according to validators on the network.         |
| TRUST       | 0.2629               |    This miner's trust as a proportion of validators on the network.              |
| CONSENSUS   | 0.89                 |    This miner's aggregate consensus score.                                       |
| INCENTIVE   | 0.029                |    This miner's incentive, TAO emission attained via mining.                     |
| DIVIDENDS   | 0.001                |    This miner's dividends, TAO emission attained via validating.                 |
| EMISSION    | 29_340_153           |    This miner's total emission in RAO ( 10^-9 TAO ) per block.                   |
| VTRUST      | 0.96936              |    This validators trust score as a validator.                                   |
| VPERMIT     | *                    |    Whether this miner is considered active for validating on this subnetwork.    |
| UPDATED     | 43                   |    Blocks since this miner set weights on the chain.                             |
| AXON        | 131.186.56.85:8091   |    The entrypoint advertised by this miner on bittensor blockchain.              |
| HOTKEY_SS58 | 5F4tQyWr...          |    The raw ss58 encoded address of the miner's hotkey.                           |