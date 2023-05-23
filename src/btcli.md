# BTCLI

The Bittensor command line interface is the primary command line tool to deploy, analyze, and interface with the Bittensor network. It can be used to run a model, stake, unstake, nominate, delegate, and more. 

You can `btcli --help` command as follows to see a full list of commands

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

Subsequently, each command has flags to help specify the configurations. For example, `--wallet.name` specifies the name of the Coldkey being used. You can see a list of these configuration flags by calling `—help` on a btcli command, as follows:
