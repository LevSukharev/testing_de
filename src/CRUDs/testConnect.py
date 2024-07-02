import psycopg2
from src.response_parsing.pars import *
from src.CRUDs.ddl_functions import *


class Database:
    def __init__(self, dbname, user, password, host, port, b=True):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.b = b

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

    def pushRow(self, query: str, params: tuple = None) -> any:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

            if cursor.description and not self.b:
                return cursor.fetchone()[0]
            elif cursor.description and self.b:
                return cursor.fetchall()
            else:
                return cursor.rowcount

    # def getRow(self, query: str, params: tuple = None) -> any:
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(query, params)
    #
    #         if cursor.description:
    #             return cursor.fetchall()
    #         else:
    #             return cursor.rowcount



class UserRepository:
    def __init__(self, db: Database):
        self.db = db

        self.db.b = True

    def load_user(self, user: User):
        city_id = db.pushRow(*execute_city(user))
        user_id = db.pushRow(*execute_user(user))
        db.pushRow(*execute_locations(user, user_id, city_id))
        db.pushRow(*execute_contact_details_query(user, user_id))
        db.pushRow(*execute_media_data_query(user, user_id))
        db.pushRow(*execute_registration_data_query(user, user_id))

    def get_user_from_db(self):
        with db.connection.cursor() as curs:
            curs.execute(f"""
            select {'*'} from users u 
			join locations l 
			  on u.user_id = l.user_id 
			  join cities c on l.city_id = c.city_id 
			  join contact_details cd on u.user_id = cd.user_id 
			join media_data md on u.user_id = md.user_id 
			join registration_data rd on rd.user_id = u.user_id """)

            print(curs.description)
            #return curs.fetchall()
            return db.getRow(f"""select from users u 
			join locations l on u.user_id = l.user_id 
			join cities c on l.city_id = c.city_id 
			join contact_details cd on u.user_id = cd.user_id 
			join media_data md on u.user_id = md.user_id 
			join registration_data rd on rd.user_id = u.user_id """)



if __name__ == '__main__':

    db = Database(host="127.0.0.1",
                  dbname="de_projects",
                  user="admin",
                  password="password",
                  port=8888)


    urepo = UserRepository(db)

    users = getUser(10)
    print(type(users[0]))
    # for user in users:
    #     if user.email_validation:
    #         urepo.load_user(user)
    #     print(user.login.password_validation, user.email_validation, sep= '<-password\temail->')
    #
    # select_res = urepo.get_user_from_db()
    # print(select_res)



