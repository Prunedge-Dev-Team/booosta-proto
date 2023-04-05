# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from booosta_proto.py_grpc import personnel_pb2 as personnel__pb2


class PersonnelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRetailerByUserId = channel.unary_unary(
                '/personnel.PersonnelService/GetRetailerByUserId',
                request_serializer=personnel__pb2.GetRetailerByUserIdRequest.SerializeToString,
                response_deserializer=personnel__pb2.GetRetailerByUserIdResponse.FromString,
                )
        self.GetAgentByUserId = channel.unary_unary(
                '/personnel.PersonnelService/GetAgentByUserId',
                request_serializer=personnel__pb2.GetAgentByUserIdRequest.SerializeToString,
                response_deserializer=personnel__pb2.GetAgentByUserIdResponse.FromString,
                )
        self.GetAggregatorByUserId = channel.unary_unary(
                '/personnel.PersonnelService/GetAggregatorByUserId',
                request_serializer=personnel__pb2.GetAggregatorByUserIdRequest.SerializeToString,
                response_deserializer=personnel__pb2.GetAggregatorByUserIdResponse.FromString,
                )


class PersonnelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetRetailerByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAggregatorByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonnelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRetailerByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRetailerByUserId,
                    request_deserializer=personnel__pb2.GetRetailerByUserIdRequest.FromString,
                    response_serializer=personnel__pb2.GetRetailerByUserIdResponse.SerializeToString,
            ),
            'GetAgentByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentByUserId,
                    request_deserializer=personnel__pb2.GetAgentByUserIdRequest.FromString,
                    response_serializer=personnel__pb2.GetAgentByUserIdResponse.SerializeToString,
            ),
            'GetAggregatorByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAggregatorByUserId,
                    request_deserializer=personnel__pb2.GetAggregatorByUserIdRequest.FromString,
                    response_serializer=personnel__pb2.GetAggregatorByUserIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'personnel.PersonnelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonnelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetRetailerByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/personnel.PersonnelService/GetRetailerByUserId',
            personnel__pb2.GetRetailerByUserIdRequest.SerializeToString,
            personnel__pb2.GetRetailerByUserIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/personnel.PersonnelService/GetAgentByUserId',
            personnel__pb2.GetAgentByUserIdRequest.SerializeToString,
            personnel__pb2.GetAgentByUserIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAggregatorByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/personnel.PersonnelService/GetAggregatorByUserId',
            personnel__pb2.GetAggregatorByUserIdRequest.SerializeToString,
            personnel__pb2.GetAggregatorByUserIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
