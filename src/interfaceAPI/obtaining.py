import os

import httpx
from src import User
from dotenv import load_dotenv
from loguru import logger

logger.add("full.log", format="{time} {level}", level='DEBUG')

try:
    load_dotenv()

    logger.debug(f'[{__file__}] Env was loaded')
except Exception as e:
    logger.error(e)


def get_user(count: int = 1, url_api: str = os.getenv("URL_API")):

    url_api = f"{url_api}{count}"


    response: httpx.Response = httpx.get(url_api)

    if response.status_code == 200:
        try:
            #  Список словарей с данными пользователей
            results_dicts: list[dict] = response.json()['results']

            #  Список объектов класса User
            users_data: list[User] = [User(**user) for user in results_dicts]

            logger.debug(f'The data has been successful obtained')

            return users_data

        except (TypeError, ValueError, KeyError) as e:

            logger.error(f'[{__file__}] get_user error - {e}')

            return None
