import re
def validate_password(password: str) -> bool:
    return not (not bool(re.search(r"[A-Z]", password)) or not bool(
        re.search(r"[a-z]", password))) and bool(re.search(r"\d", password)) and bool(re.search(r"[!\"#$%&'()*+,\- ./:;<=>?@\[\]^_`{|}~]", password))



#print(type(response.read()))






