# Delegation and Staking

Bittensor Tao can be either delegated or staked to a validator. Both staking and delegation involve transferring Tao from a Coldkey to a Hotkey. When Staking, users stake Tao to a Hotkey that belongs to them. On the other hand, when delegating their Tao users are staking Tao to a hotkey that does not belong to them for a fee to the hotkey owner. However, this removes the need to run their own Validators and allows them to support projects building on the Bittensor network.

## Staking
Staking Tao is effectively moving Tao from your Coldkey to your Hotkey. Running your Validator on your Hotkey and then staking your Tao to it from your Coldkey will translate to its rankings on the network being more prioritized over other Validators with less stake. If instead you staked your Tao to your Neuron, then this would lower the likelihood of it being deregistered from the network.

To stake to your validator, simply call the following:

```bash
btcli stake 
```
It is also possible to view all the possible commands using `btcli stake --help`.

## Delegation
Delegation allows for all users to participate in Bittensor’s consensus mechanism. By delegating Tao to a Validator, users are able to earn back Tao proportional to their contribution. Users are incentivized to delegate to a Validator based on the project that Validator is proposing. For example, a Validator can propose to validate and research image-to-text models. Users interested in image-to-text models on the Bittensor protocol are then encouraged to delegate Tao to that Validator to fund it with Tao. Hence, delegation is effectively a funding mechanism for projects on top of Bittensor.

By default, the delegates collect an 18\% share of all emissions from delegated TAO. The delegate validators must perform better than their peers to remain competitive while promoting growth and quality in the network. Delegation facilitates resource utilization, creating more powerful nodes and enhancing the network's innovative potential.

When delegating, users stake their Tao to a Hotkey belonging to a third-party Validator on the Bittensor network. This removes the need for users to provision their own hardware and deploy their own Validator. Instead, the delegating Hotkey will be responsible for validation and will provide any bond-emissions returns to the staking user's Coldkey, minus the 18\% fee. 

> NOTE: The delegation fee is presently a hard coded fee that is subject to change as the network evolves.

For users to nominate their Hotkey as a Delegate, simply call the following and follow the steps:

```bash
btcli nominate
```

To delegate to a Validator Hotkey:

```bash
btcli delegate
```
This will display a list of delegates along with information such as a description of their project, the earnings stats, and other pertinent data. 