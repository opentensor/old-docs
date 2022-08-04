# Return Codes

The following return codes from backward and forward calls can be used for diagnosing your miner:




NoReturn = 0; Default value.

Success = 1; Succesfull query.

Timeout = 2; Request timeout.

Backoff = 3; Call triggered a backoff.

Unavailable = 4; Endpoint not available.

NotImplemented = 5; Modality not implemented.

EmptyRequest = 6; Request is empty.

EmptyResponse = 7; Response is empty.

InvalidResponse = 8; Request is invalid.

InvalidRequest = 9; Response is invalid.

RequestShapeException = 10; Request has an invalid shape.

ResponseShapeException = 11; Response has an invalid shape.

RequestSerializationException = 12; Request failed to serialize. 

ResponseSerializationException = 13; Response failed to serialize.

RequestDeserializationException = 14; Request failed to deserialize.

ResponseDeserializationException = 15; Response failed to deserialize.

NotServingNucleus = 16; Receiving Neuron is not serving a Nucleus to query.

NucleusTimeout = 17; Processing on the Server side timed out.

NucleusFull = 18; Returned when the processing queue on the Server is full.

RequestIncompatibleVersion = 19; The request handler is incompatible with the request 
version. *Request from Validator to Server.*

ResponseIncompatibleVersion = 20; The request handler is incompatible with the request version. *Response from Server to Validator.*

SenderUnknown = 21; Requester is not known by the receiver. 

UnknownException = 22; Unknown exception.

Unauthenticated = 23; Authentication failed.