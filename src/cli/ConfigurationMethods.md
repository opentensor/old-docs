# Configuring a miner

There are three ways to configure your miner:

1. Command line arguments
2. Configuration file
3. Environment variables

Command line arguments take the highest priority with environmental variables being the lowest.
- Command Line —> Config —> Environment Variables

## Command line arguments

Command line arguments take the form of flags and can be strung to your miner run command.

For example, specify which port to use:
```bash
btcli run --axon.port <>
```

[Full list of command line arguments](../Arguments.md)

## Configuration file

Another way to configure your miner is through the configuration file. To call upon a configuration file, pass:

```bash
--congig <path_to_congiguration_file>
# e.g.
btcli run --config my_config_directory/my_custom_config_file.txt
```

[Refer to sample configuration files](https://github.com/opentensor/bittensor/tree/master/sample_configs)


## Environment variables

The final way to configure a miner is through environment variables.

All environment variables have the same structure:

```
BT_<object name>_<parameter name>
```

To change an environment variable:

```
export BT_VARIABLE_I_WISH_TO_CHANGE=<>
```

For example, if you wanted to specify the default port to 3000:

```
export BT_AXON_PORT=3000
```

[Full list of environment variables](../Arguments.md)





