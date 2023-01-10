# Delegation

*~this feature is only available on the finney branch. Refer [here](https://www.notion.so/Finney-How-to-test-5abffaaf28934f4a88c615c72d9bf083) to learn how to test the finney branch.*

Any hotkey may become a delegate and receive nominations of stake from other wallets in the network. Key owners of delegates collect an 18% "take" on emissions of all delegated Tao.

When a coldkey creates a hotkey delegate, it will receive all of the emissions from the stake it adds to its hotkey delegate. The delegate owner will also collect 18% of the emissions from all delegated stake.

## Turn your hotkey into a delegate:
```
btcli nonminate
```

## Stake to a delegate account:
```
btcli delegate
```

## List all the delagates in the network
```
btcli list_delegates
```



**E** = emissions earned by the key per block

**Sn** = Stake from owner

**St** = Total stake on hotkey

**Delegate key owner**

Emissions received = **E** * **0.18**+(**Sn**/**St**)*(**E**-**E** * **.18**)

*~delegates receive an 18% tax*

**Delegated stake owners**

Emissions received = (**Sn**/**St**)*(**E**-**E** * **.18**)

*~delegated stake owners pay an 18% tax through emissions*

