from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Agent(_message.Message):
    __slots__ = ["business_information", "id", "user_id"]
    BUSINESS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    business_information: str
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_information: _Optional[str] = ...) -> None: ...

class Aggregator(_message.Message):
    __slots__ = ["aggregator_code", "business_information", "company_size", "company_type", "contact_name", "estimated_customer_base", "id", "user_id"]
    AGGREGATOR_CODE_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CUSTOMER_BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    aggregator_code: str
    business_information: str
    company_size: str
    company_type: str
    contact_name: str
    estimated_customer_base: str
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_information: _Optional[str] = ..., company_type: _Optional[str] = ..., company_size: _Optional[str] = ..., estimated_customer_base: _Optional[str] = ..., aggregator_code: _Optional[str] = ..., contact_name: _Optional[str] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["closest_landmark", "delivery_address", "device_id", "id", "price", "state", "status", "user_id"]
    CLOSEST_LANDMARK_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    closest_landmark: str
    delivery_address: str
    device_id: str
    id: str
    price: float
    state: str
    status: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., price: _Optional[float] = ..., state: _Optional[str] = ..., status: _Optional[str] = ..., delivery_address: _Optional[str] = ..., closest_landmark: _Optional[str] = ...) -> None: ...

class GetAgentByUserIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAgentByUserIdResponse(_message.Message):
    __slots__ = ["agent"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]] = ...) -> None: ...

class GetAggregatorByUserIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAggregatorByUserIdResponse(_message.Message):
    __slots__ = ["aggregator"]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    aggregator: Aggregator
    def __init__(self, aggregator: _Optional[_Union[Aggregator, _Mapping]] = ...) -> None: ...

class GetRetailerByUserIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRetailerByUserIdResponse(_message.Message):
    __slots__ = ["retailer"]
    RETAILER_FIELD_NUMBER: _ClassVar[int]
    retailer: Retailer
    def __init__(self, retailer: _Optional[_Union[Retailer, _Mapping]] = ...) -> None: ...

class GetRetailerTerminalByTerminalIdRequest(_message.Message):
    __slots__ = ["terminal_id", "user_id"]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    terminal_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., terminal_id: _Optional[str] = ...) -> None: ...

class GetRetailerTerminalByTerminalIdResponse(_message.Message):
    __slots__ = ["terminal"]
    TERMINAL_FIELD_NUMBER: _ClassVar[int]
    terminal: str
    def __init__(self, terminal: _Optional[str] = ...) -> None: ...

class Retailer(_message.Message):
    __slots__ = ["account_number", "bank_code", "business_name", "business_type", "bvn", "category", "classification", "id", "is_blacklisted", "is_validated", "user_id", "wallet_balance"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    BVN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    IS_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WALLET_BALANCE_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    bank_code: str
    business_name: str
    business_type: str
    bvn: str
    category: str
    classification: str
    id: str
    is_blacklisted: bool
    is_validated: bool
    user_id: str
    wallet_balance: float
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_name: _Optional[str] = ..., business_type: _Optional[str] = ..., category: _Optional[str] = ..., classification: _Optional[str] = ..., account_number: _Optional[str] = ..., bank_code: _Optional[str] = ..., bvn: _Optional[str] = ..., is_validated: bool = ..., is_blacklisted: bool = ..., wallet_balance: _Optional[float] = ...) -> None: ...

class UpdateRetailerByUserIdRequest(_message.Message):
    __slots__ = ["retailer"]
    RETAILER_FIELD_NUMBER: _ClassVar[int]
    retailer: Retailer
    def __init__(self, retailer: _Optional[_Union[Retailer, _Mapping]] = ...) -> None: ...

class UpdateRetailerByUserIdResponse(_message.Message):
    __slots__ = ["retailer"]
    RETAILER_FIELD_NUMBER: _ClassVar[int]
    retailer: Retailer
    def __init__(self, retailer: _Optional[_Union[Retailer, _Mapping]] = ...) -> None: ...
