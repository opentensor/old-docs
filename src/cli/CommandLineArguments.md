# Flags
---
```
--config
```
- If set, defaults are overridden by the passed file.
```
--strict
```
- If flagged, config will check that only exact arguments have been set.

## Neuron

```
--neuron.learning_rate
```
- Training initial learning rate.
```
--neuron.momentum
```
- Optimizer for momentum.
```
--neuron.clip_gradients
```
- Implement gradient clipping to avoid exploding loss on smaller architectures.
```
--neuron.device
```
- Miner default training device CPU/CUDA.
```
--neuron.model_name
```
- Pretrained model from hugging face.
```
--neuron.pretrained
```
- Ff the model should be pretrained.
```
--neuron.padding
```
- To pad out final dimensions.
```
--neuron.interpolate
```
- To interpolate between sentence length.
```
--neuron.inter_degree
```
- Interpolate algorithm (nearest | linear | bilinear | bicubic | trilinear | area)
```
--neuron.name
```
- Trials for this miner go in miner.root / (wallet_cold - wallet_hot) / miner.name
```
--neuron.checking
```
- To check if server settings are correct.
```
--neuron.restart
```
- If set, train the neuron from the beginning.
```
--neuron.blacklist.stake.forward
```
- Amount of stake (Tao) in order not to get blacklisted for forward requests.
```
--neuron.blacklist.stake.backward
```
- Amount of stake (Tao) in order not to get blacklisted for backward requests.
```
--neuron.metagraph_sync
```
- How often to sync the metagraph.
```
--neuron.blocks_per_set_weights
```
- How often to sync set weights.
```
--neuron.blocks_per_epoch
```
- Blocks per epoch.
```
--neuron.blacklist.time
```
- How often a peer can query you (seconds).

## Wallet

```
--wallet.name
```
- The name of the wallet to unlock for running bittensor (name mock is reserved for mocking this wallet).
```
--wallet.hotkey
```
- The name of the wallet's hotkey.
```
--wallet.path
```
- The path to your bittensor wallets.
```
--wallet._mock
```
- To turn on wallet mocking for testing purposes.
```
--wallet.all_hotkeys
```
- Stake or unstake from all hotkeys simultaneously.
```
--wallet.hotkeys
```
- Stake or unstake from a specific set of hotkeys simultaneously.
```
--wallet.exclude_hotkeys
```
- Stake or unstake from all hotkeys simultaneously while exluding a specific set of hotkeys.
```
--max_stake
```
- Stake or unstake to a specific amount of stake on a hotkey.
  
## Axon

```
--axon.port
```
- The port this axon endpoint is served on. i.e. 8091
```
--axon.ip
```
- The local ip this axon binds to. ie. [::]
```
--axon.max_workers
```
- The maximum number connection handler threads working simultaneously on this endpoint. The grpc server distributes new worker threads to service requests up to this number.
```
--axon.maximum_concurrent_rpcs
```
- Maximum number of allowed active connections.
```
--axon.backward_timeout
```
- Number of seconds to wait for backward axon request.
```
--axon.forward_timeout
```
- Number of seconds to wait for forward axon request.
```
--axon.priority.max_workers
```
- Maximum number of threads in the thread pool.
```
--axon.priority.maxsize
```
- Maximum size of tasks in the priority queue.
```
--axon.compression
```
- Which compression algorithm to use for compression (gzip, deflate, NoCompression)

## Subtensor

```
--subtensor.network
```
- The subtensor network flag.
```
--subtensor.chain_endpoint
```
- The subtensor endpoint flag. If set, overrides the --network flag.
```
--subtensor._mock
```
- To turn on subtensor mocking for testing purposes.

## Logging

```
--logging.debug
```
- Turn on bittensor debugging information.
```
--logging.trace
```
- Turn on bittensor trace level information
```
--logging.record_log
```
- Turns on logging to file.
```
--logging.logging_dir
```
- Logging default root directory.

## Dataset

```
--dataset.batch_size
```
- Batch size.
```
--dataset.block_size
```
- Number of text items to pull for each example.
```
--dataset.num_workers
```
- Number of workers for data loader.
```
--dataset.dataset_name
```
- Which datasets to use (ArXiv, BookCorpus2, Books3, DMMathematics, EnronEmails, EuroParl, Gutenberg_PG, HackerNews, NIHExPorter, OpenSubtitles, PhilPapers, UbuntuIRC, YoutubeSubtitles).
```
--dataset.data_dir
```
- Where to save and load the data.
```
--dataset.save_dataset
```
- Save the downloaded dataset or not.
```
--dataset.max_datasets
```
- Number of datasets to load.
```
--dataset.num_batches
```
- The number of data to download each time (measured by the number of batches).

## Mock Tests

```
--dataset._mock
```
- To turn on dataset mocking for testing purposes.
```
--metagraph._mock
```
- To turn on metagraph mocking for testing purposes.
```
--strict
```
- If flagged, config will check that only exact arguments have been set.

## Nucleus

```
--nucleus.topk
```
- The number of peers queried during each remote forward call.
```
--nucleus.nhid
```
- The dimension of the feedforward network model in nn.TransformerEncoder.
```
--nucleus.nhead
```
- The number of heads in the multiheadattention models.
```
--nucleus.nlayers
```
- The number of nn.TransformerEncoderLayer in nn.TransformerEncoder.
```
--nucleus.dropout 
```
- The dropout value.
```
--nucleus.importance
```
- Hyperparameter for the importance loss.
```
--nucleus.noise_multiplier
```
- Standard deviation multiplier on weights.