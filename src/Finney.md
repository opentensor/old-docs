# Finney - Everything New



# Delegating

Any hotkey may nominate themselves as a delegate and receive stake delegations from other wallets in the network. Key owners of delegates collect an 18% "take" on emissions of all delegated Tao. 
Learn more [here](Delegation.md)


## Turn your hotkey into a delegate:
```
btcli nonminate
```

## Stake to a delegate account:
```
btcli delegate
```

## List all the delagates in the network
```
btcli list_delegates
```



# Subnetworks

Hotkeys can register to multiple networks concurrently. Each network has its own consensus mechanism and UID slots. There is a base net that hotkeys must first pass before entering any of the primary networks. For now, there is only one primary net. 

Hotkeys must achieve a ranking greater than or equal to the minimum emission threshold and solve a secondary POW before entering a primary net. Once admitted to the primary network, the hotkey from the base network will continue serving alongside its new primary net counterpart, and the two will share the same axon and IP. A base network key that drops out of the emission threshold or loses registration will not affect the primary net key counterpart. However, should the primary net key lose registration, the base net key will have to be brought back into the minimum emission threshold before the primary net key can regain entry.



## List all networks:
```
btcli list_subnets
```


