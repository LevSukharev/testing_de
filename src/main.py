# -*- coding: utf-8 -*-
import os
from interfaceAPI import get_user
from connectionDB import Connector, InsertData, SelectData
from dotenv import load_dotenv
from loguru import logger
from settings import settings

logger.add("full.log", format="{time} {level} {message}", level='DEBUG')


def main():

    try:
        load_dotenv()

        logger.debug(f'[{__file__}] Env was loaded')
    except Exception as e:
        logger.error(e)

    con = Connector(host=settings.host,
                    dbname=settings.dbname,
                    user=settings.user,
                    password=settings.password,
                    port=settings.port)

    users = get_user(count=4, url_api=settings.url_api)

    idata = InsertData(con)

    for user in users:
        idata.insert_data(user=user)

    input('Select users?')

    sdata = SelectData(con)

    users = sdata.select_data(valid_password=False, valid_email=True, limit=2)

    for user in users:
        print(user)


if __name__ == '__main__':
    main()
