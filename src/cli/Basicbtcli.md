# Basic btcli
---
Before you begin customizing your Miner to optimize your currency accrual, it is useful to familiarize yourself with our``btcli`` commands. Btcli is a command line interface to interact with Bittensor, and commands are used to monitor Miner performance, transfer Tao, and regenerate keys. 


​
## Monitoring 
​

For an overview of all possible btcli commands, enter: 


```bash
btcli help
```


Both the "overview" and "inspect" commands are used to monitor your miner performance: 


```bash
btcli overview 
```


This command will display the specifics of your progress in the network, and includes your UID, state (active or inactive), [stake](src/../Glossary.md#stake), [rank](src/../../nested/Glossary.md), [trust](src/../../nested/Glossary.md#trust), [consensus](src/../../nested/Glossary.md#consensus), [incentive](src/../../nested/Glossary.md#incentive), [dividends](src/../../nested/Glossary.md#dividends), and [emission](src/../../nested/Glossary.md#inflation). For more information about these performance indicators, refer to the ["Consensus Mechanism"](../nested/Mechanisms.md) section.


```bash
btcli inspect 
```
​

This command will not display such a detailed analysis of your performance, but will allow you to see your key identifiers, fingerprints, network, balance, stake, and emission. 
​

For a complete list of all created keys, run: 


```bash
btcli list
```


## Transferring Tao
​

The 'unstake' command will transfer Tao from a hotkey to your coldkey. 


```bash​
btcli unstake
```
​

The transfer Tao from your coldkey to your hotkey, enter: 


```bash​
btcli stake 
```
​


To expedite longer staking and unstaking operations, you can string these flags to ``btcli stake`` and ``btcli unstake``:
```bash
#stake or unstake from all hotkeys
--wallet.all_hotkeys 
#stake or unstake from a specific set of hotkeys
--wallet.hotkeys
#stake or unstake from all hotkeys while exluding a specific set of hotkeys
--wallet.exclude_hotkeys
#stake or unstake to a specific amount of stake on a hotkey
--max_stake
```
​


This command moves Tao between coldkeys. A .125 tao burn fee is applied.


```bash​
btcli transfer
```



## Key Regeneration
​

If you lose access to your keys, they can be easily regenerated with the unique mnemonic device you were provided with upon initial creation. 


```bash​
btcli regen_coldkey
```



```bash
btcli regen_hotkey
```
