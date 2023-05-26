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
    __slots__ = ["closest_landmark", "delivery_address", "device_id", "id", "price", "retailer_id", "state", "status"]
    CLOSEST_LANDMARK_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    RETAILER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    closest_landmark: str
    delivery_address: str
    device_id: str
    id: str
    price: float
    retailer_id: str
    state: str
    status: str
    def __init__(self, id: _Optional[str] = ..., retailer_id: _Optional[str] = ..., device_id: _Optional[str] = ..., price: _Optional[float] = ..., state: _Optional[str] = ..., status: _Optional[str] = ..., delivery_address: _Optional[str] = ..., closest_landmark: _Optional[str] = ...) -> None: ...

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

class GetDeviceTerminalIdByRetailerIdRequest(_message.Message):
    __slots__ = ["retailer_id"]
    RETAILER_ID_FIELD_NUMBER: _ClassVar[int]
    retailer_id: str
    def __init__(self, retailer_id: _Optional[str] = ...) -> None: ...

class GetDeviceTerminalIdByRetailerIdResponse(_message.Message):
    __slots__ = ["device_id"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

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

class Retailer(_message.Message):
    __slots__ = ["business_name", "business_type", "category", "classification", "id", "user_id"]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    business_type: str
    category: str
    classification: str
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., business_name: _Optional[str] = ..., business_type: _Optional[str] = ..., category: _Optional[str] = ..., classification: _Optional[str] = ...) -> None: ...
