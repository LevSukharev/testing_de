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
    db = Database(host="127.0.0.1", dbname="de_projects", user="admin", password="password", port="8888")
    db.connect()

    #schema = DatabaseSchema(db)
    #schema.createTable()

    user_repo = UserRepository(db)
    user_repo.create_user(user[0])

    db.closeConnection()




if __name__ == '__main__':
    main()
