import re
'''class UserValidator:
    def __init__(self, password: str = "", email: str = ""):
        self.password = password
        self.email = email
    def validatePassword(self) -> bool:
        return (bool(re.search(r"[A-Z]", self.password)) and bool(
            re.search(r"[a-z]", self.password)) and bool(re.search(r"\d", self.password))
                and bool(re.search(r"[!\"#$%&'()*+,\- ./:;<=>?@\[\]^_`{|}~]", self.password)))

    def validateEmail(self) -> bool:
        return bool(re.search(r"\w{2,}@[a-z]{2,}.[a-z]{2,}", self.email))'''


def validatePassword(password: str) -> bool:
    return (bool(re.search(r"[A-Z]", password))
            and bool(re.search(r"[a-z]", password))
            and bool(re.search(r"\d", password))
            and bool(re.search(r"[!\"#$%&'()*+,\- ./:;<=>?@\[\]^_`{|}~]", password)))

def validateEmail(email: str) -> bool:
    return bool(re.search(r"\S{1,}@[a-z]{2,}.[a-z]{2,}", email))