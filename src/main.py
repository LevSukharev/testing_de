# -*- coding: utf-8 -*-
from interfaceAPI import get_user
from connectionDB import Connector, InsertData, SelectData
import logging
import os
from settings import settings


log_dir = os.path.join(os.path.dirname(os.getcwd()), "logs")

log_file = os.path.join(log_dir, "log.log")

logging.basicConfig(
    filename=log_file,
    filemode="w",
    encoding="utf-8",
    level=(logging.WARNING, logging.DEBUG)[settings.debug],
    format="%(asctime)s (%(module)s): [%(levelname)s] - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

logger = logging.getLogger()


def main():

    try:
        con = Connector(
            host=settings.host,
            dbname=settings.dbname,
            user=settings.user,
            password=settings.password,
            port=settings.port,
        )

        logger.info(f"Successfully connection {con.connector}")

    except Exception as e:
        con = None
        logger.error(f"In db connection {e}")

    try:
        users = get_user(url_api=settings.url_api)

        logger.info("Successfully obtaining")

    except Exception as e:
        users = None
        logger.error(f"In obtain user {e}")

    try:
        idata = InsertData(con)

    except Exception as e:
        logger.error(f"In creation insert object {e}")
        idata = None

    try:
        for user in users:
            idata.insert_data(user=user)

    except Exception as e:
        logger.error(f"In insertion {e}")

    try:
        sdata = SelectData(con)

    except Exception as e:
        logger.error(f"In creation select object {e}")
        sdata = None

    try:
        users = sdata.select_data(valid_password=False, valid_email=True)

    except Exception as e:
        logger.error(f"In selection {e}")
        users = tuple()

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
