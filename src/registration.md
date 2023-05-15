# Registration

Prior to participating in the Bittensor network, a registration step is required. Registration is a Proof-of-Work (PoW) step that ensures you have the computational power necessary to run competitive models in the network, and serves as a form of Sybil resistance against attacks. You can bypass the PoW step by paying a fee instead of computing a PoW. Both the difficulty of the PoW and the fee amount change according to demand on the network. 

Each time a new hotkey is registered to the network, the lowest ranked miner is removed from the network. POW registration requires a Nvidia GPU with CUDA drivers. 

- **NOTE**
    
    Each subnetwork has a cap on the number of allowed Hotkeys. If a Subnet is full and a Hotkey is registered, then the Hotkey with the lowest performing model is replaced with the newly registered Hotkey. 
    

To register a hotkey:

  1. If you are using a Nvidia GPU to register, you must also [install Cubit](https://github.com/opentensor/cubit) to enable registration to use your GPU for a faster hash rate. 
        ```
        pip install git+https://github.com/opentensor/cubit.git@v1.1.2
        ```
  2. Run the following to register a Hotkey:
        ```    
        btcli register --wallet.name <your_wallet_name> --wallet.hotkey <your_hotkey_name>
        ```
    