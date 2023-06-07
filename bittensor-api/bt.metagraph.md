<Accordion title="Metagraph">


title: bt.metagraph

# Chain State Torch Interface


## Introduction
The `Metagraph` class holds the chain state of a particular subnetwork at a specific block.

## Examples
```python dark
import bittensor as bt

# Creating metagraph and sync state from a netuid parameter, defaults to connecting to network `finney`
metagraph = bt.metagraph( netuid = 1 )

# Create metagraph and sync with lite = False to sync weights and bonds matrices.
metagraph = bt.metagraph( netuid = 1, lite = False)

# Create metagraph and sync state from local entrypoint, assuming a subtensor chain is currently running.
metagraph = bt.metagraph( netuid = 1, network = 'local' )

# Create an empty metagraph object with no state syncing.
metagraph = bt.metagraph( netuid = 1, sync = False )

# Sync the metagraph at a particular block
metagraph.sync( block = 100000 )

# Save the metagraph to ~/.bittensor/metagraphs/network-$NETWORK_NAME/netuid-#NETUID/block-$BLOCK.pt
metagraph.save()

# Load the latest metagraph by block.
metagraph.load()
```

## Methods

### S
```python
def S(self) -> torch.FloatTensor
```
Returns the total stake.


### R
```python
def R(self) -> torch.FloatTensor
```
Returns the ranks.


### I
```python
def I(self) -> torch.FloatTensor
```
Returns the incentive.


### E
```python
def E(self) -> torch.FloatTensor
```
Returns the emission.


### C
```python
def C(self) -> torch.FloatTensor
```
Returns the consensus.


### T
```python
def T(self) -> torch.FloatTensor
```
Returns the trust.


### Tv
```python
def Tv(self) -> torch.FloatTensor
```
Returns the validator trust.


### D
```python
def D(self) -> torch.FloatTensor
```
Returns the dividends.


### B
```python
def B(self) -> torch.FloatTensor
```
Returns the bonds.


### W
```python
def W(self) -> torch.FloatTensor
```
Returns the weights.


### hotkeys
```python
def hotkeys(self) -> List[str]
```
Returns the list of hotkeys for the axons.


### coldkeys
```python
def coldkeys(self) -> List[str]
```
Returns the list of coldkeys for the axons.


### addresses
```python
def addresses(self) -> List[str]
```
Returns the list of IP addresses for the axons.


### __str__
```python
def __str__(self)
```
Returns a string representation of the Metagraph.


### __repr__
```python
def __repr__(self)
```
Returns the same string representation as `__str__`.


### metadata
```python
def metadata(self) -> dict
```
Returns a dictionary of Metagraph metadata.


### __init__
```python
def __init__(self, netuid: int, network: str = 'finney', lite: bool = True, sync: bool = True) -> 'metagraph'
```
Initializes a new instance of the Metagraph.


### sync
```python
def sync (self, block: Optional[int] = None, lite: bool = True) -> 'metagraph'
```
Syncs the Metagraph state at the passed block. Optionally syncs the weights also.


### save
```python
def save(self) -> 'metagraph'
```
Saves the Metagraph object's state_dict under bittensor root directory.


### load
```python
def load(self) -> 'metagraph'
```
Loads the Metagraph object's state_dict from bittensor root directory.


### load_from_path
```python
def load_from_path(self, dir_path:str) -> 'metagraph'
```
Loads the Metagraph object's state_dict from the specified directory path.


</Accordion>
