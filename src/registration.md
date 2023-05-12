# Registration

A Proof-of-Work (PoW) step that ensures you have the computational power necessary to run competitive models in the network, and serves as a form of sybil resistance against attacks. You can bypass the PoW step by paying a fee instead of computing a PoW. Both the difficulty of the PoW and the fee amount change according to demand on the network. 

- **NOTE**
    
    Each subnetwork has a cap on the number of allowed Hotkeys. If a Subnet is full and a Hotkey is registered, then the Hotkey with the lowest performing model is replaced with the newly registered Hotkey. 
    

To register a Hotkey on the network, simply run:

```bash
btcli register --wallet.name <your_wallet_name> --wallet.hotkey <your_hotkey_name>
```