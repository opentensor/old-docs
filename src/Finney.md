# Finney - Everything New




# Update your miners and restart them on the new Finney network

1. Do not transfer, stake, unstake, or perform chain operations on nakamoto, since these will not be reflected on the finney chain.

2. During the period between Nakamoto closing and Finney coming up, update all your bittensor repositories to the branch ``release/3.7.0``.

```bash
cd ~/.bittensor/bittensor
```
```bash
git fetch origin release/3.7.0
```
```bash
git checkout release/3.7.0
```
```bash
cd ..
```
```bash
python3 -m pip install -e .
```

3. Run SubtensorV3

```bash
git clone https://github.com/opentensor/subtensorv3.git
```
```bash
cd subtensorv3
```
```bash
docker compose up -d
```

4. Once your Bittensor release/3.7.0 branch is properly installed and you have SubtensorV3 running, you can prepare your Servers and Validators to connect into the Finney chain. The command to run your Servers and Validators is entirely the same with the exception of the command line argument ``net.uid <>``. At ~5pm EST we will open Finney and you will be able to re-run your Server and Validator commands (as normal with the additional ``--net.uid <>`` argument). If you had a registered miner on the previous Nakamoto network it will still be registered, with stake on the Finney chain on sub-network 3. Your axon-ip endpoint will update automatically when running the miner.

For example, if your mining script is normally:

```bash
btcli run
```

It becomes:

```bash
btcli run --net.uid 3
```

Net UID 3 is the only available network at this time.

5. Over the next 48 hours registrations will be turned off on Finney, giving all miners on the previous network time to begin their Servers/Validators and time for the incentive mechanism to re-stabilize. Devs will be avialable to help people bridge this period on the official Bittensor discord.

# StakePruningMin

The StakePruningMin hyperparemter, which provided deregistration immunity to any key above 1024 stake now only protects the 128 highest staked keys.

# Delegating

Delegation introduces a new way for miners to stake Tao to support the network's most honest and innovative Validators. Any hotkey may nominate themselves as a delegate and receive stake delegations from other wallets in the network. Key owners of delegates collect an 18% "take" on emissions of all delegated Tao.
Learn more [here](Delegation.md)
## Turn your hotkey into a delegate
```bash
btcli nominate
```
## Stake to a delegate account
```bash
btcli delegate
```
## List all the delagates in the network
```bash
btcli list_delegates
```
## Show who you are delegating to
```bash
btcli my_delegates
```

# Recycle Registration

A hotkey may now decide between registering through the proof of work or through the ``recycle_register`` mechanism, which charges a hotkey a fee paid in Tao. "Recycle register" Tao fees are recycled by adding to the end of the 21 million supply. Like the proof of work, the ''recycle_register`` fee is dynamic with demand to enter the network.

## Recycle to register with Tao

```bash
btcli recycle_register
```

# Specifying subnetworks

While the Finney upgrade will not introduce any new subnetworks intially, they are on the horizon. Miners need to specify which subnetwork they are mining or registering on with ``--net.uid`` or by following the user interface prompts.

For example, run on subnetwork 1:

```bash
btcli run --net.uid 1
```