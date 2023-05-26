from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ["customer_email", "customer_name", "customer_phone", "description"]
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PHONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    customer_email: str
    customer_name: str
    customer_phone: str
    description: str
    def __init__(self, customer_name: _Optional[str] = ..., customer_phone: _Optional[str] = ..., customer_email: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CustomerListResponse(_message.Message):
    __slots__ = ["customer"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _containers.RepeatedCompositeFieldContainer[Customer]
    def __init__(self, customer: _Optional[_Iterable[_Union[Customer, _Mapping]]] = ...) -> None: ...

class GetCustomerByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCustomerByIdResponse(_message.Message):
    __slots__ = ["customer"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: Customer
    def __init__(self, customer: _Optional[_Union[Customer, _Mapping]] = ...) -> None: ...

class GetCustomersByCreatedByRequest(_message.Message):
    __slots__ = ["created_by_id"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    def __init__(self, created_by_id: _Optional[str] = ...) -> None: ...

class GetCustomersByCreatedByResponse(_message.Message):
    __slots__ = ["customers"]
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    customers: _containers.RepeatedCompositeFieldContainer[Customer]
    def __init__(self, customers: _Optional[_Iterable[_Union[Customer, _Mapping]]] = ...) -> None: ...

class GetOrderByCreatedByIdAndPaymentTypeRequest(_message.Message):
    __slots__ = ["created_by_id", "payment_type"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    payment_type: str
    def __init__(self, created_by_id: _Optional[str] = ..., payment_type: _Optional[str] = ...) -> None: ...

class GetOrderByCreatedByIdAndPaymentTypeResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, order: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...

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

class GetOrderItemQuantityByProductIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetOrderItemQuantityByProductIdResponse(_message.Message):
    __slots__ = ["quantity"]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    def __init__(self, quantity: _Optional[int] = ...) -> None: ...

class GetOrderItemsByCreatedByIdRequest(_message.Message):
    __slots__ = ["created_by_id"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    def __init__(self, created_by_id: _Optional[str] = ...) -> None: ...

class GetOrderItemsByOrderIdRequest(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class GetOrderItemsByProductIdAndCreatedByIdRequest(_message.Message):
    __slots__ = ["created_by_id", "product_id"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    product_id: str
    def __init__(self, created_by_id: _Optional[str] = ..., product_id: _Optional[str] = ...) -> None: ...

class GetOrderItemsByProductIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["amount_payment", "balance", "balance_due_date", "created_by_id", "customer_id", "discount", "grand_total", "payment_date", "payment_option", "payment_type", "sales_date", "shipping_fee", "total_price", "transaction_id"]
    AMOUNT_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
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
    created_by_id: str
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
    def __init__(self, customer_id: _Optional[str] = ..., payment_type: _Optional[str] = ..., payment_option: _Optional[str] = ..., amount_payment: _Optional[float] = ..., shipping_fee: _Optional[float] = ..., balance: _Optional[float] = ..., total_price: _Optional[float] = ..., payment_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., balance_due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., discount: _Optional[float] = ..., grand_total: _Optional[float] = ..., sales_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transaction_id: _Optional[str] = ..., created_by_id: _Optional[str] = ...) -> None: ...

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

class OrderItemsListResponse(_message.Message):
    __slots__ = ["order_item"]
    ORDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    order_item: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, order_item: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...
