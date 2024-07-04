from src.connectionDB import Connector
from src.connectionDB.querys import (
    insert_locations,
    insert_user,
    insert_city,
    insert_media_data_query,
    insert_registration_data_query,
    insert_contact_details_query,
    select_all,
)
from src import User


class InsertData:

    def __init__(self, connector: Connector):
        self.connector = connector
        connector.b = False

    def insert_data(self, user: User) -> None:
        try:
            city_id = self.connector.execute_query(*insert_city(user))

            user_id = self.connector.execute_query(*insert_user(user))

            self.connector.execute_query(*insert_locations(user, user_id, city_id))

            self.connector.execute_query(*insert_contact_details_query(user, user_id))

            self.connector.execute_query(*insert_media_data_query(user, user_id))

            self.connector.execute_query(*insert_registration_data_query(user, user_id))

        except Exception:
            pass


class SelectData:

    def __init__(self, connector: Connector):
        self.connector = connector
        connector.b = True

    def select_data(
        self, valid_password: bool = False, valid_email: bool = False, limit: int = 0
    ):

        try:
            select_query_result = self.connector.execute_query(
                select_all(valid_password, valid_email, limit)
            )

            return select_query_result

        except Exception:
            return None
