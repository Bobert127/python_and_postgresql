from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

# def execute_sql(database, sql):
sql = "Select * from products"
user = 'postgres'
password = 'coderslab'
host = 'localhost'
database = 'exercises_db'
cnx = connect(user=user, password=password, host=host, database=database)
# cursor = cnx.cursor(cursor_factory=RealDictCursor)
cursor = cnx.cursor()
cursor.execute(sql)
for row in cursor:
    print(row)

cnx.commit()
cnx.close()
