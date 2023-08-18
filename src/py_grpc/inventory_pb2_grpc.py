# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from booosta_proto.py_grpc import inventory_pb2 as inventory__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProductInventoryById = channel.unary_unary(
                '/inventory.InventoryService/GetProductInventoryById',
                request_serializer=inventory__pb2.GetProductInventoryByIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetProductInventoryByIdResponse.FromString,
                )
        self.GetUnitTypeById = channel.unary_unary(
                '/inventory.InventoryService/GetUnitTypeById',
                request_serializer=inventory__pb2.GetUnitTypeByIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetUnitTypeByIdResponse.FromString,
                )
        self.GetProductInventoryByUserIDAndQuantity = channel.unary_unary(
                '/inventory.InventoryService/GetProductInventoryByUserIDAndQuantity',
                request_serializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.SerializeToString,
                response_deserializer=inventory__pb2.ProductInventoryListResponse.FromString,
                )
        self.GetProductInventoryByUserId = channel.unary_unary(
                '/inventory.InventoryService/GetProductInventoryByUserId',
                request_serializer=inventory__pb2.GetProductInventoryByUserIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.ProductInventoryListResponse.FromString,
                )
        self.GetRetailerProductList = channel.unary_unary(
                '/inventory.InventoryService/GetRetailerProductList',
                request_serializer=inventory__pb2.GetRetailerProductListRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetRetailerProductListResponse.FromString,
                )
        self.GetAllProductInventories = channel.unary_unary(
                '/inventory.InventoryService/GetAllProductInventories',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=inventory__pb2.ProductInventoryListResponse.FromString,
                )
        self.ChangeProductInventoryCount = channel.unary_unary(
                '/inventory.InventoryService/ChangeProductInventoryCount',
                request_serializer=inventory__pb2.ChangeProductInventoryCountRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetProductInventoryByIdResponse.FromString,
                )
        self.UpdateProductInventoryById = channel.unary_unary(
                '/inventory.InventoryService/UpdateProductInventoryById',
                request_serializer=inventory__pb2.UpdateProductInventoryByIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.UpdateProductInventoryByIdResponse.FromString,
                )
        self.RemoveProductInventoryFromCartById = channel.unary_unary(
                '/inventory.InventoryService/RemoveProductInventoryFromCartById',
                request_serializer=inventory__pb2.RemoveProductInventoryFromCartByIdRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProductInventoryById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUnitTypeById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductInventoryByUserIDAndQuantity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductInventoryByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRetailerProductList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllProductInventories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeProductInventoryCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProductInventoryById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveProductInventoryFromCartById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProductInventoryById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductInventoryById,
                    request_deserializer=inventory__pb2.GetProductInventoryByIdRequest.FromString,
                    response_serializer=inventory__pb2.GetProductInventoryByIdResponse.SerializeToString,
            ),
            'GetUnitTypeById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnitTypeById,
                    request_deserializer=inventory__pb2.GetUnitTypeByIdRequest.FromString,
                    response_serializer=inventory__pb2.GetUnitTypeByIdResponse.SerializeToString,
            ),
            'GetProductInventoryByUserIDAndQuantity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductInventoryByUserIDAndQuantity,
                    request_deserializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.FromString,
                    response_serializer=inventory__pb2.ProductInventoryListResponse.SerializeToString,
            ),
            'GetProductInventoryByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductInventoryByUserId,
                    request_deserializer=inventory__pb2.GetProductInventoryByUserIdRequest.FromString,
                    response_serializer=inventory__pb2.ProductInventoryListResponse.SerializeToString,
            ),
            'GetRetailerProductList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRetailerProductList,
                    request_deserializer=inventory__pb2.GetRetailerProductListRequest.FromString,
                    response_serializer=inventory__pb2.GetRetailerProductListResponse.SerializeToString,
            ),
            'GetAllProductInventories': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllProductInventories,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=inventory__pb2.ProductInventoryListResponse.SerializeToString,
            ),
            'ChangeProductInventoryCount': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeProductInventoryCount,
                    request_deserializer=inventory__pb2.ChangeProductInventoryCountRequest.FromString,
                    response_serializer=inventory__pb2.GetProductInventoryByIdResponse.SerializeToString,
            ),
            'UpdateProductInventoryById': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProductInventoryById,
                    request_deserializer=inventory__pb2.UpdateProductInventoryByIdRequest.FromString,
                    response_serializer=inventory__pb2.UpdateProductInventoryByIdResponse.SerializeToString,
            ),
            'RemoveProductInventoryFromCartById': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveProductInventoryFromCartById,
                    request_deserializer=inventory__pb2.RemoveProductInventoryFromCartByIdRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inventory.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProductInventoryById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetProductInventoryById',
            inventory__pb2.GetProductInventoryByIdRequest.SerializeToString,
            inventory__pb2.GetProductInventoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUnitTypeById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetUnitTypeById',
            inventory__pb2.GetUnitTypeByIdRequest.SerializeToString,
            inventory__pb2.GetUnitTypeByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductInventoryByUserIDAndQuantity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetProductInventoryByUserIDAndQuantity',
            inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.SerializeToString,
            inventory__pb2.ProductInventoryListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductInventoryByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetProductInventoryByUserId',
            inventory__pb2.GetProductInventoryByUserIdRequest.SerializeToString,
            inventory__pb2.ProductInventoryListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRetailerProductList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetRetailerProductList',
            inventory__pb2.GetRetailerProductListRequest.SerializeToString,
            inventory__pb2.GetRetailerProductListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllProductInventories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetAllProductInventories',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            inventory__pb2.ProductInventoryListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeProductInventoryCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/ChangeProductInventoryCount',
            inventory__pb2.ChangeProductInventoryCountRequest.SerializeToString,
            inventory__pb2.GetProductInventoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProductInventoryById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/UpdateProductInventoryById',
            inventory__pb2.UpdateProductInventoryByIdRequest.SerializeToString,
            inventory__pb2.UpdateProductInventoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveProductInventoryFromCartById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/RemoveProductInventoryFromCartById',
            inventory__pb2.RemoveProductInventoryFromCartByIdRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)