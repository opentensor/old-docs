# Consensus, Incentive, and Bonding

The network blockchain uses a consensus algorithm to reach a common agreement over who the most valuable participants in the system are and reward them accordingly while encouraging honest activity and deterring collusion. Servers in the network are rewarded based on their performance in individual instances of knowledge production, in addition to earning a general agreement amongst network Validators of their usefulness. Validators, on the other hand, are incentivized to collaborate with highly valuable Servers in the system who are also trusted by the majority through a bonding mechanism and a limitation in the supply of scores they are able to give.

*Servers receive two separate assessments from Validators that are combined to determine their Tao inflation, thus acting as an incentive.*

- The first assessment is the consensus score which is determined by the number of approval votes given by validators trust. This score is not earned in a linear fashion, as Validators with more staked Tao are able to distribute a greater number of votes. The score is also regularized by a sigmoid function: if less than 51% of the votes a Server receives are positive, the score is reduced exponentially, if more than 51% are positive, it is likewise inflated. 
- This consensus score is then combined with the rank - numerical determinant of value - achieved to determine the server's Tao inflation. Again, this score (rank) is skewed: it is combination of weights set by the validator, and the stake of that validator. 


*Validators, as well, are subject to a set of conditions to incentivize right conduct in the system.*

- The first of these is the “bonding mechanism”: when Validators rank a given Server, they simultaneously purchase equity in that node, and receive inflation proportional to this. Because of the consensus mechanism previously described, Validators benefit from distributing their highest scores to Servers who are likely to be scored highly by other Validators as well - “trusted” Servers. 
- In addition, Validators are limited in the number and size of scores they are allowed to distribute, and so must choose wisely where their investment is allocated: they must only choose the best and the brightest.

