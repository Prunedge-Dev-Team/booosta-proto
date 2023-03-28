# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\x12\tinventory\"\x85\x01\n\x10ProductInventory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncost_price\x18\x02 \x01(\x02\x12\x18\n\x10\x63urrent_quantity\x18\x03 \x01(\x03\x12\x1e\n\x16minimum_stock_quantity\x18\x04 \x01(\x03\x12\x15\n\rcreated_by_id\x18\x05 \x01(\t\"\x18\n\x08UnitType\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\x1eGetProductInventoryByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"$\n\x16GetUnitTypeByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n\x1fGetProductInventoryByIdResponse\x12\x36\n\x11product_inventory\x18\x01 \x01(\x0b\x32\x1b.inventory.ProductInventory\"A\n\x17GetUnitTypeByIdResponse\x12&\n\tunit_type\x18\x01 \x01(\x0b\x32\x13.inventory.UnitType2\xe2\x01\n\x10InventoryService\x12r\n\x17GetProductInventoryById\x12).inventory.GetProductInventoryByIdRequest\x1a*.inventory.GetProductInventoryByIdResponse\"\x00\x12Z\n\x0fGetUnitTypeById\x12!.inventory.GetUnitTypeByIdRequest\x1a\".inventory.GetUnitTypeByIdResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCTINVENTORY._serialized_start=31
  _PRODUCTINVENTORY._serialized_end=164
  _UNITTYPE._serialized_start=166
  _UNITTYPE._serialized_end=190
  _GETPRODUCTINVENTORYBYIDREQUEST._serialized_start=192
  _GETPRODUCTINVENTORYBYIDREQUEST._serialized_end=236
  _GETUNITTYPEBYIDREQUEST._serialized_start=238
  _GETUNITTYPEBYIDREQUEST._serialized_end=274
  _GETPRODUCTINVENTORYBYIDRESPONSE._serialized_start=276
  _GETPRODUCTINVENTORYBYIDRESPONSE._serialized_end=365
  _GETUNITTYPEBYIDRESPONSE._serialized_start=367
  _GETUNITTYPEBYIDRESPONSE._serialized_end=432
  _INVENTORYSERVICE._serialized_start=435
  _INVENTORYSERVICE._serialized_end=661
# @@protoc_insertion_point(module_scope)