import uuid
import re

def sanitize_phone_number(value):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~`:;,.-]')
    if regex.search(value) != None:
        return {"message": "Invalid Phone Number"}
    if value.startswith("+") and len(value) == 14:
        return value
    elif len(value) == 10:
        return "+234" + value
    elif len(value) == 11 and value.startswith("0"):
        return "+234" + value[1:]
    elif len(value) == 13 and value.startswith("234"):
        return f"+{value}"
    return {"message": "Number {0} is invalid nigerian number".format(value)}

def generate_referral_code():
    code = str(uuid.uuid4()).replace("-", "")[:9]
    return code

def test_phone(phone):
    """this is used for google test"""
    if sanitize_phone_number(phone) == '+2348077339515':
        return True
    return None  

def paginate_queryset(qs, offset=None, limit=None, ordering=None):
    count = qs.count()
    if ordering:
        qs = qs.order_by(ordering)
    if offset:
        qs = qs[offset:]
    if limit:
        qs = qs[:limit]

    return {
        'total_count': count,
        'results': qs
    }
