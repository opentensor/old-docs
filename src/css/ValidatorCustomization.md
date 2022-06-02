# Validator Customization

Running a Validator becomes beneficial only once you have accrued a significant amount of Tao. This is due to the bonding matrix: Validators accrue currency in proportion to their stake due to the existence of dividends.  This beneficial tipping point occurs at around ~1000 Tao. 
​

In addition, Validators are less sensitive to disconnection compared to Servers, who's incentive will begin falling within 20 minutes of disconnection (100 blocks). Validators, however, will only become inactive after 5000 blocks. 

Any registered hotkey can be used to run a Validator, and it is as simple as running this code: 

```bash
python3 -u ~/.bittensor/bittensor/bittensor/_neuron/text/core_validator/main.py --no_prompt --subtensor.network local --wallet.name <> --wallet.hotkey <>
```


## Optimizing Size 
​

The following configuration condenses a Validator to 8 gigs of RAM: 
```bash
--nucleus.topk 20 --nucleus.nlayers 1
```


## Optimizing Traffic 
​

There are 4096 nodes available in the network, but each Validator can only query a section of the network at a time. By using the "nucleus.topk" argument, however, you can changes the number of peers that your Validator will query per remote forward call to the network. By default, this "traffic" dimension is set to 20, but with good hardware, increasing this dimension can improve your earnings, though it is recommended not to use higher than 50. 

```bash
--nucleus.topk
```


## Optimizing Layers 
​

This is another way to increase power - and therefore earning potential - given adequate hardware: increase the layers of your model. 
​
```bash
--nucleus.nlayers
```
​

## Optimizing Importance 
​

This metric determines how "risk averse" your Validator will be in choosing who to send requests to. With a high importance parameter, validators will query more peers, without regard for how known they are to the network. With a low importance parameter, validators will take the safest route - querying mostly known peers in the system. This parameter is set to 3 by default, and it is not recommended to go above 10. 
​
```bash

```


## Staking Tao
​

If you are running a Validator, the more Tao you have staked in your hotkey, the more inflation through dividends you will earn. Refer to basic btcli to see the commands for transferring Tao. 
​