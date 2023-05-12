# Run a Validator

Validators on the Bittensor network ensure that Neurons are honest and that the best Neurons are rewarded according to their performance. 

It is important to distinguish a Bittensor validator from a traditional Blockchain validator. Bittensor verifiers contain a [Mixture-of-Experts](https://arxiv.org/abs/1701.06538) gating layer as well as a reward model to ensure that the right [Neuron](https://www.notion.so/Run-a-Neuron-78088891b9914b7f9ec510d41d3ebda6) gets rewarded accordingly. However, they are not involved in verifying transactions and enforcing the consensus mechanism. This is handled by the traditional Blockchain validator that runs Subtensor.

Similarly to the Model Neurons, the Validator Neuron is located under `neurons` [on the Bittensor repository](https://github.com/opentensor/bittensor/blob/text_prompting/neurons/text/prompting/validators/core/neuron.py).  You can run the validator using the following, where `--netuid 1` specifies the validator to be run on Subnetwork 1.

```bash

python3 ~/.bittensor/bittensor/neurons/text/prompting/validators/core/neuron.py --netuid 1

```