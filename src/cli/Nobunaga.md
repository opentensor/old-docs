# Nobunaga Guide

## Testing Miners With Nobunaga

*Nobunaga is the test network used for running practice miners.* 

### 1. **Change the Directory to Bittensor**

```bash
cd ~/.bittensor/bittensor 
```

### 2. Open the Synapse Branch

```bash
git checkout Synapse
```

If you have not yet installed Bittensor:

```bash
git clone -b Synapse https://github.com/opentensor/bittensor

pip install -e bittensor/
```

*To go back to the master branch (Nakamoto)*

```bash
git checkout master
```

*YOU MUST CREATE A NEW WALLET ON NOBUNAGA. WALLETS REGISTERED TO NAKAMOTO WILL NOT BE ACCESSIBLE FROM NOBUNAGA.*

### 3. Create a new Coldkey -

```bash
btcli new_coldkey
```

### 4. Create a New Hotkey

```bash
btcli new_hotkey
```

### 5. Run a Server or a Validator

```bash
Enter subtensor network [local/nobunaga/nakamoto] (nakamoto): nobunaga
Enter wallet name (default): WALLET_NAME
Enter hotkey name (default): HOTKEY_NAME
Enter miner name [core_validator/core_server] (core_server): core_server or core_validator
```
