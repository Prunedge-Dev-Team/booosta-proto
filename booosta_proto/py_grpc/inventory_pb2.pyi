from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProductInventoryByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProductInventoryByIdResponse(_message.Message):
    __slots__ = ["product_inventory"]
    PRODUCT_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    product_inventory: ProductInventory
    def __init__(self, product_inventory: _Optional[_Union[ProductInventory, _Mapping]] = ...) -> None: ...

class GetUnitTypeByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUnitTypeByIdResponse(_message.Message):
    __slots__ = ["unit_type"]
    UNIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    unit_type: UnitType
    def __init__(self, unit_type: _Optional[_Union[UnitType, _Mapping]] = ...) -> None: ...

class ProductInventory(_message.Message):
    __slots__ = ["cost_price", "created_by_id", "current_quantity", "minimum_stock_quantity", "name"]
    COST_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_STOCK_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cost_price: float
    created_by_id: str
    current_quantity: int
    minimum_stock_quantity: int
    name: str
    def __init__(self, name: _Optional[str] = ..., cost_price: _Optional[float] = ..., current_quantity: _Optional[int] = ..., minimum_stock_quantity: _Optional[int] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class UnitType(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
