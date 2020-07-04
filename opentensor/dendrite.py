from opentensor import opentensor_pb2_grpc as opentensor_grpc
from opentensor import opentensor_pb2
import opentensor

from typing import List

class Dendrite:
    def __init__(self, metagraph):
        self._metagraph = metagraph

    def forward (self, x: List[torch.Tensor], nodes: List[opentensor_pb2.Node]):
        
        version = 1.0
        source_uid = os.urandom(12)
        nounce = os.urandom(12) 
        node_ids = self._keys.toIds(keys)
     
        results = []
        for idx, tensor in enumerate(x):
            node = nodes[idx]
            
            # Create endpoint stub
            target_id = node.identity
            address = node.address + ":" + node.port
            channel = grpc.insecure_channel(address)
            stub = opentensor_grpc.OpentensorStub(channel)

            tensor = opentensor.Serializer.serialize(tensor)
            request = opentensor_pb2.TensorMessage(
                version = version,
                public_key = self._metagraph.public_key,
                target_id = target_id, 
                nounce = nounce,
                tensors = [tensor]
            )
            response = stub.Fwd(request) 
            tensor = opentensor.Serializer.deserialize(response.tensors[0])
            results.append(tensor)

        return results
     
