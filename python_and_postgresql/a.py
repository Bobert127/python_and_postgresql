import psycopg2

USER = "postgres"
password = "coderslab"
host = "localhost"

sql = 'CREATE TABLE messages(
    id SERIAL,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'

cnx = connect(database="workshop", user=USER, password=password, host=host)
cnx.autocommit = True
cursor = cnx.cursor()
cursor.execute(sql)
cnx.close()
