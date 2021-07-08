from flask import Flask, request

app = Flask(__name__)

FORM1 = """
<form method='GET'>
    <label for="name">liczba1:</label><br>
    <input type = "float" id = "name" name  = "liczba1"><br>
    <label for="name">dzialanie</label><br>
    <input type = "list" id = "name" name = "dzialanie"><br>
    <label for="name">liczba2:</label><br>
    <input type = "float" id = "name" name  = "liczba2"><br>
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
@app.route("/liczby/")
def get_twojeliczby():
    liczba1_return = request.args["liczba1"]
    liczba2_return = request.args["liczba2"]
    return liczba1_return "+" liczba2_return  + "!"

if __name__ == '__main__':
    app.run(debug=True)
