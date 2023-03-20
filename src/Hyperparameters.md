
| **Validator Hyperparameters**       | **Value**       |
|------------------------------------|-----------------|
| **Rho**                            | 10              |
| **Kappa**                          | 32_767          |
| **MaxAllowedUids**                 | 4096            |
| **Issuance**                       | 0               |
| **MinAllowedWeights**              | 1024            |
| **EmissionValue**                  | 1_000_000_000   |
| **MaxWeightsLimit**                | 1000            |
| **ValidatorBatchSize**             | 32              |
| **ValidatorSequenceLen**           | 256             |
| **ValidatorEpochLen**              | 100             |
| **ValidatorEpochsPerReset**        | 60              |
| **ValidatorExcludeQuantile**       | 6554            |
| **ValidatorPruneLen**              | 1               |
| **ValidatorLogitsDivergence**      | 1310            |
| **ScalingLawPower**                | 50              |
| **SynergyScalingLawPower**         | 50              |
| **MaxAllowedValidators**           | 128             |
| **Tempo**                          | 99              |
| **Difficulty**                     | 10_000_000      |
| **AdjustmentInterval**             | 100             |  
| **TargetRegistrationsPerInterval** | 2               |
| **ImmunityPeriod**                 | 4096            |
| **ActivityCutoff**                 | 5000            |
| **MaxRegistrationsPerBlock**       | 1               |
| **PruningScore**                   | MAX             |
| **BondsMovingAverage**             | 900_000         |
| **DefaultTake**                    | 11_796          |
| **WeightsVersionKey**              | 370             |
| **MinDifficulty**                  | 10_000_000      |
| **MaxDifficulty**                  | 4               |
| **ServingRateLimit**               | 50              |         
| **Burn**                           | 100_000_000_000 |
| **MinBurn**                        | 1_000_000_000   |
| **MaxBurn**                        | 100_000_000_000 |
| **TxRateLimit**                    | 1000            |


## AdjustmentInterval

- The interval over which we calculate the rate of new peer registrations, if the rate exceeds **TargetRegistrationsPerInterval** then the POW difficulty is doubled.

## BondsMovingAverage

- The coefficient α representing the smoothing factor during the computation of the new Bonds matrix via an exponentially weighted moving average.

## ImmunityPeriod

- How many blocks a a hotkey is immune from deregistration after joining the network.

## Kappa

- The temperature of sigmoid activation function to regularize Trust and become Consensus. 

## MaxAllowedUids

- How many UIDs can be registered to the network at one time.

## MinAllowedWeights

- The lower limit on the number of non zero weights a Validator sets after each epoch. Increasing **MinAllowedWeights** increases the size of the consensus set: the number of peers with greater than 50% trust.

## TargetRegistrationsPerInterval

- The target number of registrations expected each block. If the number of registrants is greater than **TargetRegistrationsPerInterval**, the difficulty of the registration will double. If the number of registrants is less than **TargetRegistrationsPerInterval**, the difficulty of the registration will be halved.

## ValidatorBatchSize

- Determines the size of each validation request sent by Validators. Each validation request has consistent state [batch size, sequence length]. Increasing batch sizes forces increased load onto Servers forcing them to improve hardware.

## ValidatorEpochLength

- Determines the number of blocks per epoch for each Validator. This parameter controls how often each Validator will set its weights.

## ValidatorEpochsPerReset	

- When active, Validators can reset their local scoring storage and start scoring without previous history.

## ValidatorSequenceLen

- Determines the size of each validation request sent by Validators. Each validation request has a consistent state [batch size, sequence length]. Increasing sequence length forces increased load onto Servers forcing them to improve hardware.

## ValidatorExcludeQuantile

- Validators exclude from weight setting the lowest quantile or percentile performing Servers recorded locally.

## ScalingLawPower	

- Adjusts through a power coefficient the estimated number of model parameters.

## SynergyScalingLawPower

- Adjusts through a power coefficient the estimated number of model parameters due to synergy.



