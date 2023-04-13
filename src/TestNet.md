# Finney Test Network
Alongside Finney main network, we have also launched the Finney test network. All chain upgrades and new code is deployed on the Finney testnet first. Once new changes are verified to be functional and without issue, then we roll it to the main network. 

## Utilizing the Finney Test Network
The secure websocket connection URL for the Finney testnet is `wss://test.finney.opentensor.ai:443`. You can reach Finney in a few ways:

1. You can reach the Finney testnet via (Polkadot JS)[https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Ftest.finney.opentensor.ai%3A443#/explorer]. 
2. Using `btcli` you can specify you wish to run your miner on the testnet by adding the following flags: `--subtensor.network finney --subtensor.chain_endpoint wss://test.finney.opentensor.ai:443`.

