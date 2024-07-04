import httpx
from src.model.model import User


def get_user(url_api: str, count: int = 1):

    url_api = f"{url_api}{count}"

    response: httpx.Response = httpx.get(url_api)

    if response.status_code == 200:
        try:
            #  Список словарей с данными пользователей
            results_dicts: list[dict] = response.json()["results"]

            #  Список объектов класса User
            users_data: list[User] = [User(**user) for user in results_dicts]

            return users_data

        except (TypeError, ValueError, KeyError):

            return response.status_code
