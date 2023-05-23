# Return Codes
As the Bittensor Network operates on GRPC, the following is a list of response codes that validators can return on the API or in the logs.

| Code | Name                             | Message                                                                                                    |
|------|----------------------------------|------------------------------------------------------------------------------------------------------------|
| 0    | NoReturn                         | Default Value                                                                                              |
| 1    | Success                          | Successful Query                                                                                           |
| 2    | Timeout                          | Request Timeout                                                                                            |
| 3    | Backoff                          | Call Triggered a backoff                                                                                   |
| 4    | Unavailable                      | Endpoint not available                                                                                     |
| 5    | NotImplemented                   | Modality is not implemented                                                                                |
| 6    | EmptyRequest                     | Request is empty                                                                                           |
| 7    | EmptyResponse                    | Response is empty                                                                                          |
| 8    | InvalidRequest                   | Request is invalid                                                                                         |
| 9    | InvalidResponse                  | Response is invalid                                                                                        |
| 10   | RequestShapeException            | Request has an invalid tensor shape                                                                        |
| 11   | ResponseShapeException           | Response has an invalid tensor shape                                                                       |
| 12   | RequestSerializationException    | Request has failed to serialize properly.                                                                  |
| 13   | ResponseSerializationException   | Response has failed to serialize properly.                                                                 |
| 14   | RequestDeserializationException  | Request has failed to deserialize properly.                                                                |
| 15   | ResponseDeserializationException | Response has failed to deserialize properly.                                                               |
| 16   | NotServingNucleus                | Receiving neuron is not serving a blockchain (nucleus) to query.                                           |
| 17   | NucleusTimeout                   | Processing on the Neuron's side has timed out.                                                             |
| 18   | NucleusFull                      | Processing Queue on the Neuron is full.                                                                    |
| 19   | RequestIncompatibleVersion       | The request handler is incompatible with the request version (for requests going from Validator to Server) |
| 20   | ResponseIncompatibleVersion      | The response handler is incompatible with the response version (for response from Server to Validator)     |
| 21   | SenderUnknown                    | Requester unknown by the receiver                                                                          |
| 22   | UnknownException                 | An unknown exception has occurred.                                                                         |
| 23   | Unauthenticated                  | Authentication failed on the GRPC channel.                                                                 |