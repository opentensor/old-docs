# Installation

Bittensor installation requires two installations: Bittensor and Subtensor. Bittensor is the python-based machine learning layer, whereas Subtensor is the rust-based blockchain consensus layer. They must run concurrently for each model.

- **NOTE**

    It is highly recommend to **install Bittensor first** and then install Subtensor.


## Installing Bittensor

There are three ways to install Bittensor.

1. Using the installer script. This is the easiest method and is recommended if you are new. Simply paste the following into your terminal.

    ```bash
    /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh](https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh))
    ```

2. Using pip.

    ```bash
    pip3 install bittensor
    ```

3. From source.

    ```bash
    git clone [https://github.com/opentensor/bittensor.git](https://github.com/opentensor/bittensor.git)
    $ python3 -m pip install -e bittensor/
    ```


Once installed, you can verify your installation by running the [Bittensor Command Line Interface](/documentation/btcli) (CLI) with `btcli --help`. The Bittensor CLI is the primary tool for interfacing with the Bittensor network.

## Run Subtensor on Docker

Subtensor can be run straight through the included Docker container. This is the fastest and most reliable method to run Subtensor as Docker takes care of all required setup.

1. Clone the Subtensor repository.

    ```bash
    git clone https://github.com/opentensor/subtensor.git ~/.bittensor
    ```

    This will clone the Subtensor repository to `~/.bittensor`.

2. Run Subtensor in a Docker container.

    ```bash
    cd ~/.bittensor/subtensor && docker-compose up -d
    ```

    This will run the blockchain in a Docker container, and will take about 5 minutes to fully synchronize with the rest of the network before it is useable.


## Run Subtensor Natively

You can also run Subtensor natively, this has a few advantages as it will run faster than a Docker container and allows you to use specific flags.

1. [Install Rust locally.](https://www.rust-lang.org/tools/install)

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

2. Install the correct nightly toolchain.

    ```bash
    cd ~/.bittensor/subtensor && ./scripts/init.sh
    ```

3. Build and compile Subtensor. This process will take a long time.

    ```bash
    cargo build --release --features runtime-benchmarks
    ```

4. Simply copy/paste the line to run Subtensor from `docker-compose.yml`
