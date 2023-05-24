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

Additional commands can be viewed by running ```btcli --help```

```bash
$ btcli --help

positional arguments:
  {run,help,list,stake,update,inspect,weights,unstake,overview,register,transfer,nominate,new_hotkey,metagraph,new_coldkey,my_delegates,list_subnets,regen_hotkey,regen_coldkey,delegate,undelegate,list_delegates,regen_coldkeypub,recycle_register}
    help                Displays the help
    list                List wallets
    stake               Stake to your hotkey accounts.
    update              Update bittensor
    inspect             Inspect a wallet (cold, hot) pair
    weights             Show weights from chain.
    unstake             Unstake from hotkey accounts.
    overview            Show registered account overview.
    register            Register a wallet to a network.
    transfer            Transfer Tao between accounts.
    nominate            Become a delegate on the network
    new_hotkey          Creates a new hotkey (for running a miner) under the
                        specified path.
    metagraph           Metagraph commands
    new_coldkey         Creates a new coldkey (for containing balance) under
                        the specified path.
    my_delegates        Show all delegates where I am delegating a positive
                        amount of stake
    list_subnets        List all subnets on the network
    regen_hotkey        Regenerates a hotkey from a passed mnemonic
    regen_coldkey       Regenerates a coldkey from a passed value
    delegate            Delegate Stake to an account.
    undelegate          Undelegate Stake from an account.
    list_delegates      List all delegates on the network
    regen_coldkeypub    Regenerates a public coldkey from the public part of the
                        coldkey.
    recycle_register    Register a wallet to a network.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       If set, defaults are overridden by passed file.
  --strict              If flagged, config will check that only exact
                        arguemnts have been set.
```



