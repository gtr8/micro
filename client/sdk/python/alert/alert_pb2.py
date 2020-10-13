# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert/alert.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert/alert.proto',
  package='alert',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x61lert/alert.proto\x12\x05\x61lert\"\xb2\x01\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\x04\x12,\n\x08metadata\x18\x06 \x03(\x0b\x32\x1a.alert.Event.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x12ReportEventRequest\x12\x1b\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x0c.alert.Event\"\x15\n\x13ReportEventResponse2O\n\x05\x41lert\x12\x46\n\x0bReportEvent\x12\x19.alert.ReportEventRequest\x1a\x1a.alert.ReportEventResponse\"\x00\x62\x06proto3'
)




_EVENT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='alert.Event.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='alert.Event.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='alert.Event.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=207,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='alert.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alert.Event.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='alert.Event.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='alert.Event.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='alert.Event.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='alert.Event.value', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='alert.Event.metadata', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=207,
)


_REPORTEVENTREQUEST = _descriptor.Descriptor(
  name='ReportEventRequest',
  full_name='alert.ReportEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='alert.ReportEventRequest.event', index=0,
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
  serialized_start=209,
  serialized_end=258,
)


_REPORTEVENTRESPONSE = _descriptor.Descriptor(
  name='ReportEventResponse',
  full_name='alert.ReportEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=260,
  serialized_end=281,
)

_EVENT_METADATAENTRY.containing_type = _EVENT
_EVENT.fields_by_name['metadata'].message_type = _EVENT_METADATAENTRY
_REPORTEVENTREQUEST.fields_by_name['event'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['ReportEventRequest'] = _REPORTEVENTREQUEST
DESCRIPTOR.message_types_by_name['ReportEventResponse'] = _REPORTEVENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_METADATAENTRY,
    '__module__' : 'alert.alert_pb2'
    # @@protoc_insertion_point(class_scope:alert.Event.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'alert.alert_pb2'
  # @@protoc_insertion_point(class_scope:alert.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.MetadataEntry)

ReportEventRequest = _reflection.GeneratedProtocolMessageType('ReportEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEVENTREQUEST,
  '__module__' : 'alert.alert_pb2'
  # @@protoc_insertion_point(class_scope:alert.ReportEventRequest)
  })
_sym_db.RegisterMessage(ReportEventRequest)

ReportEventResponse = _reflection.GeneratedProtocolMessageType('ReportEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEVENTRESPONSE,
  '__module__' : 'alert.alert_pb2'
  # @@protoc_insertion_point(class_scope:alert.ReportEventResponse)
  })
_sym_db.RegisterMessage(ReportEventResponse)


_EVENT_METADATAENTRY._options = None

_ALERT = _descriptor.ServiceDescriptor(
  name='Alert',
  full_name='alert.Alert',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=283,
  serialized_end=362,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportEvent',
    full_name='alert.Alert.ReportEvent',
    index=0,
    containing_service=None,
    input_type=_REPORTEVENTREQUEST,
    output_type=_REPORTEVENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALERT)

DESCRIPTOR.services_by_name['Alert'] = _ALERT

# @@protoc_insertion_point(module_scope)