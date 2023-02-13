# Taonomics

Tao is the token for Bittensor and gatekeeps access, representing bandwidth to the network. The supply of Tao follows the same emission cycle as Bitcoin, with a max supply of 21,000,000 and a halving cycle every four years. After each cycle, emissions per block decrease by 50%. Currently, one Tao is issued every block (12 seconds). The first halving will be October 2025.

\\[ \frac{\sum _{i=0}^{32}210000\left[\frac{50*10^8}{2^i}\right]}{10^8} \\]



# Emission Split

Servers and Validators evenly split emissions per block, with the most emissions issued to the best-performing miners.


# Validation and B (Bonds)

The Validators determine the proportion of emissions received by each Server in the network. Validators, responsible for validating the action of Servers, assign rankings to Servers based on their performance. In doing so, Validators accumulate bonded relationships in the Servers they rank. Unlike traditional bonding, our bonding is defined by:

\\[ {\Delta}{B}={W}*{S} \\]

In this way, peers accumulate bonds in the peers they rank, thus ’bonding’ themselves to those that they are connected to.

\\[ {\Delta}B_{t+1}={B_t}+{W}*{S} \\]

Validators attempting to form a cabal or collude with other Validators will see the size of their bonds diminish. This attack is only possible if the cabal holds more than 50% of the Validation stake in the network. Servers that have yet to reach Consensus recieve exponentially fewer emissions than those that have.



# T (Trust)

Trust is the measurement of the number of non-zero rankings Servers receive from Validators. 



# C (Conensus)

Consensus is defined using a continuous sigmoid function. This sigmoid produces threshold-like scaling, which rewards connected and well-performing Servers and punishes the non-trusted. 

\\[ {C}={σ}({\rho}({T^T}*{S}-{0.5})) \\]


Servers who have reached ‘Consensus’ are peers with non-zero rankings from more than 50% of the Validation stake in the network. 

\\[ ({T^T}*{S})>{0.5} \\]



# I (Incentive) + Emissions

As Servers attain more weight in the network they increase their inflation exponentially up to 0.5 

\\[ {I}={R}*{C} \\]

Using the bond matrix, the chain distributes Incentive scores to ensure that each Server receives a fixed proportion of emission in line with their performance in the network.

\\[{\Delta}S=0.5B^T*I+0.5I \\]


**KEY**
---
B = Bonds

C = Consensus

I = Incentive

R = Rank

S = Stake

T = Trust

W = Weight
