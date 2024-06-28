# -*- coding: utf-8 -*-
import re

from src.response_parsing.pars import *
from src.userValidator import validate_password, validate_email

emails = ['reboie@iewn.com', 'wnifw@venv', 'wufebiwnfio', 'finbfo@.ifnie']
def main():
    for email in emails:
        #email = user.email
        print(email, validate_email(email))
        #print(bool(re.search(r"[A-Z]", r"riobnrlTk")))


if __name__ == '__main__':
    main()
