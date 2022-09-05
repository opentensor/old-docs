# Network Updates

Occasionally network updates will require you to manually update Bittensor by pulling and installing the latest master branch. 

1. Pull the latest master and install.

```bash
git -C ~/.bittensor/bittensor pull origin master
python3 -m pip install -e ~/.bittensor/bittensor
```

2. Restart your miners.

Restarting Servers and Validators follows the same procedure. Simply stop and start your mining sequence after each update to ensure your miners are using the latest version of Bittensor.

