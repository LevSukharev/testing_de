from src.interfaceAPI.model import User


def execute_city(user: User):
    insert_city_query = """
            insert into cities (city, state, country, timezone_offset, timezone_description)
            values (%s, %s, %s, %s, %s) returning city_id
            """
    city_params = (user.location.city,
                   user.location.state,
                   user.location.country,
                   user.location.timezone.offset,
                   user.location.timezone.description)
    return insert_city_query, city_params


def execute_user(user: User):
    insert_user_query = """
            insert into users (gender, name_title, name_first, name_last, age, nat)
            values (%s, %s, %s, %s, %s, %s) returning user_id
            """
    user_params = (user.gender,
                   user.name.name_title,
                   user.name.name_first,
                   user.name.name_last,
                   user.dob.age,
                   user.nat)
    return insert_user_query, user_params


def execute_locations(user: User, user_id: int, city_id: int):
    insert_locations_query = """
            insert into locations (user_id, city_id, street_name, street_number, postcode, latitude, longtitude)
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


def execute_contact_details_query(user: User, user_id: int):
    insert_contact_details_query = """
            insert into contact_details (user_id, phone, cell)
            values (%s, %s, %s)
            """
    contact_details_params = (user_id,
                              user.phone,
                              user.cell)

    return insert_contact_details_query, contact_details_params


def execute_media_data_query(user: User, user_id: int):
    insert_media_data_query = """
            insert into media_data (user_id, picture)
            values (%s, %s)
            """
    media_data_params = (user_id,
                         user.picture.thumbnail)

    return insert_media_data_query, media_data_params


def execute_registration_data_query(user: User, user_id: int):
    insert_registration_query = """
            insert into registration_data (user_id, email, username, password, 
            password_md5, password_validation, email_validation)
            values (%s, %s, %s, %s, %s, %s, %s)
            """
    registration_params = (user_id,
                           user.email,
                           user.login.username,
                           user.login.password,
                           user.login.password_md5,
                           user.login.password_validation,
                           user.email_validation)


    return insert_registration_query, registration_params

