# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import user_pb2 as user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserById = channel.unary_unary(
                '/user.UserService/GetUserById',
                request_serializer=user__pb2.GetUserByIdRequest.SerializeToString,
                response_deserializer=user__pb2.GetUserByIdResponse.FromString,
                )
        self.SaveAuditLog = channel.unary_unary(
                '/user.UserService/SaveAuditLog',
                request_serializer=user__pb2.SaveAuditLogRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveAuditLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=user__pb2.GetUserByIdRequest.FromString,
                    response_serializer=user__pb2.GetUserByIdResponse.SerializeToString,
            ),
            'SaveAuditLog': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveAuditLog,
                    request_deserializer=user__pb2.SaveAuditLogRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/GetUserById',
            user__pb2.GetUserByIdRequest.SerializeToString,
            user__pb2.GetUserByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveAuditLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/SaveAuditLog',
            user__pb2.SaveAuditLogRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
