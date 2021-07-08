# def shorten(text):
#     return ''.join(word[0] for word in text.split()).upper()
#
#
# if __name__ == '__main__':
#     shortened = shorten("Dont me")
#     print(shortened)

# napis = "abcdefghijklmnop"
# print (napis[3:7])

# def name_sorter(names):
#     result = {
#     'female': [],
#     'male': []
#     }
#     for name in names:
#         if name[-1] == 'a':
#             result['female'].append(name)
#         else:
#             result['male'].append(name)
#     return result
#
# if __name__ == '__main__':
#
#     input = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara", "Zenon", "Ewa"]
#     print(name_sorter(input))

# def check_palindrome(text):
#     text = text.lower().replace(' ', '')
#     return text == text[::-1]
#
#
# if __name__ == '__main__':
#     print(check_palindrome("Kobyła ma mały bok"))
#     print(check_palindrome("To nie jest palindrom"))

# def div(start, stop):
#     return [i for i in range(start, stop + 1) if i % 2 == 0 and i % 3 != 0]
#
#  if __name__ == '__main__':
#      print(div(7,17))


# def div(start, stop):
#     """Make list with numbers divided by 2 and not divided by 3 from start to end (both sides included).
#     :param int start: start range
#     :param int end: end range
#     :rtype: list
#     :return: numbers from start to end divided by 2 and not divided by 3
#     """
#     return [i for i in range(start, stop + 1) if i % 2 == 0 and i % 5 != 0]
#
#
# if __name__ == '__main__':
#     print(div(7, 170))
# import random
#
#
# def roll(kostki, typ = 6, mody = 0):
#     if kostki not in (3, 4, 6, 8, 10, 12, 100):
#         raise Exception("No such dice!")
#     return sum(random.randint(1, typ) for _ in range(kostki)) + mody
#
#
# if __name__ == '__main__':
#     print(roll(10,7,8))

# from flask import Flask, request
# from exam import movies
#
#
# app = Flask(__name__)
#
#
# FORM = """
# <form method="POST">
#     <label for="title">Insert title:</label><br>
#     <input type="text" id="title" name="title"><br>
#     <input type="submit" value="Submit">
# </form>
# """
# from flask import Flask, request
# from exam import movies
#
#
# app = Flask(__name__)
#
#
# FORM = """
# <form method="POST">
#     <label for="title">Insert title:</label><br>
#     <input type="text" id="title" name="title"><br>
#     <input type="submit" value="Submit">
# </form>
# """
#
#
# @app.route("/movies/", methods=("GET", "POST"))
# def movies_view():
#     if request.method == "GET":
#         return FORM
#     else:
#         title = request.form.get("title")
#         if title in movies["favourite"]:
#             return "favourite"
#         elif title in movies["hated"]:
#             return "hated"
#         else:
#             return "no such movie!"
#
#
# if __name__ == '__main__':
#     app.run()
#
#
# @app.route("/movies/", methods=("GET", "POST"))
# def movies_view():
#     if request.method == "GET":
#         return FORM
#     else:
#         title = request.form.get("title")
#         if title in movies["favourite"]:
#             return "favourite"
#         elif title in movies["hated"]:
#             return "hated"
#         else:
#             return "no such movie!"
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)