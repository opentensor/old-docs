# Staking to a Delegate
In addition to running your own miner or validator, you also have the option to delegate your Tao to the Opentensor Foundation validation pool. In essence, 
delegating Tao simply means you are staking to the foundation's validator, instead of running your own. You can simply 'undelegate' your Tao to take it back from the pool at any time.

For a list of Delegates and their hotkeys: https://github.com/opentensor/bittensor/blob/master/delegates.json


1. Add your Bittensor wallet to the [Polkadot Extension](https://polkadot.js.org/extension/) wallet in your browser (you will need your mnemonic to do this). Once you've done so, navigate to [Polkadot JS](https://polkadot.js.org/apps/?rpc=wss://entrypoint-finney.opentensor.ai:443#/accounts) and your account should be displayed there.


2. Navigate to [Developer -> extrinsics](https://polkadot.js.org/apps/?rpc=wss://entrypoint-finney.opentensor.ai:443#/extrinsics).
![Extrinsics](images/step2.png)


3. In the drop down, select SubtensorModule.
![SubtensorModule](images/step3.png)


4. In the drop down menu corresponding to the SubtensorModule drop down, select addStake. 
![AddStake](images/step4.png)


5. Paste the hotkey of the delegate in the drop down box labeled "hotkey".
![delegatehotkey](images/step5.png)


1. In the text box, input in Rao the amount of Tao that you wish to stake to this delegate. 1 Tao = 10^9 Rao. Therefore, if you wish to stake 1 Tao, then input 1000000000. If you wish to stake 10 Tao, then input 10000000000, and so on. 
![amountstaked](images/step6.png)


7. Once you have verified the keys and amounts, click Submit Transaction to sign and submit this transaction to be included on the chain.
![signandsubmit](images/step7.png)

