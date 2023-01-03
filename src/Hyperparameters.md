
| **Validator Hyperparameter**       | **Value** |
|------------------------------------|-----------|
| **AdjustmentInterval**             | 100       |
| **BlocksPerStep**                  | 100       |
| **BondsMovingAverage**             | 900,000   |
| **ImmunityPeriod**                 | 3072      |
| **IncentivePruningDenominator**    | 1         |
| **Kappa**                          | 2         |
| **MaxAllowedMaxMinRatio**          | 64        |
| **MaxAllowedUids**                 | 4096      |
| **MinAllowedWeights**              | 1024      |
| **Rho**                            | 10        |
| **StakePruningDenominator**        | 20        |
| **StakePruningMin**                | 1024      |
| **TargetRegistrationsPerInterval** | 2         |
| **ValidatorBatchSize**             | 32        |
| **ValidatorEpochLen**              | 250       |
| **ValidatorEpochsPerReset**        | 60        |
| **ValidatorSequenceLength**        | 256       |
| **ValidatorExcludeQuantile**       | 5         |
| **ScalingLawPower**                | 50        |
| **SynergyScalingLawPower**         | 60        |
| **MaxWeightLimit**                 | 17_179_868|


## AdjustmentInterval

- The interval over which we calculate the rate of new peer registrations, if the rate exceeds **TargetRegistrationsPerInterval** then the POW difficulty is doubled.

## BlocksPerStep

- The number of blocks which pass between a recalculation of incentive terms: Rank, Trust, Consensus, Incentive, Dividends, Emissions, the distribution of newly minted stake, and the calculation of the next bond matrix.

## BondsMovingAverage

- The coefficient α representing the smoothing factor during the computation of the new Bonds matrix via an exponentially weighted moving average.

## ImmunityPeriod

- How many blocks a a hotkey is immune from deregistration after joining the network.

## IncentivePruningDenominator

- Works together with the **StakePruningDenominator** to determine the ratio between stake and incentive for a minimum bound of score to keep a hotkey registered. 

## Kappa

- The temperature of sigmoid activation function to regularize Trust and become Consensus. 

## MaxAllowedMaxMinRatio

- Sets the ratio between the highest weight and lowest weight a Validator can set in one weight setting. This influences the reward skew.

## MaxAllowedUids

- How many UIDs can be registered to the network at one time.

## MinAllowedWeights

- The lower limit on the number of non zero weights a Validator sets after each epoch. Increasing **MinAllowedWeights** increases the size of the consensus set: the number of peers with greater than 50% trust.

## StakePruningDenominator

- works together with the incentivePruningDenominator, to determine the ratio between stake and incentive for a minimum bound of score to keep a hotkey registered. 

## StakePruningMin

- The threshold value which separates Servers from Validators during a pruning operation. Miners with stake greater than stakePruningMin are not pruned based on incentive.

## TargetRegistrationsPerInterval

- The target number of registrations expected each block. If the number of registrants is greater than **TargetRegistrationsPerInterval**, the difficulty of the registration will double. If the number of registrants is less than **TargetRegistrationsPerInterval**, the difficulty of the registration will be halved.

## ValidatorBatchSize

- Determines the size of each validation request sent by Validators. Each validation request has consistent state [batch size, sequence length]. Increasing batch sizes forces increased load onto Servers forcing them to improve hardware.

## ValidatorEpochLength

- Determines the number of blocks per epoch for each Validator. This parameter controls how often each Validator will set its weights.

## ValidatorEpochsPerReset	

- When active, Validators can reset their local scoring storage and start scoring without previous history.

## ValidatorSequenceLength

- Determines the size of each validation request sent by Validators. Each validation request has a consistent state [batch size, sequence length]. Increasing sequence length forces increased load onto Servers forcing them to improve hardware.

## ValidatorExcludeQuantile

- Validators exclude from weight setting the lowest quantile or percentile performing Servers recorded locally.

## ScalingLawPower	

- Adjusts through a power coefficient the estimated number of model parameters.

## SynergyScalingLawPower

- Adjusts through a power coefficient the estimated number of model parameters due to synergy.

## MaxWeightLimit

- The maximum weight a Validator is allowed to set on a Server.


