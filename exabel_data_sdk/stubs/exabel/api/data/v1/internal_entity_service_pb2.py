# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exabel/api/data/v1/internal_entity_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from exabel_data_sdk.stubs.exabel.api.data.v1 import entity_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2
from exabel_data_sdk.stubs.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exabel/api/data/v1/internal_entity_service.proto',
  package='exabel.api.data.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.exabel.api.data.v1B\032InternalEntityServiceProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0exabel/api/data/v1/internal_entity_service.proto\x12\x12\x65xabel.api.data.v1\x1a(exabel/api/data/v1/entity_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"N\n\x17\x43reateEntityTypeRequest\x12\x33\n\x0b\x65ntity_type\x18\x01 \x01(\x0b\x32\x1e.exabel.api.data.v1.EntityType\"\x7f\n\x17UpdateEntityTypeRequest\x12\x33\n\x0b\x65ntity_type\x18\x01 \x01(\x0b\x32\x1e.exabel.api.data.v1.EntityType\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask2\xbc\x02\n\x15InternalEntityService\x12\x85\x01\n\x10\x43reateEntityType\x12+.exabel.api.data.v1.CreateEntityTypeRequest\x1a\x1e.exabel.api.data.v1.EntityType\"$\x82\xd3\xe4\x93\x02\x1e\"\x0f/v1/entityTypes:\x0b\x65ntity_type\x12\x9a\x01\n\x10UpdateEntityType\x12+.exabel.api.data.v1.UpdateEntityTypeRequest\x1a\x1e.exabel.api.data.v1.EntityType\"9\x82\xd3\xe4\x93\x02\x33\x32$/v1/{entity_type.name=entityTypes/*}:\x0b\x65ntity_typeB6\n\x16\x63om.exabel.api.data.v1B\x1aInternalEntityServiceProtoP\x01\x62\x06proto3'
  ,
  dependencies=[exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_CREATEENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='CreateEntityTypeRequest',
  full_name='exabel.api.data.v1.CreateEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='exabel.api.data.v1.CreateEntityTypeRequest.entity_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=178,
  serialized_end=256,
)


_UPDATEENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateEntityTypeRequest',
  full_name='exabel.api.data.v1.UpdateEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='exabel.api.data.v1.UpdateEntityTypeRequest.entity_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='exabel.api.data.v1.UpdateEntityTypeRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=258,
  serialized_end=385,
)

_CREATEENTITYTYPEREQUEST.fields_by_name['entity_type'].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE
_UPDATEENTITYTYPEREQUEST.fields_by_name['entity_type'].message_type = exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE
_UPDATEENTITYTYPEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['CreateEntityTypeRequest'] = _CREATEENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEntityTypeRequest'] = _UPDATEENTITYTYPEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('CreateEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENTITYTYPEREQUEST,
  '__module__' : 'exabel.api.data.v1.internal_entity_service_pb2'
  # @@protoc_insertion_point(class_scope:exabel.api.data.v1.CreateEntityTypeRequest)
  })
_sym_db.RegisterMessage(CreateEntityTypeRequest)

UpdateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateEntityTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENTITYTYPEREQUEST,
  '__module__' : 'exabel.api.data.v1.internal_entity_service_pb2'
  # @@protoc_insertion_point(class_scope:exabel.api.data.v1.UpdateEntityTypeRequest)
  })
_sym_db.RegisterMessage(UpdateEntityTypeRequest)


DESCRIPTOR._options = None

_INTERNALENTITYSERVICE = _descriptor.ServiceDescriptor(
  name='InternalEntityService',
  full_name='exabel.api.data.v1.InternalEntityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=388,
  serialized_end=704,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateEntityType',
    full_name='exabel.api.data.v1.InternalEntityService.CreateEntityType',
    index=0,
    containing_service=None,
    input_type=_CREATEENTITYTYPEREQUEST,
    output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE,
    serialized_options=b'\202\323\344\223\002\036\"\017/v1/entityTypes:\013entity_type',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateEntityType',
    full_name='exabel.api.data.v1.InternalEntityService.UpdateEntityType',
    index=1,
    containing_service=None,
    input_type=_UPDATEENTITYTYPEREQUEST,
    output_type=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2._ENTITYTYPE,
    serialized_options=b'\202\323\344\223\00232$/v1/{entity_type.name=entityTypes/*}:\013entity_type',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERNALENTITYSERVICE)

DESCRIPTOR.services_by_name['InternalEntityService'] = _INTERNALENTITYSERVICE

# @@protoc_insertion_point(module_scope)
