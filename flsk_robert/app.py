from flask import Flask, render_template, request
from exam import movies

app = Flask(__name__)

Form = """
<form method="Post">
    <label for="title">Wprowadź tytuł:</label><br>
    <input type="text" id ="title" name="title"><br>
    <input type="submit" value="Submit">
</form>
"""


@app.route("/movies/", methods=("GET", "POST"))
def movies_view():
    if request.method == "GET":
        return Form
    else:
        title = request.form.get("title")
        if title in movies["favourite"]:
            return "favourite"
        elif title in movies["hated"]:
            return "hated"
        else:
            return "no such movie!"


@app.route("/film/", methods=("GET", "POST"))
def film():
    return "to są filmy"


@app.route("/muzyka/", methods=("GET", "POST"))
def muzyka():
    return "to jest dobra myzka"

if __name__ == '__main__':
    app.run()
