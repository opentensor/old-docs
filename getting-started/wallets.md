
## Wallets


The Bittensor wallet is the core ownership and identity technology around which all functionalities of the network are carried out. A wallet consists of a [coldkey](../glossary/glossary)  and a [hotkey](../glossary/glossary) pairing of two seperate [EdDSA cryptographic keypairs](https://en.wikipedia.org/wiki/EdDSA#Ed25519) that are responsible for different functionalities within the ecosystem, but are logically connected via the API.

The (../glossary/glossary/#coldkey) is encrypted on your device and is used to store funds securely and perform high risk operations, such as transfers and staking, while the (../glossary/glossary/#hotkey) is unencrypted, and used for less secure operations such as signing messages into the network, running miners, and validating the network.

Once you have [installed bittensor](../getting-started/installation), you can a wallet locally on your machine in two ways, described below. You can also create an [external wallet](#03-external-wallet).


 through the Bittensor website, or use a secondary tool like [subkey](https://docs.substrate.io/reference/command-line-tools/subkey/). Both of these options allow you to use TAO without installing Bittensor.

### 01 btcli

```bash dark
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
!> As previously mentioned, the hotkey is **not** encrypted on the device whereas the coldkey **is**.
If you want to encrypt your hotkey, use `btcli new_hotkey --use_password`.


### 02 Python

```python numbered dark
import bittensor as bt
wallet = bt.wallet( name = 'my_coldkey', hotkey = 'my_first_hotkey' )
wallet.create_if_non_existent()
"Wallet (my_coldkey, my_first_hotkey, ~/.bittensor/wallets/)"
```

Generated wallets are stored locally on your machine under `~/.bittensor/wallets`.
```bash dark nocopy
$ tree ~/.bittensor/
    ~/.bittensor/                       # The Bittensor root directory.
        wallets/                        # The folder containing all Bittensor wallets.
            my_coldkey/                 # The name of your wallet, i.e. "my_coldkey".
                coldkey                 # Your password encrypted coldkey.
                coldkeypub.txt          # The unencrypted public address of your coldkey
                hotkeys/                # The folder containing all this coldkey's hotkeys.
                    my_first_hotkey     # Your unencrypted hotkey information.
```

You can list all the local wallets stored in Bittensor's root directly with [btcli list](../reference/btcli).
```bash dark nocopy
$ btcli list
Wallets
└─
    my_wallet (<ss58_address>)
       └── my_first_hotkey (<ss58_address>)
```
The [ss58 encoded](https://docs.substrate.io/reference/address-formats/#:~:text=case%20L%20(l)-,Address%20type,address%20bytes%20that%20follow%20it.&text=Simple%20account%2Faddress%2Fnetwork%20identifier,directly%20as%20such%20an%20identifier) strings shown above are compact representations of your public keys, use these as destinations for transfering TAO, for instance when using [btcli transfer](../reference/btcli).

?> Be sure to store your mnemonics safely
If someone has your mnemonic, they own your TAO. If you lose the password to your wallet, or the access to the machine where the wallet is stored, you can always regenerate the coldkey using the mnemonic you saved from above. You can **not** retrieve the wallet with the password alone.

If you need to regenerate your wallets, you can use the cli with your mnemonic.
```bash dark
btcli regen_coldkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****
```


### 03 External Wallet

To create a wallet without installing bittensor you can use the wallet on [Bittensor](http://bittensor.com). Click the **0.00** in the top right corner. Select **create** to create a new wallet or **import** to import your mnemonic from an existing wallet. The "access" option can be used if you have already created a wallet using the website and have not chosen to "forget" it. Once you have accessed your account, you can send, receive, or stake your TAO.
