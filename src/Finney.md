# Finney - Everything New




# Update your miners and restart them on the new Finney network


1. Pull the latest master and install.

```bash
git -C ~/.bittensor/bittensor pull origin master
python3 -m pip install -e ~/.bittensor/bittensor
```

2. Restart your miners

A simple stop and start will do.

# StakePruningMin

The StakePruningMin hyperparemter, which provided deregistration immunity to any key above X amount of Tao now only applies to the 100 highest staked keys.

# Delegating

Delegation introduces a new way for miners to stake Tao to support the most honest and inovative Validators in the network. Any hotkey may nominate themselves as a delegate and receive stake delegations from other wallets in the network. Key owners of delegates collect an 18% "take" on emissions of all delegated Tao.
Learn more [here](Delegation.md)


## Turn your hotkey into a delegate:
```bash
btcli nominate
```
## Stake to a delegate account:
```bash
btcli delegate
```
## List all the delagates in the network
```bash
btcli list_delegates
```

# Recycle Registration

A hotkey may now decide between registering through the proof of work or through the ``recycle_register`` mechanism, which charges a hotkey a fee paid in Tao. "Recycled register" Tao fees are recycled by adding to the end of the 21 million supply. Like the proof of work, the ''recycle_register`` fee is dynamic with demand to enter the network.

## Pay to register with Tao

```bash
btcli recycle_register
```

# Specifying subnetworks

While the Finney upgrade will not introduce any new subnetworks intially, they are on the horizon. Miners need to specify which subnetwork they are mining or registering on with ``--net.uid`` or by following the user interface prompts.

For example, mine to subnetwork 1:

```bash
btcli run --net.uid 1
```