<Accordion title="Basic Commands">

---
title: bt.wallet
---
# Wallet Class Reference Documentation

---
## Introduction
The `Wallet` acts as an interface over a coldkey, hotkey pairing.

## Examples
```python dark
import bittensor as bt

# Creating a default wallet coldkey = default, hotkey = default, path = ~/.bittensor/wallets
wallet = bt.wallet()

# Create wallet by parsing --wallet.name, --wallet.hotkey and --wallet.path from the command line.
wallet = bt.wallet( config = bt.wallet.config() )

# Create wallet by explicitly setting names of coldkey, hotkey and path.
wallet = bt.wallet( name = 'my_coldkey', hotkey = 'my_first_hotkey', path = '~/path/to/wallets/dir' )
```

## Methods

---
### create_coldkey_from_uri
```python
create_coldkey_from_uri(self, uri:str, use_password: bool = True, overwrite:bool = False) -> 'Wallet'
```
Creates coldkey from suri string, optionally encrypts it with the user's inputed password.

---
### create_hotkey_from_uri
```python
create_hotkey_from_uri( self, uri:str, use_password: bool = False, overwrite:bool = False) -> 'Wallet'
```
Creates hotkey from suri string, optionally encrypts it with the user's inputed password.

---
### new_coldkey
```python
new_coldkey( self, n_words:int = 12, use_password: bool = True, overwrite:bool = False) -> 'Wallet'
```
Creates a new coldkey, optionally encrypts it with the user's inputed password and saves to disk.

---
### create_new_coldkey
```python
create_new_coldkey( self, n_words:int = 12, use_password: bool = True, overwrite:bool = False) -> 'Wallet'
```
Creates a new coldkey, optionally encrypts it with the user's inputed password and saves to disk.

---
### new_hotkey
```python
new_hotkey( self, n_words:int = 12, use_password: bool = False, overwrite:bool = False) -> 'Wallet'
```
Creates a new hotkey, optionally encrypts it with the user's inputed password and saves to disk.

---
### create_new_hotkey
```python
create_new_hotkey( self, n_words:int = 12, use_password: bool = False, overwrite:bool = False) -> 'Wallet'
```
Creates a new hotkey, optionally encrypts it with the user's inputed password and saves to disk.

---
### regenerate_coldkeypub
```python
regenerate_coldkeypub( self, ss58_address: Optional[str] = None, public_key: Optional[Union[str, bytes]] = None, overwrite: bool = False ) -> 'Wallet'
```
Regenerates the coldkeypub from passed ss58_address or public_key and saves the file

---
### regenerate_coldkey
```python
regenerate_coldkey(self, use_password: bool = True, overwrite: bool = False, **kwargs) -> 'Wallet'
```
Regenerates the coldkey from passed mnemonic, seed, or json encrypts it with the user's password and saves the file.

---
### regenerate_hotkey
```python
regenerate_hotkey(self, use_password: bool = True, overwrite: bool = False, **kwargs) -> 'Wallet'
```
Regenerates the hotkey from passed mnemonic, seed, or json encrypts it with the user's password and saves the file.

---
### __str__
```python
__str__(self)
```
Returns a string representation of the Wallet.

---
### __repr__
```python
__repr__(self)
```
Returns the same string representation as `__str__`.

---
### create_if_non_existent
```python
create_if_non_existent(self, coldkey_use_password:bool = True, hotkey_use_password:bool = False) -> 'Wallet'
```
Creates coldkeypub and hotkeys if they don't exist.


---
### create
```python
create(self, coldkey_use_password:bool = True, hotkey_use_password:bool = False) -> 'Wallet'
```
Similar to `create_if_non_existent`, creates coldkeypub and hotkeys if they don't exist.

---
### recreate
```python
recreate(self, coldkey_use_password:bool = True, hotkey_use_password:bool = False ) -> 'Wallet'
```
Creates new coldkeypub and hotkeys, overwriting existing ones.

---
### set_hotkey, set_coldkeypub, set_coldkey
```python
set_hotkey(self, keypair: 'bittensor.Keypair', encrypt: bool = False, overwrite: bool = False) -> 'bittensor.Keyfile'
set_coldkeypub(self, keypair: 'bittensor.Keypair', encrypt: bool = False, overwrite: bool = False) -> 'bittensor.Keyfile'
set_coldkey(self, keypair: 'bittensor.Keypair', encrypt: bool = True, overwrite: bool = False) -> 'bittensor.Keyfile'
```
Sets the hotkey, coldkeypub, and coldkey, respectively. Each can optionally be encrypted and overwritten.

---
### get_coldkey, get_hotkey, get_coldkeypub
```python
get_coldkey(self, password: str = None ) -> 'bittensor.Keypair'
get_hotkey(self, password: str = None ) -> 'bittensor.Keypair'
get_coldkeypub(self, password: str = None ) -> 'bittensor.Keypair'
```
Returns the coldkey, hotkey, and coldkeypub, respectively. If encrypted, requires a password.

---
### create_coldkey_from_uri
```python
create_coldkey_from_uri(self, uri:str, use_password: bool = True, overwrite:bool = False) -> 'Wallet'
```
Creates a coldkey from a suri string. Optionally encrypts and overwrites existing coldkey.



</Accordion>