
## [btcli]


The Bittensor command line interface (btcli) comes [installed](getting-started/installation) with the bittensor API and can be used to stake or unstake funds, run miners, check network state, and even deploy, analyze, and interface with the Bittensor network.



<Accordion title="_basic commands">

```bash dark
btcli [COMMAND]
$ btcli --help

positional arguments:
  {list,stake,update,inspect,unstake,overview,register,transfer,nominate,new_hotkey,metagraph,new_coldkey,my_delegates,list_subnets,regen_hotkey,regen_coldkey,delegate,undelegate,list_delegates,regen_coldkeypub,recycle_register,senate,proposals,proposal_votes,senate_register,senate_leave,senate_vote}
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
    senate              View senate and it's members
    proposals           View active triumvirate proposals and their status
    proposal_votes      View an active proposal's votes by address.
    senate_register     Register as a senate member to participate in proposals
    senate_leave        Discard senate membership in the governance protocol
    senate_vote         Vote on an active proposal by hash.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       If set, defaults are overridden by passed file.
  --strict              If flagged, config will check that only exact
                        arguemnts have been set.
```

</Accordion>


<Accordion title="_wallets">

### List wallets
Lists all wallets locally stored on your machine under path `--wallet.path`. Outputs addresses are [ss58 encoded](https://docs.substrate.io/reference/address-formats/#:~:text=case%20L%20(l)-,Address%20type,address%20bytes%20that%20follow%20it.&text=Simple%20account%2Faddress%2Fnetwork%20identifier,directly%20as%20such%20an%20identifier) required as desinstations for ```btcli transfer```
**Usage**: ```btcli list [OPTIONS]```
```bash dark
btcli list
Wallets
└─
    my_wallet (<ss58_address>)
       └── my_first_hotkey (<ss58_address>)
```
### New Coldkey
Create a new wallet with encrypted coldkey [EdDSA cryptographic keypair](https://en.wikipedia.org/wiki/EdDSA#Ed25519)
**Usage**: ```btcli new_coldkey [OPTIONS]```
```bash dark
btcli new_coldkey
```

### New Hotkey
Create a [EdDSA cryptographic keypair](https://en.wikipedia.org/wiki/EdDSA#Ed25519) hotkey associated with a wallet.
**Usage**: ```btcli new_hotkey [OPTIONS]```
```bash dark
btcli new_hotkey
```

### Regenerate Hotkey
Regenerate a hotkey from mnemonic.
**Usage**: ```btcli regen_hotkey [OPTIONS]```
```bash dark
btcli regen_hotkey
```

### Regenerate Coldkey
Regenerate a wallet encrypted coldkey file from mnemonic or seed.
**Usage**: ```btcli regen_coldkey [OPTIONS]```
```bash dark
btcli regen_coldkey
```

### Regenerate Coldkeypub
Regenerate a wallet with just the public seed of your coldkey.
**Usage**: ```btcli regen_coldkeypub [OPTIONS]```
```bash dark
btcli regen_coldkeypub
```
</Accordion>



<Accordion title="Registration">

### POW registration
Begins a proof of word registration.
**Usage**: ```btcli register [OPTIONS]```
```bash dark
btcli register
```

### Recycle registration
Initiates a TAO recycle registration.
**Usage**: ```btcli recycle_register [OPTIONS]```
```bash dark
btcli recycle_register
```
</Accordion>


<Accordion title="Transfers/Staking">

### Transfer Tao
Transfers TAO from a wallet coldkey to another wallet public key address. Destination addresses must be [ss58 encoded](https://docs.substrate.io/reference/address-formats/#:~:text=case%20L%20(l)-,Address%20type,address%20bytes%20that%20follow%20it.&text=Simple%20account%2Faddress%2Fnetwork%20identifier,directly%20as%20such%20an%20identifier).
**Usage**: ```btcli transfer [OPTIONS]```
```bash dark
btcli transfer
```

### Stake Tao
Stake TAO from the coldkey balance to the hotkey staking account.
**Usage**: ```btcli stake [OPTIONS]```
```bash dark
btcli stake
```

### Unstake Tao
Remove stake TAO from the hotkey staking account and add it to the coldkey.
**Usage**: ```btcli unstake [OPTIONS]```
```bash dark
btcli unstake
```
</Accordion>


<Accordion title="Delegation">

### Delegate Tao
List all active delegates available for delegated TAO.
**Usage**: ```btcli list_delegates```
```bash dark
btcli list_delegates
```
![List Delegates](/images/list_delegates.png 'Output of List Delegates')

### Delegate Tao
Delegate TAO from the coldkey balance to the hotkey staking account of a delegate.
**Usage**: ```btcli delegate [OPTIONS]```
```bash dark
btcli delegate
```

### Undelegate Tao
Remove TAO from the hotkey balance of delegate you have previously delegated to.
**Usage**: ```btcli undelegate [OPTIONS]```
```bash dark
btcli undelegate
```

### Nominate
Nominate a hotkey as a delegate as a prerequisite for recieving delegations.
**Usage**: ```btcli nominate [OPTIONS]```
```bash dark
btcli nominate
```

### My Delegates
Create a hotkey associated to a wallet.
**Usage**: ```btcli new_hotkey [OPTIONS]```
```bash dark
btcli new_hotkey
```
</Accordion>

<Accordion title="Governance">

### View proposals
List all active proposals for the Senate to vote on.
**Usage**: ```btcli proposals```
```bash dark
btcli proposals
```
![Proposals](/images/list_proposals.png 'Output of Proposals')

### View Senate
View all delegates currently registered to Senate.
**Usage**: ```btcli senate```
```bash dark
btcli senate
```

### Proposal Votes
Inspect the votes for a single proposal.
**Usage**: ```btcli proposal_votes [OPTIONS]```
```bash dark
btcli proposal_votes --proposal=[PROPOSAL_HASH]
```

### Senate Register
Elect to join the Senate with your nominated hotkey.
**Usage**: ```btcli senate_register [OPTIONS]```
```bash dark
btcli senate_register
```

### Senate Leave
Disown your membership of a Senate seat with your nominated hotkey.
**Usage**: ```btcli senate_leave [OPTIONS]```
```bash dark
btcli senate_leave
```

### Senate Vote
Participate in a triumvirate proposal by voting with your senate hotkey.
**Usage**: ```btcli senate_vote [OPTIONS]```
```bash dark
btcli senate_vote --proposal=[PROPOSAL_HASH]
```
</Accordion>

<Accordion title="Misc">

### Update Bittensor
Update your Bittensor installation
**Usage**: ```btcli update [OPTIONS]```
```bash dark
btcli update
```
</Accordion>
