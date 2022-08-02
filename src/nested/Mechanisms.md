# The Consensus Mechanism

The distribution of Tao is not linear and is not determined by a single transaction.  Our consensus mechanism is designed so that nodes that are valuable in the network receive more reward at an increasing rate. Once individual scores have been determined, the network blockchain uses a [consensus algorithm](src/../Glossary.md#consensus-mechanism) to reach a common agreement over who the most valuable participants in the system are in order to reward them accordingly, while deterring the activity of malicious nodes in the network. 


Servers are rewarded based on their performance in individual instances of knowledge production, and in addition, they must prove useful to the majority of Validators in the network to optimize their earnings. Validators, on the other hand, are incentivized to collaborate with highly valuable Servers in the system who are also trusted by the majority through a bonding mechanism and a limitation in the supply of scores they are able to give.

Servers receive two separate assessments from Validators that are combined to determine their Tao inflation, thus acting as an incentive. 

- The first assessment is the [consensus score](src/../Glossary.md#consensus-mechanism), which is determined by the number of approval votes given by Validators [(trust)](src/../Glossary.md#trust). This score is not earned in a linear fashion, as Validators with more stake (Tao) are able to distribute a greater number of votes. The score is also regularized by a [sigmoid function](src/../Glossary.md#sigmoid-function): if less than 51% of the votes a Server receives are positive, the score is reduced exponentially, if more than 51% are positive, it is likewise inflated.

- This consensus score is then combined with the [rank](src/../Glossary.md#rank) - numerical determinant of representational knowledge value - achieved to determine the Server's Tao inflation. Again, this score (rank) is skewed: it is a combination of weights set by the validator and the stake of that validator.

Validators, as well, are subject to a set of conditions to incentivize right conduct in the system. 

- The first of these is the [“bonding mechanism”](src/../Glossary.md#bodning-mechanism): when Validators [rank](src/../Glossary.md#rank) a given Server, they simultaneously purchase equity in that node, and receive inflation proportional to this. Because of the [consensus mechanism](src/../Glossary.md#consensus-mechanism) previously described, Validators benefit from distributing their highest scores to Servers who are likely to be scored highly by other Validators as well - [“trusted”](src/../Glossary.md#trust) Servers. 

- In addition, Validators are limited in the number and size of scores they are allowed to distribute, and so must choose wisely where their investment is allocated: they must only choose the best and the brightest.
