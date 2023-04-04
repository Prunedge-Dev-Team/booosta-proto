from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class GetProductInventoryByUserIDAndQuantityRequest(_message.Message):
    __slots__ = ["created_by_id", "low_quantity"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    LOW_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    low_quantity: bool
    def __init__(self, created_by_id: _Optional[str] = ..., low_quantity: bool = ...) -> None: ...

class GetProductInventoryByUserIdRequest(_message.Message):
    __slots__ = ["created_by_id"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    def __init__(self, created_by_id: _Optional[str] = ...) -> None: ...

class GetRetailerProductListRequest(_message.Message):
    __slots__ = ["created_by_id", "ordering", "status"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    ordering: str
    status: str
    def __init__(self, created_by_id: _Optional[str] = ..., status: _Optional[str] = ..., ordering: _Optional[str] = ...) -> None: ...

class GetRetailerProductListResponse(_message.Message):
    __slots__ = ["product_inventory"]
    PRODUCT_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    product_inventory: _containers.RepeatedCompositeFieldContainer[ProductAdminList]
    def __init__(self, product_inventory: _Optional[_Iterable[_Union[ProductAdminList, _Mapping]]] = ...) -> None: ...

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

class ProductAdminList(_message.Message):
    __slots__ = ["business_name", "cost_price", "selling_price", "sold", "status", "stock_quantity", "stock_value"]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    COST_PRICE_FIELD_NUMBER: _ClassVar[int]
    SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    SOLD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STOCK_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    STOCK_VALUE_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    cost_price: int
    selling_price: float
    sold: str
    status: str
    stock_quantity: int
    stock_value: int
    def __init__(self, stock_quantity: _Optional[int] = ..., stock_value: _Optional[int] = ..., sold: _Optional[str] = ..., status: _Optional[str] = ..., selling_price: _Optional[float] = ..., business_name: _Optional[str] = ..., cost_price: _Optional[int] = ...) -> None: ...

class ProductInventory(_message.Message):
    __slots__ = ["category", "cost_price", "created_by_id", "current_quantity", "default_quantity", "description", "image", "low_quantity", "minimum_stock_quantity", "name", "selling_price", "unit_type"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    COST_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOW_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_STOCK_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    UNIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    category: str
    cost_price: float
    created_by_id: str
    current_quantity: int
    default_quantity: int
    description: str
    image: str
    low_quantity: bool
    minimum_stock_quantity: int
    name: str
    selling_price: float
    unit_type: str
    def __init__(self, name: _Optional[str] = ..., cost_price: _Optional[float] = ..., current_quantity: _Optional[int] = ..., minimum_stock_quantity: _Optional[int] = ..., created_by_id: _Optional[str] = ..., image: _Optional[str] = ..., default_quantity: _Optional[int] = ..., unit_type: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., low_quantity: bool = ..., selling_price: _Optional[float] = ...) -> None: ...

class ProductInventoryListResponse(_message.Message):
    __slots__ = ["product_inventory"]
    PRODUCT_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    product_inventory: _containers.RepeatedCompositeFieldContainer[ProductInventory]
    def __init__(self, product_inventory: _Optional[_Iterable[_Union[ProductInventory, _Mapping]]] = ...) -> None: ...

class UnitType(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
