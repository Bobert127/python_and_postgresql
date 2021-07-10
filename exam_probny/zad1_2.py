from psycopg2 import connect, OperationalError

from psycopg2.errors import DuplicateDatabase, DuplicateTable

query_2 = """
ALTER TABLE messages ADD COLUMN date_of_created timestamp DEFAULT NULL

"""

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "localhost"

try:
    con = connect(database="exam2", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    con.autocommit = True
    cursor = con.cursor()
    try:
        cursor.execute(query_2)
        print("Table create")
    except DuplicateTable as e:
        print("Table exists ", e)
    con.close()
except OperationalError as g:
    print("Connection ERROR ", g)