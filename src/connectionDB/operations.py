import psycopg2
from src.connectionDB.connector import Connector
from src.connectionDB.querys import (execute_locations,
                    execute_user,
                    execute_city,
                    execute_media_data_query,
                    execute_registration_data_query,
                    execute_contact_details_query)
from src.interfaceAPI.model import User



class InsertData:

    def __init__(self, connector: Connector):
        self.connector = connector
        self.b = False

    def insert_data(self, user: User) -> None:
        city_id = self.connector.execute_query(*execute_city(user))
        user_id = self.connector.execute_query(*execute_user(user))
        self.connector.execute_query(*execute_locations(user, user_id, city_id))
        self.connector.execute_query(*execute_contact_details_query(user, user_id))
        self.connector.execute_query(*execute_media_data_query(user, user_id))
        self.connector.execute_query(*execute_registration_data_query(user, user_id))



