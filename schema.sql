CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists country(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists city(
        id integer primary key autoincrement,
        name text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists sql_girl_not_part(
        id integer primary key autoincrement,
        not_condition text,
            is_not_applied text,
            sql_query_controller_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists sql_boy_part(
        id integer primary key autoincrement,
        positive_conditions text,
            select_clause text,
            sql_query_controller_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists rails_view_guard(
        id integer primary key autoincrement,
        view_template_path text,
            layout_format text,
            is_rendered text,
            rails_controller_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists rails_controller(
        id integer primary key autoincrement,
        controller_name text,
            action_name text,
            before_action_filters text,
            web_development_route_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            phone text,
            email text,
            password text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists street(
        id integer primary key autoincrement,
        name text,
            city_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists station(
        id integer primary key autoincrement,
        city_id text,
            name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists display_rule(
        id integer primary key autoincrement,
        display_mode text,
            title text,
            description text,
            web_development_route_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists pedestrian_route(
        id integer primary key autoincrement,
        lat text,
            lon text,
            street_id text,
            user_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists sql_query_controller(
        id integer primary key autoincrement,
        web_development_route_id text,
            query text,
            description text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists afficher(
        id integer primary key autoincrement,
        affichage text,
            web_development_route text,
            title text,
            description text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists webapp(
        id integer primary key autoincrement,
        name text,
            user_id text,
            description text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists waypoint(
        id integer primary key autoincrement,
        lat text,
            lon text,
            sequence_order text,
            pedestrian_route_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists web_development_route(
        id integer primary key autoincrement,
        name text,
            webapp_id text,
            description text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists train_conductor(
        id integer primary key autoincrement,
        name text,
            fm text,
            public_transportation_route_id text,
            pic text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists public_transportation_route(
        id integer primary key autoincrement,
        mean_of_transportation text,
            web_development_route_id text,
            pedestrian_route_id text,
            destination text,
            departure_station_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists query_log(
        id integer primary key autoincrement,
        executed_query text,
            executed_at text,
            sql_query_controller_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
