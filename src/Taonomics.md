# Taokenomics

Tao is the token for Bittensor and gatekeeps access, representing bandwidth to the network. The supply of Tao follows the same emission cycle as Bitcoin, with a max supply of 21,000,000 and a halving cycle every four years. After each cycle, emissions per block decrease by 50%. Currently, one Tao is issued every block (12 seconds). The first halving will be October 2025.

\\[ \frac{\sum _{i=0}^{32}210000\left[\frac{50*10^8}{2^i}\right]}{10^8} \\]



# Emission Split

Servers and Validators evenly split emissions per block, with the most emissions issued to the best-performing miners.



# Validation

Validators determine the proportion of emissions received by each Server in the network. Validators, who are responsible for validating the action of Servers, assign rankings to Servers based on their performance. In doing so, Validators accumulate bonds in the Servers they rank. The more stake held by a Validator, the more weight their rankings carry. This bonding mechanism creates an incentive for Validators to rank and bond with Servers expected to perform well by the majority of Validation stake in the network, similar to making a marked-based speculation on a traditional financial entity. 

Validators attempting to form a cabal or collude with other Validators will see the value of their bonds diminish. This attack is only possible if the cabal holds more than 50% of the Validation stake in the network, as Servers that have yet to reach Consensus earn exponentially fewer emissions than those that have.



# Trust

Trust is the measurement of the number of non-zero rankings Servers receive from Validators. 



# Conensus

Consensus is defined using a continuous sigmoid function. This sigmoid produces threshold-like scaling, which rewards connected and well-performing Servers and punishes the non-trusted. 

\\[ {C}={σ}(({T^T}*{S}-{0.5})) \\]


Servers who have reached ‘Consensus’ are peers with non-zero rankings from more than 50% of the Validation stake in the network. 

\\[ ({T^T}*{S})>{0.5} \\]



# Incentive + Emissions

\\[ {I}={R}*{C} \\]

Due to threshold like sigmoid rewards, the majority of Incentive distributes to Servers trusted by the majority stake in the network. 

\\[ {Server} {Emissions}=({I}/{2})*{100} \\]




