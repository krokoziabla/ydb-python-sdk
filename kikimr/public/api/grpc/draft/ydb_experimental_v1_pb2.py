# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_experimental_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_experimental_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_experimental_v1.proto',
  package='Ydb.Experimental.V1',
  syntax='proto3',
  serialized_options=b'\n\036com.yandex.ydb.experimental.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6kikimr/public/api/grpc/draft/ydb_experimental_v1.proto\x12\x13Ydb.Experimental.V1\x1a/kikimr/public/api/protos/ydb_experimental.proto2\xcf\x02\n\x13\x45xperimentalService\x12W\n\nUploadRows\x12#.Ydb.Experimental.UploadRowsRequest\x1a$.Ydb.Experimental.UploadRowsResponse\x12q\n\x12\x45xecuteStreamQuery\x12+.Ydb.Experimental.ExecuteStreamQueryRequest\x1a,.Ydb.Experimental.ExecuteStreamQueryResponse0\x01\x12l\n\x11GetDiskSpaceUsage\x12*.Ydb.Experimental.GetDiskSpaceUsageRequest\x1a+.Ydb.Experimental.GetDiskSpaceUsageResponseB \n\x1e\x63om.yandex.ydb.experimental.v1b\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_EXPERIMENTALSERVICE = _descriptor.ServiceDescriptor(
  name='ExperimentalService',
  full_name='Ydb.Experimental.V1.ExperimentalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=129,
  serialized_end=464,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadRows',
    full_name='Ydb.Experimental.V1.ExperimentalService.UploadRows',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._UPLOADROWSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._UPLOADROWSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteStreamQuery',
    full_name='Ydb.Experimental.V1.ExperimentalService.ExecuteStreamQuery',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._EXECUTESTREAMQUERYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._EXECUTESTREAMQUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDiskSpaceUsage',
    full_name='Ydb.Experimental.V1.ExperimentalService.GetDiskSpaceUsage',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._GETDISKSPACEUSAGEREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._GETDISKSPACEUSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXPERIMENTALSERVICE)

DESCRIPTOR.services_by_name['ExperimentalService'] = _EXPERIMENTALSERVICE

# @@protoc_insertion_point(module_scope)
