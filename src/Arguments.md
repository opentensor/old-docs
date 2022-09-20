# Configuration Settings
---
```
--config.file
```
- If set, defaults are overridden by the passed file.
```
--config.strict
```
- If flagged, config.file will check that only exact arguments have been set.

## Neuron

```
--neuron.learning_rate
neuron.learning_rate:
```
- Training initial learning rate.
```
--neuron.momentum
neuron.momentum:
```
- Optimizer for momentum.
```
--neuron.clip_gradients
neuron.clip_gradients:
```
- Implement gradient clipping to avoid exploding loss on smaller architectures.
```
--neuron.device
neuron.device:
```
- Miner default training device CPU/CUDA.
```
--neuron.model_name
neuron.model_name:
```
- Pretrained model from hugging face.
```
--neuron.pretrained
neuron.pretrained:
```
- Ff the model should be pretrained.
```
--neuron.padding
neuron.padding:
```
- To pad out final dimensions.
```
--neuron.interpolate
neuron.interpolate:
```
- To interpolate between sentence length.
```
--neuron.inter_degree
neuron.inter_degree:
```
- Interpolate algorithm (nearest | linear | bilinear | bicubic | trilinear | area)
```
--neuron.name
neuron.name:
```
- Trials for this miner go in miner.root / (wallet_cold - wallet_hot) / miner.name
```
--neuron.checking
neuron.checking:
```
- To check if server settings are correct.
```
--neuron.restart
neuron.restart:
```
- If set, train the neuron from the beginning.
```
--neuron.blacklist.stake.forward
neuron.blacklist.stake.forward:
```
- Amount of stake (Tao) in order not to get blacklisted for forward requests.
```
--neuron.blacklist.stake.backward
neuron.blacklist.stake.backward:
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
neuron.blocks_per_epoch:
```
- Blocks per epoch.
```
--neuron.blacklist.time
neuron.blacklist.time:
```
- How often a peer can query you (seconds).
```
--neuron.local_train
neruon.local_train:
```
- If true, allow local training.
```
--neuron.remote_train
neuron.remote_train:
```
- If true, allow remote training.
```
--neuron.validation_synapse
neuron.validation_synapse:
```
- For Validators only. Synpase used for validation <TextCausalLMNext | TextCausalLM>. Default TextCausalLMNext. This should generally not be used. 

## Wallet

```
--wallet.name
wallet.name:
BT_WALLET_NAME
```
- The name of the wallet to unlock for running bittensor (name mock is reserved for mocking this wallet).
```
--wallet.hotkey
wallet.hotkey:
BT_WALLET_HOTKEY
```
- The name of the wallet's hotkey.
```
--wallet.path
wallet.path:
BT_WALLET_PATH
```
- The path to your bittensor wallets.
```
--wallet._mock
wallet._mock:
BT_WALLET_MOCK
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
--wallet.sort_by
```
- Sort the hotkeys by the specified column title (e.g. name, uid, axon).
```
--wallet.sort_order
```
- Sort the hotkeys in the specified ordering. (ascending/asc or descending/desc/reverse).
```
--wallet.reregister
```
- Whether to reregister the wallet if it is not already registered.
```
--max_stake
```
- Stake or unstake to a specific amount of stake on a hotkey.
  
## Axon

```
--axon.port
axon.port:
BT_AXON_PORT
```
- The port this axon endpoint is served on. i.e. 8091
```
--axon.ip
axon.ip:
BT_AXON_IP
```
- The local ip this axon binds to. ie. [::]
```
--axon.max_workers
axon.max_workers:
BT_AXON_MAX_WORERS
```
- The maximum number connection handler threads working simultaneously on this endpoint. The grpc server distributes new worker threads to service requests up to this number.
```
--axon.maximum_concurrent_rpcs
axon.maximum_concurrent_rpcs: 
BT_AXON_MAXIMUM_CONCURRENT_RPCS
```
- Maximum number of allowed active connections.
```
--axon.backward_timeout
axon.backward_timeout:
```
- Number of seconds to wait for backward axon request.
```
--axon.forward_timeout
axon.forward_timeout:
```
- Number of seconds to wait for forward axon request.
```
--axon.priority.max_workers
axon.priority.max_workers:
BT_AXON_PRIORITY_MAX_WORKERS
```
- Maximum number of threads in the thread pool.
```
--axon.priority.maxsize
axon.priority.maxsize:
BT_AXON_PRIORITY_MAXSIZE
```
- Maximum size of tasks in the priority queue.
```
--axon.compression
```
- Which compression algorithm to use for compression (gzip, deflate, NoCompression).

## Dendrite

```
--dendrite.timeout
dendrite.timeout:
BT_DENDRITE_TIMEOUT
```
- Default request timeout.
```
--dendrite.max_worker_threads
dendrite.max_worker_threads:
BT_DENDRITE_MAX_WORKER_THREADS
```
- Max number of concurrent threads used for sending RPC requests.
```
--dendrite.max_active_receptors
dendrite.max_active_receptors:
BT_DENDRITE_MAX_ACTIVE_RECEPTORS
```
- Max number of concurrently active receptors / tcp-connections.
```
--dendrite.requires_grad
dendrite.requires_grad:
BT_DENDRITE_REQUIRES_GRAD
```
- If true, the dendrite passes gradients on the wire.
```
--dendrite.no_requires_grad
```
- If set, the dendrite will not passes gradients on the wire.
```
--dendrite.multiprocessing
dendrite.multiprocessing:
BT_DENDRITE_MULTIPROCESSING
```
- If set, the dendrite will initialize multiprocessing.
```
--dendrite.compression
dendrite.compression:
```
- Which compression algorithm to use for compression (gzip, deflate, NoCompression).
```
--dendrite._mock
dendrite._mock:
```
- To turn on dendrite mocking for testing purposes.

## Subtensor

```
--subtensor.network
subtensor.network:
BT_SUBTENSOR_NETWORK
```
- The Subtensor network (nobunaga/nakamoto/local).
```
--subtensor.chain_endpoint
subtensor.chain_endpoint:
BT_SUBTENSOR_CHAIN_ENDPOINT
```
- The Subtensor endpoint. If set, overrides subtensor.network.
```
--subtensor._mock
BT_SUBTENSOR_MOCK
```
- To turn on Subtensor mocking for testing purposes.

## Logging

```
--logging.debug
logging.debug:
BT_LOGGING_DEBUG
```
- Turn on Bittensor debugging information.
```
--logging.trace
logging.trace:
BT_LOGGING_TRACE
```
- Turn on Bittensor trace level information.
```
--logging.record_log
logging.record_log:
BT_LOGGING_RECORD_LOG
```
- Turns on logging to file.
```
--logging.logging_dir
logging.logging_dir:
BT_LOGGING_LOGGING_DIR
```
- Logging default root directory.

## Dataset

```
--dataset.batch_size
dataset.batch_size:
BT_DATASET_BATCH_SIZE
```
- Batch size.
```
--dataset.block_size
dataset.block_size:
BT_DATASET_BLOCK_SIZE
```
- Number of text items to pull for each example.
```
--dataset.num_workers
dataset.num_workers:
BT_DATASET_NUM_WORKERS
```
- Number of workers for data loader.
```
--dataset.dataset_name
dataset.dataset_name:
BT_DATASET_DATASET_NAME
```
- Which datasets to use (ArXiv, BookCorpus2, Books3, DMMathematics, EnronEmails, EuroParl, Gutenberg_PG, HackerNews, NIHExPorter, OpenSubtitles, PhilPapers, UbuntuIRC, YoutubeSubtitles).
```
--dataset.data_dir
dataset.data_dir:
BT_DATASET_DATADIR
```
- Where to save and load the data.
```
--dataset.save_dataset
dataset.save_dataset:
BT_DATASET_SAVE_DATASET
```
- Save the downloaded dataset or not.
```
--dataset.max_datasets
dataset.max_datasets:
BT_DATASET_MAX_DATASETS
```
- Number of datasets to load.
```
--dataset.num_batches
dataset.num_batches:
BT_DATASET_NUM_BATCHES
```
- The number of data to download each time (measured by the number of batches).
```
--dataset._mock
dataset._mock:
```
- To turn on dataset mocking for testing purposes.

## Metagraph

```
--metagraph._mock
```
- To turn on metagraph mocking for testing purposes.


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

## CUDA

```
--cuda
```
- Uses CUDA for registration.
```
--cuda.dev_id
```
Which GPU to use for registration.
```
--cuda.TPB
```
- The number of threads per block in the CUDA kernel. This should be left at the default 256 or raised to 512. The registration process may crash if this is set too high. Only set to powers of 2.
```
--cuda.update_interval
```
- The number of nonces to solve between chain updates. Default setting is 50_000. Setting to a higher value may mean less frequent chain updates, which may lead to submitting a solution outside of the valid solve window for that block (not efficient).


## Wandb

```
--wandb.api_key
wandb.api_key:
```
- Pass Wandb api key.
```
--wandb.directory
wandb.directory:
BT_WANDB_DIRECTORY
```
- Pass Wandb run name.
```
--wandb.name
wandb.name:
BT_WANDB_NAME
```
- Pass Wandb project name.
```
--wandb.offline
wandb.offline:
BT_WANDB_OFFLINE
```
- Pass Wandb offline option.
```
--wandb.project
wandb.project:
BT_WANDB_PROJECT
```
- Pass Wandb project name.
```
--wandb.run_group
wandb.run_group:
BT_WANDB_RUN_GROUP
```
- Pass Wandb group name.
```
--wandb.tags
wandb.tags:
BT_WANDB_TAGS
```
- Pass Wandb tags.



