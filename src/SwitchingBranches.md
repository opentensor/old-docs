# Testing Finney

To begin testing the Finney network, hop to the Finney branch.

1. Open the Bittensor directory
```bash
cd ~/.bittensor/bittensor
```

2. Run a quick update
```bash
btcli update
```

3. Jump to the finney branch
```
git checkout finney
```

4. Install
```bash
python3 -m pip install -e
```

# Finney Chain Endpoint

You may connect to the chain endpoint:
``
wss://public.finney.opentensor.ai:443
``
```bash
--subtensor.chain_endpoint wss://public.finney.opentensor.ai:443
```


# Return to the master branch

1. Remain in the Bittensor directory
```bash
cd ~/.bittensor/bittensor
```

2. Jump back ton the master branch
```bash
git checkout master
```

