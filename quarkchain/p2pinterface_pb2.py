# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2pinterface.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='p2pinterface.proto',
  package='p2pinterface',
  syntax='proto3',
  serialized_pb=_b('\n\x12p2pinterface.proto\x12\x0cp2pinterface\"\xa3\x01\n\x0cQuarkMessage\x12\x14\n\x0cis_broadcast\x18\x01 \x01(\x08\x12\x0f\n\x07peer_id\x18\x02 \x01(\t\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.p2pinterface.QuarkMessage.Type\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\",\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08P2PHELLO\x10\x01\x12\t\n\x05OTHER\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_QUARKMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p2pinterface.QuarkMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2PHELLO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=156,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_QUARKMESSAGE_TYPE)


_QUARKMESSAGE = _descriptor.Descriptor(
  name='QuarkMessage',
  full_name='p2pinterface.QuarkMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_broadcast', full_name='p2pinterface.QuarkMessage.is_broadcast', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='p2pinterface.QuarkMessage.peer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='p2pinterface.QuarkMessage.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='p2pinterface.QuarkMessage.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUARKMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=200,
)

_QUARKMESSAGE.fields_by_name['type'].enum_type = _QUARKMESSAGE_TYPE
_QUARKMESSAGE_TYPE.containing_type = _QUARKMESSAGE
DESCRIPTOR.message_types_by_name['QuarkMessage'] = _QUARKMESSAGE

QuarkMessage = _reflection.GeneratedProtocolMessageType('QuarkMessage', (_message.Message,), dict(
  DESCRIPTOR = _QUARKMESSAGE,
  __module__ = 'p2pinterface_pb2'
  # @@protoc_insertion_point(class_scope:p2pinterface.QuarkMessage)
  ))
_sym_db.RegisterMessage(QuarkMessage)


# @@protoc_insertion_point(module_scope)