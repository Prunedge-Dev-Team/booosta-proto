from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOrderByIdRequest(_message.Message):
    __slots__ = ["id", "payment_type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    payment_type: str
    def __init__(self, id: _Optional[str] = ..., payment_type: _Optional[str] = ...) -> None: ...

class GetOrderByIdResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class GetOrderItemByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetOrderItemByIdResponse(_message.Message):
    __slots__ = ["order_item"]
    ORDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    order_item: OrderItem
    def __init__(self, order_item: _Optional[_Union[OrderItem, _Mapping]] = ...) -> None: ...

class GetOrderItemsByProductIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetOrderItemsByProductIdResponse(_message.Message):
    __slots__ = ["order_item"]
    ORDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    order_item: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, order_item: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["amount_payment", "balance", "balance_due_date", "customer_id", "discount", "grand_total", "payment_date", "payment_option", "payment_type", "sales_date", "shipping_fee", "total_price", "transaction_id"]
    AMOUNT_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_OPTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SALES_DATE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FEE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    amount_payment: float
    balance: float
    balance_due_date: _timestamp_pb2.Timestamp
    customer_id: str
    discount: float
    grand_total: float
    payment_date: _timestamp_pb2.Timestamp
    payment_option: str
    payment_type: str
    sales_date: _timestamp_pb2.Timestamp
    shipping_fee: float
    total_price: float
    transaction_id: str
    def __init__(self, customer_id: _Optional[str] = ..., payment_type: _Optional[str] = ..., payment_option: _Optional[str] = ..., amount_payment: _Optional[float] = ..., shipping_fee: _Optional[float] = ..., balance: _Optional[float] = ..., total_price: _Optional[float] = ..., payment_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., balance_due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., discount: _Optional[float] = ..., grand_total: _Optional[float] = ..., sales_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class OrderItem(_message.Message):
    __slots__ = ["created_by_id", "discount_selling_price", "order_id", "product_cost_price", "product_id", "quantity", "selling_price", "total_price"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    discount_selling_price: float
    order_id: str
    product_cost_price: float
    product_id: str
    quantity: int
    selling_price: float
    total_price: float
    def __init__(self, product_id: _Optional[str] = ..., order_id: _Optional[str] = ..., quantity: _Optional[int] = ..., discount_selling_price: _Optional[float] = ..., product_cost_price: _Optional[float] = ..., selling_price: _Optional[float] = ..., total_price: _Optional[float] = ..., created_by_id: _Optional[str] = ...) -> None: ...