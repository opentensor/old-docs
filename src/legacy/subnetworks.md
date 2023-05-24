# The Bittensor Network and Subnetworks 
Bittensor's protocol rewards users with TAO tokens for valuable contributions to the network. The network comprises of Neurons and Validators. Validators evaluate Neuron performance and ensure they are being honest and running real AI models, they also rank the models on the network according to their performance and submit the ranking to the Blockchain. Neurons, on the other hand, contain models that perform a specific task on a given modality such as text, image, audio, etc. Users can either contribute by running Neurons with their own AI models or ones provided by the Bittensor codebase, or they can run Validators which evaluate Neuron responses and ensure network consensus. Both contributions serve a very important purpose and both are rewarded accordingly.

In other words, neurons receive rewards by producing valuable knowledge and being useful to the majority of the network while Validators are incentivized to collaborate with highly valuable Servers through a bonding mechanism and score restrictions.

# Subnetworks
In order to facilitate the consensus mechanism on multiple machine tasks, Bittensor utilizes a unique functionality called "Subnetworks". They are a partition of the Bittensor network dedicated to validating and building neural network models specific to a task or modality. For example, currently Subnetwork 1 is dedicated to models running prompt tasks — that is, text-based neural network models that are trained on question and answer data. More subnetworks are presently being developed such audio and image subnetworks.

To view a list of subnetworks, users can call:

```bash
btcli list_subnets
```