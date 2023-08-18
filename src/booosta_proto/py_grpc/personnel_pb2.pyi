from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Retailer(_message.Message):
    __slots__ = ["id", "user_id", "business_name", "business_type", "category", "classification", "account_number", "bank_code", "bvn", "is_validated", "is_blacklisted", "wallet_balance", "image"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    BVN_FIELD_NUMBER: _ClassVar[int]
    IS_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    IS_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    WALLET_BALANCE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    business_name: str
    business_type: str
    category: str
    classification: str
    account_number: str
    bank_code: str
    bvn: str
    is_validated: bool
    is_blacklisted: bool
    wallet_balance: float
    image: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_name: _Optional[str] = ..., business_type: _Optional[str] = ..., category: _Optional[str] = ..., classification: _Optional[str] = ..., account_number: _Optional[str] = ..., bank_code: _Optional[str] = ..., bvn: _Optional[str] = ..., is_validated: bool = ..., is_blacklisted: bool = ..., wallet_balance: _Optional[float] = ..., image: _Optional[str] = ...) -> None: ...

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

class Agent(_message.Message):
    __slots__ = ["id", "user_id", "business_information"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    business_information: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_information: _Optional[str] = ...) -> None: ...

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

class Aggregator(_message.Message):
    __slots__ = ["id", "user_id", "business_information", "company_type", "company_size", "estimated_customer_base", "aggregator_code", "contact_name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_SIZE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CUSTOMER_BASE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    business_information: str
    company_type: str
    company_size: str
    estimated_customer_base: str
    aggregator_code: str
    contact_name: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_information: _Optional[str] = ..., company_type: _Optional[str] = ..., company_size: _Optional[str] = ..., estimated_customer_base: _Optional[str] = ..., aggregator_code: _Optional[str] = ..., contact_name: _Optional[str] = ...) -> None: ...

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

class Device(_message.Message):
    __slots__ = ["id", "user_id", "device_id", "price", "state", "status", "delivery_address", "closest_landmark"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLOSEST_LANDMARK_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    device_id: str
    price: float
    state: str
    status: str
    delivery_address: str
    closest_landmark: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., price: _Optional[float] = ..., state: _Optional[str] = ..., status: _Optional[str] = ..., delivery_address: _Optional[str] = ..., closest_landmark: _Optional[str] = ...) -> None: ...

class GetRetailerTerminalByTerminalIdRequest(_message.Message):
    __slots__ = ["user_id", "terminal_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    terminal_id: str
    def __init__(self, user_id: _Optional[str] = ..., terminal_id: _Optional[str] = ...) -> None: ...

class GetRetailerTerminalByTerminalIdResponse(_message.Message):
    __slots__ = ["terminal"]
    TERMINAL_FIELD_NUMBER: _ClassVar[int]
    terminal: str
    def __init__(self, terminal: _Optional[str] = ...) -> None: ...

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
