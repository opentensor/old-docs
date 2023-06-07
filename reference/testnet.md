
## Testnet & Difficulty


<Accordion title="Testnet">


# Testnet

The Bittensor Testnet is built to verify incoming changes and features made by developers. The block explorer can be reached [here](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Ftest.finney.opentensor.ai%3A443#/explorer).

To run your Neuron or Validator on the test network, users can simply add the following flag to the Neuron or Validator calls:
```bash dark
--subtensor.chain_endpoint wss://test.finney.opentensor.ai:443
```
This will point the system towards the testnet blockchain. You can also run a local version of the test network by in Subtensor by modifying `--chain` flag to use the test network spec file `--chain raw_spec_testfinney.json`:
```bash dark
./node-subtensor --chain test_finney --rpc-external --rpc-cors all --ws-external --no-mdns --sync warp --bootnodes /ip4/192.81.212.20/tcp/30333/p2p/12D3KooWQawexXodtsPEymJUX1X2eKzjNq6s8MvzEWtKwJ6mLmzy
```

### Testnet Taonomics
The consensus mechanism, validation, and mining are all identical between the test net and the main net, with the only exception being that there is no Tao issued to Neurons (meaning emissions are 0).


</Accordion>




<Accordion title="Difficulty Adjustment">


# Difficulty Adjustment

The POW and Recycle difficulties are adaptively adjusted every 100 blocks based on the following 4 cases.


    1. Registrations exceed the target and there were more recycle registrations than pow registrations?
        `burn_cost = burn_cost * ( burn_regs_this_interval + target_regs ) / 2 * target_regs`

    2. Registrations exceed the target and there were not more recycle registrations than pow registrations?
        `pow_difficulty = pow_difficulty * ( pow_regs_this_interval + target_regs ) / 2 * target_regs`

    3. Registrations do not exceed the target and there were more recycle registrations than pow registrations?
        `burn_difficulty = pow_difficulty * ( regs_this_interval + target_regs ) / 2 * target_regs`

    4. Registrations do not exceed the target and there were not more recycle registrations than pow registrations?
        `pow_difficulty = pow_difficulty * ( regs_this_interval + target_regs ) / 2 * target_regs`


### Viewing current difficulty
Using the cli
```bash dark
btcli list_subnets
NETUID  NEURONS  MAX_N   DIFFICULTY  TEMPO  CON_REQ  EMISSION  BURN(τ)
1       691    1.02 K   198.08 T    99     None     28.44%   τ4.75710
3      4096    4.10 K   320.81 T    99     None     71.56%   τ1.00000
    DIFFICULTY: Current proof of work difficulty
    BURN: Current cost to register a key via recycle registration.
```

</Accordion>
