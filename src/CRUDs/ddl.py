import psycopg2
from psycopg2.extras import RealDictCursor
from src.response_parsing.models.user import User




class DatabaseSchema:
    def __init__(self, db: Database):
        self.db = db

    def createTable(self):
        create_tables_query = """create table if not exists users(
        	user_id serial primary key,
        	gender varchar(10),
        	name_title varchar(50),
        	name_first varchar(50),
        	name_last varchar(50),
        	age int,
        	nat varchar(50),
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp
        );

        create table if not exists cities(
        	city_id serial primary key,
        	city varchar(50) not null,
        	state varchar(50) not null,
        	country varchar(50) not null,
        	timezone_offset varchar(20) not null,
        	timezone_description varchar(100),
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp
        );

        create table if not exists locations(
        	user_id serial primary key,
        	city_id int,
        	street_name varchar(50),
        	street_number int,
        	postcode varchar(50),
        	latitude decimal(9,6) not null,
        	longtitude decimal(9,6) not null,
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp,
        	foreign key(user_id) references users(user_id) on delete cascade on update cascade,
        	foreign key(city_id) references cities(city_id) on delete cascade on update cascade
        );

        create table if not exists contact_deta(
        	user_id serial primary key,
        	phone varchar(20),
        	cell varchar(50),
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp,
        	foreign key(user_id) references users(user_id) on delete cascade on update cascade
        );

        create table if not exists media_data(
        	user_id serial primary key,
        	picture varchar(100),
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp,
        	foreign key(user_id) references users(user_id) on delete cascade on update cascade
        );

        create table if not exists registration_data(
        	user_id serial primary key,
        	email varchar(50),
        	username varchar(50) not null,
        	password varchar(255) not null,
        	password_md5 varchar(100) not null,
        	password_validation bool,
        	created_dttm timestamp default current_timestamp,
        	updated_dttm timestamp default current_timestamp,
        	foreign key(user_id) references users(user_id) on delete cascade on update cascade
        );

        create or replace function update_updated_column()
        returns trigger as $$
        begin
        	new.updated_dttm = current_timestamp;
        	return new;
        end;
        $$ language plpgsql;

        create trigger before_update_users
        before update on users
        for each row execute function update_updated_column();

        create trigger before_update_cities
        before update on cities
        for each row execute function update_updated_column();

        create trigger before_update_locations
        before update on locations
        for each row execute function update_updated_column();

        create trigger before_update_contact_deta
        before update on contact_deta
        for each row execute function update_updated_column();

        create trigger before_update_media_data
        before update on media_data
        for each row execute function update_updated_column();

        create trigger before_update_registration_data
        before update on registration_data
        for each row execute function update_updated_column();
        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(create_tables_query)
        self.db.connection.commit()
class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def create_city(self, user: User):
        insert_city_query = """
                insert into cities (city, state, country, timezone_offset, timezone_description)
                values (%s, %s, %s, %s, %s) returning city_id
                """
        city_params = (user.location.city
                       , user.location.state
                       , user.location.country
                       , user.location.timezone.offset
                       , user.location.timezone.description)
        city_result = self.db.execute(insert_city_query, city_params)
        self.city_id = city_result[0]["city_id"]

    def create_user(self, user: User):

        insert_user_query = """
        insert into users (gender, name_title, name_first, name_last, age, nat)
        values (%s, %s, %s, %s, %s, %s) returning user_id
        """
        user_params = (user.gender
                       ,user.name.name_title
                       ,user.name.name_first
                       ,user.name.name_last
                       ,user.dob.age, user.nat)
        user_result = self.db.execute(insert_user_query, user_params)
        user_id = user_result[0]["user_id"]

        insert_contact_query = """
        insert into contact_details (phone, cell)
        values (%s, %s)
        """
        contact_params = (user_id
                          ,user.phone
                          ,user.cell)
        self.db.execute(insert_contact_query, contact_params)

        insert_media_query = """
        insert into media_data (user_id, picture)
        values (%s, %s)
        """
        media_params = (user_id
                        ,user.picture.thumbnail)
        self.db.execute(insert_media_query, media_params)

        insert_registration_query = """
        insert into registration_data (user_id, email, username, password, password_md5, password_validation)
        values (%s, %s, %s, %s, %s, %s)
        """
        registration_params = (user_id
                               ,user.email
                               ,user.login.username
                               ,user.login.password, user.login.password_md5
                               ,int(UserValidator(password=user.login.password).validatePassword()))
        self.db.execute(insert_registration_query, registration_params)

        insert_locations_query = """
        insert into locations (user_id, city_id, street_name, stree_number, postcode, latitude, longtitude)
        values (%s, %s, %s, %s, %s, %s, %s)
        """
        locations_params = (user_id
                            ,city_id
                            ,user.location.street.name
                            ,user.location.street.number
                            ,user.location.postcode
                            ,user.location.coordinates.latitude
                            ,user.location.coordinates.longitude)
        self.db.execute(insert_locations_query, locations_params)

        return user_id

