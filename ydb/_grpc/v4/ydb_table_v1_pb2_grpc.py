# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ydb._grpc.v4.protos import ydb_table_pb2 as protos_dot_ydb__table__pb2


class TableServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
                '/Ydb.Table.V1.TableService/CreateSession',
                request_serializer=protos_dot_ydb__table__pb2.CreateSessionRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.CreateSessionResponse.FromString,
                )
        self.DeleteSession = channel.unary_unary(
                '/Ydb.Table.V1.TableService/DeleteSession',
                request_serializer=protos_dot_ydb__table__pb2.DeleteSessionRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.DeleteSessionResponse.FromString,
                )
        self.KeepAlive = channel.unary_unary(
                '/Ydb.Table.V1.TableService/KeepAlive',
                request_serializer=protos_dot_ydb__table__pb2.KeepAliveRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.KeepAliveResponse.FromString,
                )
        self.CreateTable = channel.unary_unary(
                '/Ydb.Table.V1.TableService/CreateTable',
                request_serializer=protos_dot_ydb__table__pb2.CreateTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.CreateTableResponse.FromString,
                )
        self.DropTable = channel.unary_unary(
                '/Ydb.Table.V1.TableService/DropTable',
                request_serializer=protos_dot_ydb__table__pb2.DropTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.DropTableResponse.FromString,
                )
        self.AlterTable = channel.unary_unary(
                '/Ydb.Table.V1.TableService/AlterTable',
                request_serializer=protos_dot_ydb__table__pb2.AlterTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.AlterTableResponse.FromString,
                )
        self.CopyTable = channel.unary_unary(
                '/Ydb.Table.V1.TableService/CopyTable',
                request_serializer=protos_dot_ydb__table__pb2.CopyTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.CopyTableResponse.FromString,
                )
        self.CopyTables = channel.unary_unary(
                '/Ydb.Table.V1.TableService/CopyTables',
                request_serializer=protos_dot_ydb__table__pb2.CopyTablesRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.CopyTablesResponse.FromString,
                )
        self.RenameTables = channel.unary_unary(
                '/Ydb.Table.V1.TableService/RenameTables',
                request_serializer=protos_dot_ydb__table__pb2.RenameTablesRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.RenameTablesResponse.FromString,
                )
        self.DescribeTable = channel.unary_unary(
                '/Ydb.Table.V1.TableService/DescribeTable',
                request_serializer=protos_dot_ydb__table__pb2.DescribeTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.DescribeTableResponse.FromString,
                )
        self.ExplainDataQuery = channel.unary_unary(
                '/Ydb.Table.V1.TableService/ExplainDataQuery',
                request_serializer=protos_dot_ydb__table__pb2.ExplainDataQueryRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ExplainDataQueryResponse.FromString,
                )
        self.PrepareDataQuery = channel.unary_unary(
                '/Ydb.Table.V1.TableService/PrepareDataQuery',
                request_serializer=protos_dot_ydb__table__pb2.PrepareDataQueryRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.PrepareDataQueryResponse.FromString,
                )
        self.ExecuteDataQuery = channel.unary_unary(
                '/Ydb.Table.V1.TableService/ExecuteDataQuery',
                request_serializer=protos_dot_ydb__table__pb2.ExecuteDataQueryRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ExecuteDataQueryResponse.FromString,
                )
        self.ExecuteSchemeQuery = channel.unary_unary(
                '/Ydb.Table.V1.TableService/ExecuteSchemeQuery',
                request_serializer=protos_dot_ydb__table__pb2.ExecuteSchemeQueryRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ExecuteSchemeQueryResponse.FromString,
                )
        self.BeginTransaction = channel.unary_unary(
                '/Ydb.Table.V1.TableService/BeginTransaction',
                request_serializer=protos_dot_ydb__table__pb2.BeginTransactionRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.BeginTransactionResponse.FromString,
                )
        self.CommitTransaction = channel.unary_unary(
                '/Ydb.Table.V1.TableService/CommitTransaction',
                request_serializer=protos_dot_ydb__table__pb2.CommitTransactionRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.CommitTransactionResponse.FromString,
                )
        self.RollbackTransaction = channel.unary_unary(
                '/Ydb.Table.V1.TableService/RollbackTransaction',
                request_serializer=protos_dot_ydb__table__pb2.RollbackTransactionRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.RollbackTransactionResponse.FromString,
                )
        self.DescribeTableOptions = channel.unary_unary(
                '/Ydb.Table.V1.TableService/DescribeTableOptions',
                request_serializer=protos_dot_ydb__table__pb2.DescribeTableOptionsRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.DescribeTableOptionsResponse.FromString,
                )
        self.StreamReadTable = channel.unary_stream(
                '/Ydb.Table.V1.TableService/StreamReadTable',
                request_serializer=protos_dot_ydb__table__pb2.ReadTableRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ReadTableResponse.FromString,
                )
        self.ReadRows = channel.unary_unary(
                '/Ydb.Table.V1.TableService/ReadRows',
                request_serializer=protos_dot_ydb__table__pb2.ReadRowsRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ReadRowsResponse.FromString,
                )
        self.BulkUpsert = channel.unary_unary(
                '/Ydb.Table.V1.TableService/BulkUpsert',
                request_serializer=protos_dot_ydb__table__pb2.BulkUpsertRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.BulkUpsertResponse.FromString,
                )
        self.StreamExecuteScanQuery = channel.unary_stream(
                '/Ydb.Table.V1.TableService/StreamExecuteScanQuery',
                request_serializer=protos_dot_ydb__table__pb2.ExecuteScanQueryRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__table__pb2.ExecuteScanQueryPartialResponse.FromString,
                )


class TableServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSession(self, request, context):
        """Create new session. Implicit session creation is forbidden,
        so user must create new session before execute any query,
        otherwise BAD_SESSION status will be returned.
        Simultaneous execution of requests are forbiden.
        Sessions are volatile, can be invalidated by server, for example in case
        of fatal errors. All requests with this session will fail with BAD_SESSION status.
        So, client must be able to handle BAD_SESSION status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSession(self, request, context):
        """Ends a session, releasing server resources associated with it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeepAlive(self, request, context):
        """Idle sessions can be kept alive by calling KeepAlive periodically.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTable(self, request, context):
        """Creates new table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropTable(self, request, context):
        """Drop table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AlterTable(self, request, context):
        """Modifies schema of given table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyTable(self, request, context):
        """Creates copy of given table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyTables(self, request, context):
        """Creates consistent copy of given tables.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenameTables(self, request, context):
        """Creates consistent move of given tables.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTable(self, request, context):
        """Returns information about given table (metadata).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExplainDataQuery(self, request, context):
        """Explains data query.
        SessionId of previously created session must be provided.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareDataQuery(self, request, context):
        """Prepares data query, returns query id.
        SessionId of previously created session must be provided.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteDataQuery(self, request, context):
        """Executes data query.
        SessionId of previously created session must be provided.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteSchemeQuery(self, request, context):
        """Executes scheme query.
        SessionId of previously created session must be provided.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BeginTransaction(self, request, context):
        """Begins new transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitTransaction(self, request, context):
        """Commits specified active transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RollbackTransaction(self, request, context):
        """Performs a rollback of the specified active transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTableOptions(self, request, context):
        """Describe supported table options.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamReadTable(self, request, context):
        """Streaming read table
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadRows(self, request, context):
        """Reads specified keys non-transactionally from a single table
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkUpsert(self, request, context):
        """Upserts a batch of rows non-transactionally.
        Returns success only when all rows were successfully upserted. In case of an error some rows might
        be upserted and some might not.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamExecuteScanQuery(self, request, context):
        """Executes scan query with streaming result.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TableServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=protos_dot_ydb__table__pb2.CreateSessionRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.CreateSessionResponse.SerializeToString,
            ),
            'DeleteSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSession,
                    request_deserializer=protos_dot_ydb__table__pb2.DeleteSessionRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.DeleteSessionResponse.SerializeToString,
            ),
            'KeepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.KeepAlive,
                    request_deserializer=protos_dot_ydb__table__pb2.KeepAliveRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.KeepAliveResponse.SerializeToString,
            ),
            'CreateTable': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTable,
                    request_deserializer=protos_dot_ydb__table__pb2.CreateTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.CreateTableResponse.SerializeToString,
            ),
            'DropTable': grpc.unary_unary_rpc_method_handler(
                    servicer.DropTable,
                    request_deserializer=protos_dot_ydb__table__pb2.DropTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.DropTableResponse.SerializeToString,
            ),
            'AlterTable': grpc.unary_unary_rpc_method_handler(
                    servicer.AlterTable,
                    request_deserializer=protos_dot_ydb__table__pb2.AlterTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.AlterTableResponse.SerializeToString,
            ),
            'CopyTable': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyTable,
                    request_deserializer=protos_dot_ydb__table__pb2.CopyTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.CopyTableResponse.SerializeToString,
            ),
            'CopyTables': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyTables,
                    request_deserializer=protos_dot_ydb__table__pb2.CopyTablesRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.CopyTablesResponse.SerializeToString,
            ),
            'RenameTables': grpc.unary_unary_rpc_method_handler(
                    servicer.RenameTables,
                    request_deserializer=protos_dot_ydb__table__pb2.RenameTablesRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.RenameTablesResponse.SerializeToString,
            ),
            'DescribeTable': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTable,
                    request_deserializer=protos_dot_ydb__table__pb2.DescribeTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.DescribeTableResponse.SerializeToString,
            ),
            'ExplainDataQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ExplainDataQuery,
                    request_deserializer=protos_dot_ydb__table__pb2.ExplainDataQueryRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ExplainDataQueryResponse.SerializeToString,
            ),
            'PrepareDataQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareDataQuery,
                    request_deserializer=protos_dot_ydb__table__pb2.PrepareDataQueryRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.PrepareDataQueryResponse.SerializeToString,
            ),
            'ExecuteDataQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteDataQuery,
                    request_deserializer=protos_dot_ydb__table__pb2.ExecuteDataQueryRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ExecuteDataQueryResponse.SerializeToString,
            ),
            'ExecuteSchemeQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteSchemeQuery,
                    request_deserializer=protos_dot_ydb__table__pb2.ExecuteSchemeQueryRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ExecuteSchemeQueryResponse.SerializeToString,
            ),
            'BeginTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.BeginTransaction,
                    request_deserializer=protos_dot_ydb__table__pb2.BeginTransactionRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.BeginTransactionResponse.SerializeToString,
            ),
            'CommitTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.CommitTransaction,
                    request_deserializer=protos_dot_ydb__table__pb2.CommitTransactionRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.CommitTransactionResponse.SerializeToString,
            ),
            'RollbackTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.RollbackTransaction,
                    request_deserializer=protos_dot_ydb__table__pb2.RollbackTransactionRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.RollbackTransactionResponse.SerializeToString,
            ),
            'DescribeTableOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTableOptions,
                    request_deserializer=protos_dot_ydb__table__pb2.DescribeTableOptionsRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.DescribeTableOptionsResponse.SerializeToString,
            ),
            'StreamReadTable': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamReadTable,
                    request_deserializer=protos_dot_ydb__table__pb2.ReadTableRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ReadTableResponse.SerializeToString,
            ),
            'ReadRows': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadRows,
                    request_deserializer=protos_dot_ydb__table__pb2.ReadRowsRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ReadRowsResponse.SerializeToString,
            ),
            'BulkUpsert': grpc.unary_unary_rpc_method_handler(
                    servicer.BulkUpsert,
                    request_deserializer=protos_dot_ydb__table__pb2.BulkUpsertRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.BulkUpsertResponse.SerializeToString,
            ),
            'StreamExecuteScanQuery': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamExecuteScanQuery,
                    request_deserializer=protos_dot_ydb__table__pb2.ExecuteScanQueryRequest.FromString,
                    response_serializer=protos_dot_ydb__table__pb2.ExecuteScanQueryPartialResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.Table.V1.TableService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TableService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/CreateSession',
            protos_dot_ydb__table__pb2.CreateSessionRequest.SerializeToString,
            protos_dot_ydb__table__pb2.CreateSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/DeleteSession',
            protos_dot_ydb__table__pb2.DeleteSessionRequest.SerializeToString,
            protos_dot_ydb__table__pb2.DeleteSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/KeepAlive',
            protos_dot_ydb__table__pb2.KeepAliveRequest.SerializeToString,
            protos_dot_ydb__table__pb2.KeepAliveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/CreateTable',
            protos_dot_ydb__table__pb2.CreateTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.CreateTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DropTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/DropTable',
            protos_dot_ydb__table__pb2.DropTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.DropTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AlterTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/AlterTable',
            protos_dot_ydb__table__pb2.AlterTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.AlterTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CopyTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/CopyTable',
            protos_dot_ydb__table__pb2.CopyTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.CopyTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CopyTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/CopyTables',
            protos_dot_ydb__table__pb2.CopyTablesRequest.SerializeToString,
            protos_dot_ydb__table__pb2.CopyTablesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenameTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/RenameTables',
            protos_dot_ydb__table__pb2.RenameTablesRequest.SerializeToString,
            protos_dot_ydb__table__pb2.RenameTablesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/DescribeTable',
            protos_dot_ydb__table__pb2.DescribeTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.DescribeTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExplainDataQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/ExplainDataQuery',
            protos_dot_ydb__table__pb2.ExplainDataQueryRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ExplainDataQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrepareDataQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/PrepareDataQuery',
            protos_dot_ydb__table__pb2.PrepareDataQueryRequest.SerializeToString,
            protos_dot_ydb__table__pb2.PrepareDataQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteDataQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/ExecuteDataQuery',
            protos_dot_ydb__table__pb2.ExecuteDataQueryRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ExecuteDataQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteSchemeQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/ExecuteSchemeQuery',
            protos_dot_ydb__table__pb2.ExecuteSchemeQueryRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ExecuteSchemeQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BeginTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/BeginTransaction',
            protos_dot_ydb__table__pb2.BeginTransactionRequest.SerializeToString,
            protos_dot_ydb__table__pb2.BeginTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/CommitTransaction',
            protos_dot_ydb__table__pb2.CommitTransactionRequest.SerializeToString,
            protos_dot_ydb__table__pb2.CommitTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RollbackTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/RollbackTransaction',
            protos_dot_ydb__table__pb2.RollbackTransactionRequest.SerializeToString,
            protos_dot_ydb__table__pb2.RollbackTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTableOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/DescribeTableOptions',
            protos_dot_ydb__table__pb2.DescribeTableOptionsRequest.SerializeToString,
            protos_dot_ydb__table__pb2.DescribeTableOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamReadTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Ydb.Table.V1.TableService/StreamReadTable',
            protos_dot_ydb__table__pb2.ReadTableRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ReadTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadRows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/ReadRows',
            protos_dot_ydb__table__pb2.ReadRowsRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ReadRowsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkUpsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Table.V1.TableService/BulkUpsert',
            protos_dot_ydb__table__pb2.BulkUpsertRequest.SerializeToString,
            protos_dot_ydb__table__pb2.BulkUpsertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamExecuteScanQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Ydb.Table.V1.TableService/StreamExecuteScanQuery',
            protos_dot_ydb__table__pb2.ExecuteScanQueryRequest.SerializeToString,
            protos_dot_ydb__table__pb2.ExecuteScanQueryPartialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
