# Fine Tuning

Welcome to the CLM Model Tuning walkthrough. This section will guide you through how to install and use our guide to fine tune your models. 

Fine tuning can help improve your model's accuracy and efficency before training it on the Bittensor network. 

## Instalation and Requirements

Bittensor must be either locally or in the virtual environment you are working from.

Run:
```bash
pip install -r requirements.txt
```
to install the additional packages for this script.


## Fine tuning on Bittensor

```bash
python3 finetune_using_clm.py dataset.name=./path/to/your/data.txt
```

## Fine tuning on HuggingFace

```bash
python finetune_using_clm.py dataset.name=wikitext dataset.config_name=wikitext-103-v1
```

## Fine tuning on your own data

```bash
python finetune_using_clm.py dataset.name=./path/to/your/data.txt
```

## Configuring training parameters

```bash
conf/config.yaml
```

## Serving custom models on the Bittensor

```bash
btcli run ..... --neuron.model_name=/home/user/models/my-tuned-gpt2
```

OR

..
mv pytorch_model.bin advanced_server
...

## Transferring model files between devices

Your model files can also be transferred between devices through the secure file transfer protocol [(sftp)](https://www.ssh.com/academy/ssh/sftp).



- sftp

sftp root@xx.xx.xx.xx where xx.xx.xx.xx is the ip address of the other machine and cd to the directory you want. Then when you find the file, just use get pytorch_model.bin



```
output_dir: "tuned-model"

bittensor:
  network: "nobunaga"

dataset:
  # either 'bittensor', a local path, or one from huggingface
  name: "bittensor"
  config_name: null # necessary for huggingface datasets
  num_batches: 10
  block_size: null # if null, defaults to bittensor's validator sequence length.

  overwrite_cache: false
  keep_linebreaks: true
  concatenate_raw: false # only really necessary when loading a local .txt file

model:
  name: gpt2
  config_name: null

tokenizer:
  name: null
  use_fast: true
  preprocessing_num_workers: null
  pad_token: "[PAD]"

training:
  seed: null
  val_split_percent: 5

  # if null these both default to bittensor's validator batch size
  train_batch_size: null
  eval_batch_size: null

  learning_rate: 1e-5
  weight_decay: 0.0
  num_epochs: 5
  max_train_steps: null
  gradient_accumulation_steps: 1
  lr_scheduler: "constant" # ["linear", "cosine", "cosine_with_restarts", "polynomial", "constant", "constant_with_warmup"]
  lr_warmup_steps: 0
  eval_every: 50
  checkpoint:
    resume_from_checkpoint: 0 # integer representing which checkpoint to load from, or <= 0 to not
    every_n_steps: null

tracking:
  enabled: false
  report_to: "all"
```