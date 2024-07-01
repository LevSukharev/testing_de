import psycopg2
from psycopg2.extras import RealDictCursor
from src.response_parsing.pars import *
from src.userValidator import UserValidator


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


    def execute_city(self, user: User):
        insert_city_query = """
                insert into cities (city, state, country, timezone_offset, timezone_description)
                values (%s, %s, %s, %s, %s)
                """
        city_params = (user.location.city,
                       user.location.state,
                       user.location.country,
                       user.location.timezone.offset,
                       user.location.timezone.description)

        return insert_city_query, city_params

    def execute_user(self, user: User):
        insert_user_query = """
                insert into users (gender, name_title, name_first, name_last, age, nat)
                values (%s, %s, %s, %s, %s, %s)
                """
        user_params = (user.gender,
                       user.name.name_title,
                       user.name.name_first,
                       user.name.name_last,
                       user.dob.age,
                       user.nat)

        return insert_user_query, user_params

    def execute_locations(self, user: User):
        insert_locations_query = """
                insert into locations (user_id, city_id, street_name, stree_number, postcode, latitude, longtitude)
                values (%s, %s, %s, %s, %s, %s, %s)
                """
        locations_params = (user_id,
                            city_id,
                            user.location.street.name,
                            user.location.street.number,
                            user.location.postcode,
                            user.location.coordinates.latitude,
                            user.location.coordinates.longitude)

        return insert_locations_query, locations_params

    def execute_contact_details_query(self, user: User):
        insert_contact_details_query = """
                insert into contact_details (phone, cell)
                values (%s, %s)
                """
        contact_details_params = (user_id,
                          user.phone,
                          user.cell)

        return insert_contact_details_query, contact_details_params

    def execute_media_data_query(self, user: User):
        insert_media_data_query = """
                insert into media_data (user_id, picture)
                values (%s, %s)
                """
        media_data_params = (user_id,
                             user.picture.thumbnail)

        return insert_media_data_query, media_data_params

    def execute_registration_data_query(self, user: User):
        insert_registration_query = """
                insert into registration_data (user_id, email, username, password, password_md5, password_validation)
                values (%s, %s, %s, %s, %s, %s)
                """
        registration_params = (user_id,
                               user.email,
                               user.login.username,
                               user.login.password, user.login.password_md5,
                               UserValidator(password=user.login.password).validatePassword())

        return insert_registration_query, registration_params

    def load_user(self, db: Database, user: User):
        db.execute(*self.execute_city(user))
        db.execute(*self.execute_user(user))
        db.execute(*self.execute_locations(user))


if __name__ == '__main__':

    db = Database(host="127.0.0.1",
                  dbname="de_projects",
                  user="admin",
                  password="password",
                  port=8888)

    user = getUser(1)
    user_repo = UserRepository()
    user_repo.execute_city(user)

    '''db.execute("""
                insert into cities (city, state, country, timezone_offset, timezone_description)
                values (%s, %s, %s, %s, %s) returning city_id
                """, (user.location.city
                       , user.location.state
                       , user.location.country
                       , user.location.timezone.offset
                       , user.location.timezone.description))'''
