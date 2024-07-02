import httpx
from src.interfaceAPI.model import User


def getUser(count: int = 1):

    url_api = f"https://randomuser.me/api/?password=special,upper,lower,number&results={count}"

    response: httpx.Response = httpx.get(url_api)

    if response.status_code == 200:
        try:
            # Список словарей с данными пользователей
            resultsDicts: list[dict] = response.json()['results']
            #  Список объектов класса User
            usersData: list[User] = [User(**user) for user in resultsDicts]
            return usersData
        except (TypeError, ValueError, KeyError) as e:
            print(e)
            return None
