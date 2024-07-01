create table if not exists users(
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

