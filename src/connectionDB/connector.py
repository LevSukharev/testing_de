import psycopg2
from loguru import logger

logger.add("full.log", format="{time} {level} {message}", level='DEBUG')


class Connector:

    def __init__(self, dbname, user, password, host, port, b=True):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.b = b

        self.connector = self.__connect()

    def __connect(self):
        try:
            connector = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

            logger.debug(f'Connector object {connector} successfully created')

            return connector

        except Exception as e:
            logger.error(f'[ERROR] connection error: {e}')


    def execute_query(self, query: str, params: tuple = None) -> any:
        with self.connector.cursor() as cursor:
            cursor.execute(query, params)
            self.connector.commit()

            if cursor.description and not self.b:
                return cursor.fetchone()[0]
            elif cursor.description and self.b:
                return cursor.fetchall()
            else:
                return cursor.rowcount
