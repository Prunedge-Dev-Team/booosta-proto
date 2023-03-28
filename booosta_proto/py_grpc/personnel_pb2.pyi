from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
