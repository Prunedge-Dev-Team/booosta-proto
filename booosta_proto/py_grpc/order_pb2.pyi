from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ["id", "customer_id", "payment_type", "payment_option", "amount_payment", "shipping_fee", "balance", "total_price", "discount", "grand_total", "transaction_id", "created_by_id", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_OPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FEE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    customer_id: str
    payment_type: str
    payment_option: str
    amount_payment: float
    shipping_fee: float
    balance: float
    total_price: float
    discount: float
    grand_total: float
    transaction_id: str
    created_by_id: str
    status: str
    def __init__(self, id: _Optional[str] = ..., customer_id: _Optional[str] = ..., payment_type: _Optional[str] = ..., payment_option: _Optional[str] = ..., amount_payment: _Optional[float] = ..., shipping_fee: _Optional[float] = ..., balance: _Optional[float] = ..., total_price: _Optional[float] = ..., discount: _Optional[float] = ..., grand_total: _Optional[float] = ..., transaction_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class OrderItem(_message.Message):
    __slots__ = ["product_id", "order_id", "quantity", "discount_selling_price", "product_cost_price", "selling_price", "total_price", "created_by_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COST_PRICE_FIELD_NUMBER: _ClassVar[int]
    SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    order_id: str
    quantity: int
    discount_selling_price: float
    product_cost_price: float
    selling_price: float
    total_price: float
    created_by_id: str
    def __init__(self, product_id: _Optional[str] = ..., order_id: _Optional[str] = ..., quantity: _Optional[int] = ..., discount_selling_price: _Optional[float] = ..., product_cost_price: _Optional[float] = ..., selling_price: _Optional[float] = ..., total_price: _Optional[float] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class Cart(_message.Message):
    __slots__ = ["id", "product_id", "quantity", "selling_price", "discount_selling_price", "total_price", "created_by_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_SELLING_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_id: str
    quantity: int
    selling_price: float
    discount_selling_price: float
    total_price: float
    created_by_id: str
    def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., quantity: _Optional[int] = ..., selling_price: _Optional[float] = ..., discount_selling_price: _Optional[float] = ..., total_price: _Optional[float] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class GetOrderByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetOrderByCreatedByIdAndPaymentTypeRequest(_message.Message):
    __slots__ = ["created_by_id", "payment_type"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    payment_type: str
    def __init__(self, created_by_id: _Optional[str] = ..., payment_type: _Optional[str] = ...) -> None: ...

class GetOrderItemByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetOrderByIdResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class GetOrderByCreatedByIdAndPaymentTypeResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, order: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...

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

class GetOrderItemsByCreatedByIdRequest(_message.Message):
    __slots__ = ["created_by_id"]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    created_by_id: str
    def __init__(self, created_by_id: _Optional[str] = ...) -> None: ...

class OrderItemsListResponse(_message.Message):
    __slots__ = ["order_item"]
    ORDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    order_item: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, order_item: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...

class Customer(_message.Message):
    __slots__ = ["customer_name", "customer_phone", "customer_email", "description"]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PHONE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    customer_name: str
    customer_phone: str
    customer_email: str
    description: str
    def __init__(self, customer_name: _Optional[str] = ..., customer_phone: _Optional[str] = ..., customer_email: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

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

class CustomerListResponse(_message.Message):
    __slots__ = ["customer"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _containers.RepeatedCompositeFieldContainer[Customer]
    def __init__(self, customer: _Optional[_Iterable[_Union[Customer, _Mapping]]] = ...) -> None: ...

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

class UpdateOrderByIdRequest(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class UpdateOrderByIdResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class RemoveProductFromCartByProductIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class RemoveProductFromCartByProductIdResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class GetCustomerDebtByIdRequest(_message.Message):
    __slots__ = ["customer_id"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class GetCustomerDebtByIdResponse(_message.Message):
    __slots__ = ["debt"]
    DEBT_FIELD_NUMBER: _ClassVar[int]
    debt: float
    def __init__(self, debt: _Optional[float] = ...) -> None: ...

class UpdateCustomerDebtByIdRequest(_message.Message):
    __slots__ = ["customer_id", "amount_paid"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    amount_paid: float
    def __init__(self, customer_id: _Optional[str] = ..., amount_paid: _Optional[float] = ...) -> None: ...

class UpdateCustomerDebtByIdResponse(_message.Message):
    __slots__ = ["customer_id", "debt"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEBT_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    debt: float
    def __init__(self, customer_id: _Optional[str] = ..., debt: _Optional[float] = ...) -> None: ...

class GetCartByProductIdRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetCartByProductIdResponse(_message.Message):
    __slots__ = ["cart"]
    CART_FIELD_NUMBER: _ClassVar[int]
    cart: Cart
    def __init__(self, cart: _Optional[_Union[Cart, _Mapping]] = ...) -> None: ...
