
<Accordion title="Logging">









title: bt.logging

# Logging Reference Documentation


## Introduction
The `Logging` interfaces with bittensor internal logging system.

## Examples
```python dark
import bittensor as bt

# Turn on debug logs
bt.debug()

# Turn on trace logs
bt.trace()

# Turn off debug logs
bt.set_debug(False)

# Turn off trace logs
bt.set_trace(False)

# Turn on logging from class definition
bt.logging( set_debug = True )

# Instantiate logging from command line args
bt.logging( bt.logging.config() )

# Turn on logging to file
bt.logging( record_log = True, logging_dir = '/path/to/logs/' )

# Log
bt.logging.info(message)
bt.logging.debug(message)
bt.logging.trace(message)
bt.logging.success(message)
bt.logging.critical(message)
bt.logging.error(message)
>>> 2023-05-29 09:27:25.426 |       INFO       | message

# Log using prefex suffix design
bt.logging.info(prefix, message)
bt.logging.debug(prefix, message)
bt.logging.trace(prefix, message)
bt.logging.success(prefix, message)
bt.logging.critical(prefix, message)
bt.logging.error(prefix, message)
>>> 2023-05-29 09:27:47.184 |       INFO       | cat                           dogs
```








</Accordion>
