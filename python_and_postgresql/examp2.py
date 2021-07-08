from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

CREATE_DB = "CREATE DATABASE exam2"
DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    cnx = connect(database="exam", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)

guery_1 = """
Create table Users (
id serial PRIMARY KEY,
name varchar(60),
email varchar(60),
password varchar(60)
)
"""

guery_2 = """
Create table Messages (
id serial PRIMARY KEY,
user_id int,
message  text
)
"""

guery_3 = """
Create table Items (
id serial PRIMARY KEY,
name varchar(60),
description  text,
price decimal(7,2)
)
"""

guery_34= """
Create table Orders (
id serial PRIMARY KEY,
description  text
)
"""

query_5 = """CREATE TABLE ItemsOrders(
    id serial PRIMARY KEY,
    item_id int REFERENCES Items (id) ON DELETE CASCADE,
    order_id int REFERENCES Orders (id) ON DELETE CASCADE
)"""