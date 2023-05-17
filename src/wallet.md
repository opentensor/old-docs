# The Wallet

The Bittensor wallet is a crucial tool for interacting with the network: it can be used to hold TAO and to interface with applications connected to the network. 

Each wallet consists of a coldkey and hotkey. A coldkey may contain many hotkeys, while each hotkey can only belong to a single coldkey. Coldkeys store funds securely, while hotkeys are used for all extrinsic operations such as registration, staking, unstaking and delegation.

# Using BTCLI

1. To create a coldkey, paste the following command into your terminal: 

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

Select `create` to create a new wallet or `import` to import your mnemonic from an existing wallet. The "access" option can be used if you have already created a wallet using the website and have not chosen to "forget" it. Once you have accessed your account, you can send, receive, or stake your TAO. 
