# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kikimr.public.api.protos import ydb_monitoring_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2


class MonitoringServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SelfCheck = channel.unary_unary(
                '/Ydb.Monitoring.V1.MonitoringService/SelfCheck',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckResponse.FromString,
                )


class MonitoringServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SelfCheck(self, request, context):
        """Gets the health status of the database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitoringServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SelfCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCheck,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.Monitoring.V1.MonitoringService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MonitoringService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SelfCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Monitoring.V1.MonitoringService/SelfCheck',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.SelfCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
