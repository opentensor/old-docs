
| **Validator Hyperparameter**       | **Value** |
|------------------------------------|-----------|
| **adjustmentInterval**             | 100       |
| **blocksPerStep**                  | 100       |
| **bondsMovingAverage**             | 900,000   |
| **immunityPeriod**                 | 3072      |
| **incentivePruningDenominator**    | 1         |
| **kappa**                          | 2         |
| **maxAllowedMaxMinRatio**          | 64        |
| **maxAllowedUids**                 | 4096      |
| **minAllowedWeights**              | 1024      |
| **rho**                            | 10        |
| **stakePruningDenominator**        | 20        |
| **stakePruningMin**                | 1024      |
| **targetRegistrationsPerInterval** | 2         |
| **validatorBatchSize**             | 32        |
| **validatorEpochLen**              | 250       |
| **validatorEpochsPerReset**        | 60        |
| **validatorSequenceLength**        | 256       |
| **validatorExcludeQuantile**       | 5         |
| **scalingLawPower**                | 50        |
| **synergyScalingLawPower**         | 60        |
| **MaxWeightLimit**                 | 17_179_868|


## adjustmentInterval

- The interval over which we calculate the rate of new peer registrations, if the rate exceeds **targetRegistrationsPerInterval** then the POW difficulty is doubled.

## blocksPerStep

- The number of blocks which pass between a recalculation of incentive terms: Rank, Trust, Consensus, Incentive, Dividends, Emissions, the distribution of newly minted stake, and the calculation of the next bond matrix.

## bondsMovingAverage

- The coefficient α representing the smoothing factor during the computation of the new Bonds matrix via an exponentially weighted moving average.

## immunityPeriod

- How many blocks a a hotkey is immune from deregistration after joining the network.

## incentivePruningDenominator

- Works together with the stakePruningDenominator to determine the ratio between stake and incentive for a minimum bound of score to keep a hotkey registered. 

## kappa

- The temperature of sigmoid activation function to regularize Trust and become Consensus. 

## maxAllowedMaxMinRatio

- Sets the ratio between the highest weight and lowest weight a Validator can set in one weight setting. This influences the reward skew.

## maxAllowedUids

- How many UIDs can be registered to the network at one time.

## minAllowedWeights

- The lower limit on the number of non zero weights a Validator sets after each epoch. Increasing minAllowedWeights increases the size of the consensus set: the number of peers with greater than 50% trust.

## stakePruningDenominator

- works together with the incentivePruningDenominator, to determine the ratio between stake and incentive for a minimum bound of score to keep a hotkey registered. 

## stakePruningMin

- The threshold value which separates Servers from Validators during a pruning operation. Miners with stake greater than stakePruningMin are not pruned based on incentive.

## targetRegistrationsPerInterval

- The target number of registrations expected each block. If the number of registrants is greater than **targetRegistrationsPerInterval**, the difficulty of the registration will double. If the number of registrants is less than **targetRegistrationsPerInterval**, the difficulty of the registration will be halved.

## validatorBatchSize

- Determines the size of each validation request sent by Validators. Each validation request has consistent state [batch size, sequence length]. Increasing batch sizes forces increased load onto Servers forcing them to improve hardware.

## validatorEpochLength

- Determines the number of blocks per epoch for each Validator. This parameter controls how often each Validator will set its weights.

## validatorSequenceLength

- Determines the size of each validation request sent by Validators. Each validation request has a consistent state [batch size, sequence length]. Increasing sequence length forces increased load onto Servers forcing them to improve hardware.
