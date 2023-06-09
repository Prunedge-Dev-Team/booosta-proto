# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: personnel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpersonnel.proto\x12\tpersonnel\"\xfd\x01\n\x08Retailer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x15\n\rbusiness_name\x18\x03 \x01(\t\x12\x15\n\rbusiness_type\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x16\n\x0e\x63lassification\x18\x06 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x07 \x01(\t\x12\x11\n\tbank_code\x18\x08 \x01(\t\x12\x0b\n\x03\x62vn\x18\t \x01(\t\x12\x14\n\x0cis_validated\x18\n \x01(\x08\x12\x16\n\x0eis_blacklisted\x18\x0b \x01(\x08\x12\x16\n\x0ewallet_balance\x18\x0c \x01(\x01\"(\n\x1aGetRetailerByUserIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"D\n\x1bGetRetailerByUserIdResponse\x12%\n\x08retailer\x18\x01 \x01(\x0b\x32\x13.personnel.Retailer\"B\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x1c\n\x14\x62usiness_information\x18\x03 \x01(\t\"%\n\x17GetAgentByUserIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x18GetAgentByUserIdResponse\x12\x1f\n\x05\x61gent\x18\x01 \x01(\x0b\x32\x10.personnel.Agent\"\xc3\x01\n\nAggregator\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x1c\n\x14\x62usiness_information\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_type\x18\x04 \x01(\t\x12\x14\n\x0c\x63ompany_size\x18\x05 \x01(\t\x12\x1f\n\x17\x65stimated_customer_base\x18\x06 \x01(\t\x12\x17\n\x0f\x61ggregator_code\x18\x07 \x01(\t\x12\x14\n\x0c\x63ontact_name\x18\x08 \x01(\t\"*\n\x1cGetAggregatorByUserIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"J\n\x1dGetAggregatorByUserIdResponse\x12)\n\naggregator\x18\x01 \x01(\x0b\x32\x15.personnel.Aggregator\"\x9a\x01\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x11\n\tdevice_id\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x18\n\x10\x64\x65livery_address\x18\x07 \x01(\t\x12\x18\n\x10\x63losest_landmark\x18\x08 \x01(\t\"N\n&GetRetailerTerminalByTerminalIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0bterminal_id\x18\x02 \x01(\t\";\n\'GetRetailerTerminalByTerminalIdResponse\x12\x10\n\x08terminal\x18\x01 \x01(\t\"F\n\x1dUpdateRetailerByUserIdRequest\x12%\n\x08retailer\x18\x01 \x01(\x0b\x32\x13.personnel.Retailer\"G\n\x1eUpdateRetailerByUserIdResponse\x12%\n\x08retailer\x18\x01 \x01(\x0b\x32\x13.personnel.Retailer2\xc5\x04\n\x10PersonnelService\x12\x66\n\x13GetRetailerByUserId\x12%.personnel.GetRetailerByUserIdRequest\x1a&.personnel.GetRetailerByUserIdResponse\"\x00\x12]\n\x10GetAgentByUserId\x12\".personnel.GetAgentByUserIdRequest\x1a#.personnel.GetAgentByUserIdResponse\"\x00\x12l\n\x15GetAggregatorByUserId\x12\'.personnel.GetAggregatorByUserIdRequest\x1a(.personnel.GetAggregatorByUserIdResponse\"\x00\x12\x8a\x01\n\x1fGetRetailerTerminalByTerminalId\x12\x31.personnel.GetRetailerTerminalByTerminalIdRequest\x1a\x32.personnel.GetRetailerTerminalByTerminalIdResponse\"\x00\x12o\n\x16UpdateRetailerByUserId\x12(.personnel.UpdateRetailerByUserIdRequest\x1a).personnel.UpdateRetailerByUserIdResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'personnel_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RETAILER._serialized_start=31
  _RETAILER._serialized_end=284
  _GETRETAILERBYUSERIDREQUEST._serialized_start=286
  _GETRETAILERBYUSERIDREQUEST._serialized_end=326
  _GETRETAILERBYUSERIDRESPONSE._serialized_start=328
  _GETRETAILERBYUSERIDRESPONSE._serialized_end=396
  _AGENT._serialized_start=398
  _AGENT._serialized_end=464
  _GETAGENTBYUSERIDREQUEST._serialized_start=466
  _GETAGENTBYUSERIDREQUEST._serialized_end=503
  _GETAGENTBYUSERIDRESPONSE._serialized_start=505
  _GETAGENTBYUSERIDRESPONSE._serialized_end=564
  _AGGREGATOR._serialized_start=567
  _AGGREGATOR._serialized_end=762
  _GETAGGREGATORBYUSERIDREQUEST._serialized_start=764
  _GETAGGREGATORBYUSERIDREQUEST._serialized_end=806
  _GETAGGREGATORBYUSERIDRESPONSE._serialized_start=808
  _GETAGGREGATORBYUSERIDRESPONSE._serialized_end=882
  _DEVICE._serialized_start=885
  _DEVICE._serialized_end=1039
  _GETRETAILERTERMINALBYTERMINALIDREQUEST._serialized_start=1041
  _GETRETAILERTERMINALBYTERMINALIDREQUEST._serialized_end=1119
  _GETRETAILERTERMINALBYTERMINALIDRESPONSE._serialized_start=1121
  _GETRETAILERTERMINALBYTERMINALIDRESPONSE._serialized_end=1180
  _UPDATERETAILERBYUSERIDREQUEST._serialized_start=1182
  _UPDATERETAILERBYUSERIDREQUEST._serialized_end=1252
  _UPDATERETAILERBYUSERIDRESPONSE._serialized_start=1254
  _UPDATERETAILERBYUSERIDRESPONSE._serialized_end=1325
  _PERSONNELSERVICE._serialized_start=1328
  _PERSONNELSERVICE._serialized_end=1909
# @@protoc_insertion_point(module_scope)
