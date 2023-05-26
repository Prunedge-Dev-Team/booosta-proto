from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDVARequest(_message.Message):
    __slots__ = ["account_number", "bank_code", "bvn", "email", "first_name", "last_name", "middle_name", "phone"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    BVN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    bank_code: str
    bvn: str
    email: str
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    def __init__(self, email: _Optional[str] = ..., first_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone: _Optional[str] = ..., account_number: _Optional[str] = ..., bvn: _Optional[str] = ..., bank_code: _Optional[str] = ...) -> None: ...

class CreateDVAResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class FetchCustomerDVARequest(_message.Message):
    __slots__ = ["email_or_phone"]
    EMAIL_OR_PHONE_FIELD_NUMBER: _ClassVar[int]
    email_or_phone: str
    def __init__(self, email_or_phone: _Optional[str] = ...) -> None: ...

class FetchCustomerDVAResponse(_message.Message):
    __slots__ = ["account_name", "account_number", "active", "assigned", "bank_id", "bank_name", "bank_slug", "currency", "id", "status"]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_SLUG_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    account_number: str
    active: bool
    assigned: bool
    bank_id: str
    bank_name: str
    bank_slug: str
    currency: str
    id: str
    status: bool
    def __init__(self, bank_name: _Optional[str] = ..., bank_id: _Optional[str] = ..., bank_slug: _Optional[str] = ..., id: _Optional[str] = ..., account_name: _Optional[str] = ..., account_number: _Optional[str] = ..., currency: _Optional[str] = ..., active: bool = ..., assigned: bool = ..., status: bool = ...) -> None: ...

class RequeryVDARequest(_message.Message):
    __slots__ = ["account_number", "provider_slug", "txn_date"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_SLUG_FIELD_NUMBER: _ClassVar[int]
    TXN_DATE_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    provider_slug: str
    txn_date: str
    def __init__(self, account_number: _Optional[str] = ..., provider_slug: _Optional[str] = ..., txn_date: _Optional[str] = ...) -> None: ...

class ResolveAccountNumberRequest(_message.Message):
    __slots__ = ["account_number", "bank_code"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    bank_code: str
    def __init__(self, account_number: _Optional[str] = ..., bank_code: _Optional[str] = ...) -> None: ...

class ResolveAccountResponse(_message.Message):
    __slots__ = ["account_name", "account_number", "bank_id", "message", "status"]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    account_number: str
    bank_id: str
    message: str
    status: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., account_number: _Optional[str] = ..., account_name: _Optional[str] = ..., bank_id: _Optional[str] = ...) -> None: ...

class VerifyBVNRequest(_message.Message):
    __slots__ = ["account_number", "bank_code", "bvn", "first_name", "last_name", "middle_name"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    BVN_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    bank_code: str
    bvn: str
    first_name: str
    last_name: str
    middle_name: str
    def __init__(self, bvn: _Optional[str] = ..., account_number: _Optional[str] = ..., bank_code: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ...) -> None: ...

class VerifyBVNResponse(_message.Message):
    __slots__ = ["account_number", "bvn", "first_name", "is_blacklisted", "last_name", "message", "middle_name", "status"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BVN_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_number: bool
    bvn: str
    first_name: bool
    is_blacklisted: bool
    last_name: bool
    message: str
    middle_name: bool
    status: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., bvn: _Optional[str] = ..., is_blacklisted: bool = ..., account_number: bool = ..., first_name: bool = ..., middle_name: bool = ..., last_name: bool = ...) -> None: ...
