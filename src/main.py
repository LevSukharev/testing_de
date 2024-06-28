# -*- coding: utf-8 -*-
import re

from src.response_parsing.pars import *
from src.userValidator import validate_password

def main():
    for user in getUser(100):
        password = user.login.password
        print(password)
        print(validate_password(password))
        #print(bool(re.search(r"[A-Z]", r"riobnrlTk")))


if __name__ == '__main__':
    main()
