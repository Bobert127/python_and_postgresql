from sqlite3 import OperationalError

from psycopg2 import connect
from psycopg2.errors import DuplicateDatabase

CREATE_DB = "CREATE DATABASE workshop;"

create_users_table = """create table users (
    id serial PRIMARY KEY,
    username varchar(255) UNIQUE,
    hashed_password varchar(80)
)"""
create_messages_table = """ create table messages (
    id serial PRIMARY KEY,
    from_id INTEGER REFERENCES  users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES  users(id) ON DELETE CASCAD
    TEXT VARCHAR(255),
    creation_date timestamp DEAFULT CURRENT_TIMESTAMP
)"""
USER = "postgres"
password = "coderslab"
host = "localhost"



try:
    cnx = connect(user=USER, password=password, host=host)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as z:
        print("Database exists ", z)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", z)


try:
    cnx = connect(database="workshop", user=USER, password=password, host=host)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(create_users_table)
        print("Table users created")
    except DuplicateDatabase as d:
        print("Table exists ", d)
    cnx.close()
except OperationalError as d:
    print("Connection Error: ", d)


try:
    cnx = connect(database="workshop", user=USER, password=password, host=host)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(create_messages_table)
        print("Table created")
    except DuplicateDatabase as d:
        print("Table exists ", d)
    cnx.close()
except OperationalError as d:
    print("Connection Error: ", d)

