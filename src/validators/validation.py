import re
# from pydantic import validate_email

def validatePassword(password: str) -> bool:
    return (bool(re.search(r"[A-Z]", password))
            and bool(re.search(r"[a-z]", password))
            and bool(re.search(r"\d", password))
            and bool(re.search(r"[!\"#$%&'()*+,\- ./:;<=>?@\[\]^_`{|}~]", password)))

def validateEmail(email: str) -> bool:
    return bool(re.search(r"\S{1,}@[a-z]{2,}.[a-z]{2,}", email))