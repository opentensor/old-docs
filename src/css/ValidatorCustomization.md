# Customizing your miner - Validator
---
The Core Validator finetunes on the bittensor network with a mixture of experts model and shapely scoring. The Validator's main jobs are to identify important/useful peers in the network and to correctly weight them. To achieve this, the Validator will send requests to different peers on the network and evaluate their responses.


Running a Validator becomes beneficial only once you have accrued a significant amount of Tao. This is due to the [bonding matrix](../nested/Glossary.md#bonding-matrix): Validators accrue currency in proportion to their stake due to the existence of dividends. Validators typically need 1024 Tao to stay registered on the network, however the minimum Validator stake is subject to change.


In addition, Validators are less sensitive to disconnection compared to Servers, who's incentive will begin falling within 20 minutes of disconnection (100 blocks). Validators, however, will only become inactive after ~5000 blocks. 



## Running a Validator


Any registered hotkey can be used to run a Validator, and it is as simple as running this command: 

```bash
btcli run
```
Choose ``core_validator``



## Staking Tao


If you are running a Validator, the more Tao you have staked in your hotkey, the more inflation through dividends you will earn. Refer to [Wallet](../cli/Basicbtcli.md) to see the commands for transferring and staking Tao. 
