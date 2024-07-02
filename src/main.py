# -*- coding: utf-8 -*-
import re
from src.interfaceAPI.obtaining import getUser
from src.interfaceAPI.model import User
from connectionDB import Connector, InsertData
from src.validators.validation import password_validate


def main():

    #users = getUser(10)
    user = getUser(1)
    print(user)

    con = Connector(host="127.0.0.1",
                  dbname="de_projects",
                  user="admin",
                  password="password",
                  port=8888,
                    b=False)

    id = InsertData(con)
    #id.insert_data(users[0])





if __name__ == '__main__':
    main()
