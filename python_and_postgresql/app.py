from sqlite3 import OperationalError

from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

FORM = """
<form method='POST'>
    <label for="name">name:</label><br>
    <input type = "string" name  = "name"><br>
    <label for="name">description</label><br>
    <input type = "string"  name = "description"><br>
    <label for="name">price:</label><br>
    <input type = "float" name  = "price"><br>
    <label><button type="submit"> Prześlij</button></label>
</form>
 """


#
def get_return_date(cur, name, description, price):
    sql = "insert into items(name, description, price) values(%s, %s, %s)"
    values = (name, description, price)
    cur.execute(sql, values)


@app.route("/add_product/", methods=("POST", "GET"))
def produkc_return():
    if request.method == "GET":
        return FORM
    else:
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        if len(name) > 60 or not price or not description:
            return "Invalid date !!!"

        try:
            con = connect(database="exam2", user="postgres", password="coderslab", host="localhost")
            con.autocommit = True
            cursor = con.cursor()
            get_return_date(cursor, name, description, price)
            con.close()
            return "Product added!"
        except OperationalError as e:
            return e

if __name__ == '__main__':
    app.run(debug=True)
