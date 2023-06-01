from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditLog(_message.Message):
    __slots__ = ["activity_type", "description", "user_id"]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    activity_type: str
    description: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., activity_type: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GenerateEnumerationCodeRequest(_message.Message):
    __slots__ = ["enumeration_type", "length", "reg_code"]
    ENUMERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    REG_CODE_FIELD_NUMBER: _ClassVar[int]
    enumeration_type: str
    length: int
    reg_code: str
    def __init__(self, reg_code: _Optional[str] = ..., enumeration_type: _Optional[str] = ..., length: _Optional[int] = ...) -> None: ...

class GenerateEnumerationCodeResponse(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class GetUserByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserByIdResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class SaveAuditLogRequest(_message.Message):
    __slots__ = ["audit_log"]
    AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    audit_log: AuditLog
    def __init__(self, audit_log: _Optional[_Union[AuditLog, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["email", "firstname", "id", "image", "lastname", "middlename", "phone"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLENAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    email: str
    firstname: str
    id: str
    image: str
    lastname: str
    middlename: str
    phone: str
    def __init__(self, id: _Optional[str] = ..., firstname: _Optional[str] = ..., lastname: _Optional[str] = ..., middlename: _Optional[str] = ..., image: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
