# -*- coding: utf-8 -*-
import re
from src.response_parsing.pars import *
from src.CRUDs.ddl import *

emails = ['reboie@iewn.com', 'wnifw@venv', 'wufebiwnfio', 'finbfo@.ifnie', 'levacloud@mail.ru']
def main():

    '''for email in emails:
        validator = UserValidator(email = email, password='ejirfbui')
        #email = user.email
        #print(email, validator.validateEmail())
        #print(bool(re.search(r"[A-Z]", r"riobnrlTk")))

    validator = UserValidator(password=getUser(1)[0].login.password)
    print(validator.password, validator.validatePassword())'''

    user = getUser(1)




if __name__ == '__main__':
    main()
