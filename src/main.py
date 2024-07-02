# -*- coding: utf-8 -*-
import re
from src.interfaceAPI.obtaining import getUser
from src.interfaceAPI.model import User
from connectionDB import Connector
from connectionDB import InsertData
from validators.validation import validateEmail

emails = ['reboie@iewn.com', 'wnifw@venv', 'wufebiwnfio', 'finbfo@.ifnie', 'levacloud@mail.ru']
def main():



    users = getUser(1)
    # print(user, sep='\n')

    con = Connector(host="127.0.0.1",
                  dbname="de_projects",
                  user="admin",
                  password="password",
                  port=8888,
                    b=False)

    id = InsertData(con)
    id.insert_data(users[0])
    #
    # for user in users:
    #     if user.email_validation:
    #         urepo.load_user(user)
    #     print(user.login.password_validation, user.email_validation, sep= '<-password\temail->')
    #




if __name__ == '__main__':
    main()
