import psycopg2
from psycopg2.extras import RealDictCursor
from src.response_parsing.pars import *


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.__connect()

    def __connect(self):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

            print("Successful connection")

            return connection

        except Exception as e:
            print(f'[ERROR] connection error: {e}')

    def execute(self, query: str, params: tuple = None) -> any:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

class UserRepository:
    def __init__(self, db: Database):
        self.db


if __name__ == '__main__':

    db = Database(host="127.0.0.1",
                  dbname="de_projects",
                  user="admin",
                  password="password",
                  port=8888)

    user = getUser(1)


    '''db.execute("""
                insert into cities (city, state, country, timezone_offset, timezone_description)
                values (%s, %s, %s, %s, %s) returning city_id
                """, (user.location.city
                       , user.location.state
                       , user.location.country
                       , user.location.timezone.offset
                       , user.location.timezone.description))'''
