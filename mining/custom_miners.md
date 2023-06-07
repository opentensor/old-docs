---
title: Custom Miners
---
Miners must service the unique task-loads required by validators which are then evaluated 

Since the weights set by validators determine their inflation of TAO, and the and in a manner that does not over extend their ability to process those tasks, 


Since the network is competitive it is important  


For instance, by generating responses to prompts on Bittensor text subnetwork 1. In all cases, miners implement 3 core methods which determine how they respond to requests and in what order those are processed. 

1. A function which returns true if the miner will not process the request.
    ```python numbered dark
        def blacklist( self, forward_call: bittensor.Call ) -> bool:
    ```

2. A function which returns the priority of the request to be processed by the request.
    ```python numbered dark
        def priority( self, forward_call: bittensor.Call ) -> float:
    ```

3. A function which returns the task output from the passed request.
    ```python numbered dark
        def forward( self, inputs: Any ) -> Any:
    ```
