# The Protocol

There are two types of [nodes](src/../nested/Glossary.md#miner/neuron/peer/node) that comprise the network: [Servers](src/../nested/Glossary.md#servers) and [Validators](src/../nested/Glossary.md#validators). The Validators are tasked with “validating” the performance of the Servers, prompting them for information and assessing them according to their responses. These assessments are then relayed to the network blockchain, [Nakamoto](src/../nested/Glossary.md#nakamoto), where currency is distributed. Servers are tasked with optimizing their responses so that they can compete with other Servers in the system for positive assessments, and therefore [currency](src/../nested/Glossary.md#tao). The best preforming servers will recieve a larger portion of the limited supply of minted Tao.


Each validation process begins when a Validator locates a Server in the network and sends its [input](src/../Glossary.md#inputs) in the form of tokenized text, also referred to as [**tokens**](src/../nested/Glossary.md#tokens). The Servers will then respond with [**logits**](src/../nested/Glossary.md#logits), which represent their best attempt at [**next token prediction** (NTP)](src/../nested/Glossary.md#next-token-prediction). This constitutes the central value-producing activity of the network. The Validator will then score each Server according to their response, using a series of information-based processes and game theoretic strategies to determine the usefulness of the information received. 


The Validators are able to do this efficiently because they have the data on hand that they are serving, they already have the “answer” needed to properly assess the predicative responses they are recieving.

![logit/tokens](IntelligencePath.png)
