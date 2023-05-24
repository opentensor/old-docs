# Getting Started

All interaction with Bittensor involve wallets. These are the core ownership and identity technology around which all functions on Bittensor are carried out. For instance, holding or transferring TAO, accessing Bittensor directly to extract knowledge, mining and validating. Before creating wallets, you will need to install the bittensor API. Note, if you just want to create a wallet to hold TAO you can use the website [here](#website-wallet)

There are three primary ways to install Bittensor on your local machine: 
1. Using the installer script. This is the easiest method and is recommended if you are new. Simply paste the following into your terminal.

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
    ```

2. Using pip.

    ```bash
    pip3 install bittensor
    ```

3. From source.

    ```bash
    git clone https://github.com/opentensor/bittensor.git
    $ python3 -m pip install -e bittensor/
    ```

Once installed, you can verify your installation by running the [Bittensor Command Line Interface](/documentation/btcli) (CLI) with ```btcli --help``` and/or check your installation in python.
```python
import bittensor as bt
```

# Wallets.
Bittensor wallets consists of a coldkey and hotkey, a pairing of two separate cryptographic keypairs which are responsible for different functions within the Bittensor ecosystem. Coldkeys store funds securely and perform high risk operation such as transfers and staking, while hotkeys are used for less secure operations such as signing messages into the network, running miners, and validating the network. You can create wallets using the Bittensor API in two ways.

1. Using the python-api
```python
import bittensor as bt
wallet = bt.wallet( name = 'my_coldkey', hotkey = 'my_first_hotkey' )
wallet.create_new_coldkey()
wallet.create_new_hotkey()
print (wallet)
"Wallet (my_coldkey, my_first_hotkey, ~/.bittensor/wallets/)"
```

2. Or using btcli
```bash
$ btcli new_coldkey --wallet.name my_coldkey
    IMPORTANT: Store this mnemonic in a secure (preferably offline place), as anyone who has possesion of this mnemonic can use it to regenerate the key and access your tokens. 
    The mnemonic to the new coldkey is:
    **** *** **** **** ***** **** *** **** **** **** ***** *****
    You can use the mnemonic to recreate the key in case it gets lost. The command to use to regenerate the key using this mnemonic is:
    btcli regen_coldkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****

$ btcli new_hotkey --wallet.name my_coldkey --wallet.hotkey my_first_hotkey
    IMPORTANT: Store this mnemonic in a secure (preferably offline place), as anyone who has possesion of this mnemonic can use it to regenerate the key and access your tokens. 
    The mnemonic to the new hotkey is:
    **** *** **** **** ***** **** *** **** **** **** ***** *****
    You can use the mnemonic to recreate the key in case it gets lost. The command to use to regenerate the key using this mnemonic is:
    btcli regen_hotkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****
```
When creating wallets you can specify the name of the coldkey and hotkey. The above commands used the names ```my_coldkey``` and ```my_first_hotkey``` which will create a directory containing your wallets inside bittensor's root directory ```~/.bittensor/wallets/```. You can view this directory using the cli via ```btcli list```.

```bash
$ tree ~/.bittensor/
    .bittensor/                         # Bittensor, root directory.
        wallets/                        # The folder containing all bittensor wallets.
            my_coldkey/                 # The name of your wallet, "my_coldkey"
                coldkey                 # Your encrypted coldkey.
                coldkeypub.txt          # Your coldkey public address
                hotkeys/                # The folder containing all of your hotkeys.
                    my_first_hotkey     # You unencrypeted hotkey information.
```

Be sure to store your mnemonics safely when generating your keys. If you lose the password to your wallet, or the access to the machine where the wallet is stored, you can always regenerate the coldkey using the mnemonic you saved from above.
```bash
btcli regen_coldkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****
```

# Website Wallet

To create a wallet without installing bittensor, simply navigate to [Bittensor](http://bittensor.com) and click the `0.00` at the top right corner. Select `create` to create a new wallet or `import` to import your mnemonic from an existing wallet. The "access" option can be used if you have already created a wallet using the website and have not chosen to "forget" it. Once you have accessed your account, you can send, receive, or stake your TAO. 
