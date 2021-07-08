from flask import Flask, request

app = Flask(__name__)

FORM1 = """
<form method='GET'>
    <label for="name">liczba1:</label><br>
    <input type = "float" id = "name" name  = "name1"><br>
    <label><button type="submit"> Prześlij</button></label>
</form>
 """
#
#
@app.route("/liczby/")
#
def get_liczby():
    if request.method == "GET":
    return FORM1
#
# @app.route("/twojeimie/")
# def get_twojeimie():
#     twoje_imie_return = request.args["name1"]
#     return "Witaj " + twoje_imie_return + "!"

if __name__ == '__main__':
    app.run(debug=True)
