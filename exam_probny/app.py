from flask import Flask, request

app = Flask(__name__)

FORM = """
<form method='GET' action="/twojeimie/">
    <label for="name">Podaj imię:</label><br>
    <input type = "text" id = "name" name  = "name1"><br>
    <label><button type="submit"> Prześlij</button></label>
</form>
 """

@app.route("/imie/")

def get_imie():
    if request.method == "GET":
        return FORM


@app.route("/twojeimie/")
def get_twojeimie():
    twoje_imie_return = request.args["name1"]
    return "Witaj " + twoje_imie_return + "!"


if __name__ == '__main__':
    app.run(debug=True)
