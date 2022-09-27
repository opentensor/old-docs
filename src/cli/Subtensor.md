# Running locally - Subtensor
--- 
Subtensor is our network blockchain and keeps a record of every transaction that occurs. A new block is created and recorded every 12 seconds - or "blockstep" - at which time a new round of Tao is distributed. 


By connecting to Nakamoto, you automatically gain access to Subtensor. Running a Subtensor instance locally, however, will ensure a faster and more consistent experience in the case that the network is compromised or slowed by high traffic. It is therefore **highly** recommended to run Subtensor locally for serious miners.



## Running Subtensor 


1. Prepare your system by updating outdated packages in your system, and installing the newest available ones. You can do this in two commands. 


```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade
```

2. Grant permmissions to use Docker.

```bash
chmod +x ./get-docker.sh
```

3. Install Docker. For more information, follow this [link](https://www.docker.com/).

```bash
sudo ./get-docker.sh
```

4. Clone the Subtensor repository

```bash
git clone https://github.com/opentensor/subtensor.git ~/.bittensor/subtensor
```

5. Open the Subtensor directory 

```bash
cd ~/.bittensor/subtensor
```

6. Pull the latest Subtensor image

```bash
sudo docker pull opentensorfdn/subtensor
```

7. Run Subtensor inside of Docker 

```bash
sudo docker compose up -d
```

8. Check that Subtensor is fully synced


```bash
sudo docker logs --since=1h node-subtensor 2>&1  | grep "best"
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
cd ~/.bittensor/subtensor && \
/usr/local/bin/docker-compose down && \
/usr/local/bin/docker-compose up -d

# full restart
cd ~/.bittensor/subtensor && \
/usr/local/bin/docker-compose down && \
docker system prune -a -f && \
git -C ~/.bittensor/subtensor pull origin master && \
docker pull opentensorfdn/subtensor && \
/usr/local/bin/docker-compose up -d
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
sudo docker compose down
#Connect to directory
cd ~/.bittensor/subtensor
#update Subtensor
sudo git pull
#Bring Subtensor back up 
sudo docker compose up -d
```
