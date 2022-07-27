# Customizing your miner - Validator
---
The Core Validator finetunes on the bittensor network with a mixture of experts model and shapely scoring. The Validator's main jobs are to identify important/useful peers in the network and to correctly weight them. To achieve this, the Validator will send requests to different peers on the network and evaluate their responses.


Running a Validator becomes beneficial only once you have accrued a significant amount of Tao. This is due to the [bonding matrix](src/../Glossary.md#bonding-matrix): Validators accrue currency in proportion to their stake due to the existence of dividends. Validators typically need at least 700 Tao to stay registered on the network, however the minimum Validator stake is subject to change.


In addition, Validators are less sensitive to disconnection compared to Servers, who's incentive will begin falling within 20 minutes of disconnection (100 blocks). Validators, however, will only become inactive after ~5000 blocks. 



## Running a Validator


Any registered hotkey can be used to run a Validator, and it is as simple as running this command: 

```bash
btcli run
```
Choose ``core_validator``


## Optimizing traffic 


There are 4096 nodes available in the network, but each Validator can only query a section of the network at a time. By using the "nucleus.topk" argument, however, you can changes the number of peers that your Validator will query per remote forward call to the network. By default, this "traffic" dimension is set to 20, but with good hardware, increasing this dimension can improve your earnings, though it is recommended not to set higher than 50. 


```bash
--nucleus.topk <>
```



## Optimizing layers 


This is another way to increase power - and therefore earning potential - given adequate hardware: increase the layers of your model. 


```bash
--nucleus.nlayers <>
```

## Optimizing Importance 


This metric determines how "risk averse" your Validator will be in choosing who to send requests to. With a high importance parameter, validators will query more peers, without regard for how known they are to the network. With a low importance parameter, validators will take the safest route - querying mostly known peers in the system. This parameter is set to 3 by default, and it is not recommended to set above 10. 


```bash
--nucleus.importance <>
```



## Staking Tao


If you are running a Validator, the more Tao you have staked in your hotkey, the more inflation through dividends you will earn. Refer to [Wallet](../cli/Basicbtcli.md) to see the commands for transferring and staking Tao. 