# Running locally - Subtensor
--- 
Subtensor is our network blockchain and keeps a record of every transaction that occurs. A new block is created and recorded every 12 seconds - or "blockstep" - at which time a new round of Tao is distributed. 


By connecting to Nakamoto, you automatically gain access to Subtensor. Running a Subtensor instance locally, however, will ensure a faster and more consistent experience in the case that the network is compromised or slowed by high traffic. It is therefore **highly** recommended to run Subtensor locally for serious miners.



## Running Subtensor 

*Should any of the below commands fail, try running with sudo.*

1. Prepare your system by updating outdated packages in your system, and installing the newest available ones. You can do this in two commands. 


```bash
apt-get update
```

```bash
apt-get upgrade
```

2. Download Docker.

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

3. Make the Docker install script executable.

```bash
chmod +x ./get-docker.sh
```

4. Install Docker. For more information, follow this [link](https://www.docker.com/).

```bash
./get-docker.sh
```

5. Clone the Subtensor repository.

```bash
git clone https://github.com/opentensor/subtensorv3.git
```

6. Open the Subtensor directory.

```bash
cd subtensorv3
```

7. Pull the latest Subtensor image.

```bash
docker pull opentensor/subtensor
```

8. Run Subtensor inside of Docker.

```bash
docker compose up -d
```

9. Check that Subtensor is fully synced.


```bash
docker logs --since=1h node-subtensor 2>&1  | grep "best"
```


Here is an example of a synced copy of Subtensor:


```bash
/node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50564.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50568.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50572.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50576.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50580.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50584.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50588.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50592.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50596.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50600.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50604.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50608.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50612.    
node-subtensor    | 2022-04-27 01:32:22 Accepted a new tcp connection from 172.22.0.1:50616. 
```


In case your Subtensor goes down, here is the command to restart it: 


```bash
# quick restart
cd subtensorv3 && \
docker-compose down && \
docker-compose up -d

# full restart
cd subtensorv3 && \
docker-compose down && \
docker system prune -a -f && \
git pull && \
docker pull opentensor/subtensor && \
docker-compose up -d
```


Lastly, here are the steps to ensure both Bittensor and Subtensor are up to date. 


Update Bittensor: 


```bash
git -C ~/.bittensor/bittensor pull origin master
python3 -m pip install -e ~/.bittensor/bittensor
```


Update Subtensor: 


```bash
#Bring Subtensor down
docker compose down
#Connect to directory
cd subtensorv3
#update Subtensor
git pull
#Bring Subtensor back up 
docker compose up -d
```
