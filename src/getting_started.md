# Getting Started

All interactions with Bittensor involve wallets which are the core ownership and identity technology around which all functions on Bittensor are carried out. For instance, holding or transferring TAO, querying Bittensor, mining or validating. Before creating a wallet, you will need to install the Bittensor API. Note, if you just want to create a wallet to hold TAO you can use the website [here](#website-wallet). There are also other ways of generating the underlying keys that bittensor uses, for instance, via [subkey](https://docs.substrate.io/reference/command-line-tools/subkey/)

# Installation
There are three primary ways to install Bittensor on your local machine: 
1. Using the installer script. This is the easiest method and is recommended if you are new to coding as it will pre-install the requirements like python if they are not already present on your machine. To run the installer, simply paste the following into your terminal.

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
    ```

2. Using pip.
    ```bash
    pip3 install bittensor
    ```

3. Or from source.
    ```bash
    git clone https://github.com/opentensor/bittensor.git
    $ python3 -m pip install -e bittensor/
    ```

Once installed, you can verify your installation by running the [Bittensor Command Line Interface](using_btcli.md) (btcli) with ```btcli --help``` and/or check the installation in python.
```python
import bittensor as bt
print( bt.__version__ )
```

# Wallets.
Bittensor wallets consists of a ```coldkey``` and ```hotkey```, a pairing of two separate [EdDSA cryptographic keypairs](https://en.wikipedia.org/wiki/EdDSA#Ed25519) which are responsible for different functions within the Bittensor ecosystem but are logically connected via the API. ```Coldkeys``` store funds securely and perform high risk operation such as transfers and staking, while hotkeys are used for less secure operations such as signing messages into the network, running miners, and validating the network. You can create wallets using the Bittensor API in two ways.

1. Using the python-api
```python
import bittensor as bt
wallet = bt.wallet( name = 'my_coldkey', hotkey = 'my_first_hotkey' )
wallet.create_if_non_existent() 
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
In both examples above we used the names ```my_coldkey``` as the coldkey name and ```my_first_hotkey``` as the hotkey name. These two keys were created locally on the device where you ran the commands and were then stored into bittensor's root directory ```~/.bittensor/wallets/```. If you ran the commands above you will notice that the coldkey generation required a password and the hotkey generation did not, the hotkey is **not** encrypted on the device whereas the coldkey **is** encrypted. You can view the directory where these keys have been generated via ```btcli list``` or directly with the terminal.

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

**Be sure to store your mnemonics safely** after generating your keys. If you lose the password to your wallet, or the access to the machine where the wallet is stored, you can always regenerate the coldkey using the mnemonic you saved from above. You can not retrieve the wallet with the password alone.
```bash
btcli regen_coldkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****
```

# Using btcli

The Bittensor command line interface (btcli) binary comes pre-installed with the bittensor API. You can use btcli to deploy, analyze, and interface with the Bittensor network, for instance stake or unstake funds, run miners, check network state etc. All of these operations are performed on wallets which you have created by following the instructions on the [previous page](#getting_started.md). To list all of your wallets run ```btcli list```. 
```bash
btcli list
Wallets
└─
    my_wallet (<ss58_address>)
       └── my_first_hotkey (<ss58_address>)
```

This shows the wallet addresses of the public keys associated with your cold and hot keys. The address are [ss58 encoded](https://docs.substrate.io/reference/address-formats/#:~:text=case%20L%20(l)-,Address%20type,address%20bytes%20that%20follow%20it.&text=Simple%20account%2Faddress%2Fnetwork%20identifier,directly%20as%20such%20an%20identifier) which is a compact representation of the keys. If you want to transfer TAO or recieve it, you can specify this address as the destination when performing ```btcli transfer```, while using the [website wallet](www.bittensor.com), or other community tool.
```bash 
btcli transfer --wallet.name YOUR_WALLET_NAME --dest DESTINATION_SS58_ADDRESS --amount AMOUNT_IN_TAO
```

Btcli can also be used to inspect the balances of wallets you have made ```btcli inspect```.
```bash
btcli inspect --wallet.name YOUR_WALLET_NAME
```

# Website Wallet

To create a wallet without installing bittensor, simply navigate to [Bittensor](http://bittensor.com) and click the `0.00` at the top right corner. Select `create` to create a new wallet or `import` to import your mnemonic from an existing wallet. The "access" option can be used if you have already created a wallet using the website and have not chosen to "forget" it. Once you have accessed your account, you can send, receive, or stake your TAO. 
