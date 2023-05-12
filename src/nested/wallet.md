# Create a Wallet

Your Bittensor wallet is your tool to interact with the Bittensor network. It helps  hold your Tao and to interface with the different APIs run by application running on top of Bittensor. 

Wallets on Bittensor consist of a coldkey and a hotkey. A Coldkey can contain many Hotkeys, whereas a Hotkey can only belong to one Coldkey. A Coldkey is meant to store funds securely and thus cannot be used to sign the extrinsic operations needed to participate in validation. Hotkeys, on the other hand, are meant to sign extrinsic operations like registration, staking, unstaking, and delegation. 

# Using BTCLI

Let’s create a wallet — or Coldkey — with one Hotkey associated with it. 

1. First, create a new coldkey by pasting the following command to your terminal and following the steps.

```bash
btcli new_coldkey
```

2. Now, similarly create a new hotkey and ensure to specify your wallet name used in the previous step when creating it.

```bash
btcli new_hotkey
```

3. If you lose your password to your wallet, you can always regenerate the coldkey using the mnemonic you saved in step 1. You can similarly use `btcli regen_hotkey` to regenerate your hotkey using the mnemonic you saved in Step 2.

```bash
btcli regen_coldkey
```

# Using the Bittensor Website

Simply navigate to [Bittensor](http://bittensor.com) and click the `0.00` at the top right corner. 

![Bittensor Wallet UI](images/wallet.png)

Click `create` to create a brand new wallet, or `import` to import your mnemonic from an existing wallet. Finally, click `Access` to Send, Receive, or Stake your Tao.