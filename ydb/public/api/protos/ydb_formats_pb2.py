# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb/public/api/protos/ydb_formats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb/public/api/protos/ydb_formats.proto',
  package='Ydb.Formats',
  syntax='proto3',
  serialized_options=b'\n\026com.yandex.ydb.formats\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'ydb/public/api/protos/ydb_formats.proto\x12\x0bYdb.Formats\"$\n\x12\x41rrowBatchSettings\x12\x0e\n\x06schema\x18\x01 \x01(\x0c\"W\n\x0b\x43svSettings\x12\x11\n\tskip_rows\x18\x01 \x01(\r\x12\x11\n\tdelimiter\x18\x02 \x01(\x0c\x12\x12\n\nnull_value\x18\x03 \x01(\x0c\x12\x0e\n\x06header\x18\x04 \x01(\x08\x42\x1b\n\x16\x63om.yandex.ydb.formats\xf8\x01\x01\x62\x06proto3'
)




_ARROWBATCHSETTINGS = _descriptor.Descriptor(
  name='ArrowBatchSettings',
  full_name='Ydb.Formats.ArrowBatchSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='Ydb.Formats.ArrowBatchSettings.schema', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=92,
)


_CSVSETTINGS = _descriptor.Descriptor(
  name='CsvSettings',
  full_name='Ydb.Formats.CsvSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='skip_rows', full_name='Ydb.Formats.CsvSettings.skip_rows', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delimiter', full_name='Ydb.Formats.CsvSettings.delimiter', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='null_value', full_name='Ydb.Formats.CsvSettings.null_value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='Ydb.Formats.CsvSettings.header', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['ArrowBatchSettings'] = _ARROWBATCHSETTINGS
DESCRIPTOR.message_types_by_name['CsvSettings'] = _CSVSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrowBatchSettings = _reflection.GeneratedProtocolMessageType('ArrowBatchSettings', (_message.Message,), {
  'DESCRIPTOR' : _ARROWBATCHSETTINGS,
  '__module__' : 'ydb.public.api.protos.ydb_formats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Formats.ArrowBatchSettings)
  })
_sym_db.RegisterMessage(ArrowBatchSettings)

CsvSettings = _reflection.GeneratedProtocolMessageType('CsvSettings', (_message.Message,), {
  'DESCRIPTOR' : _CSVSETTINGS,
  '__module__' : 'ydb.public.api.protos.ydb_formats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Formats.CsvSettings)
  })
_sym_db.RegisterMessage(CsvSettings)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)