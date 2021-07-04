from create_db import password


class User:
    def __init__(self, usename="", password="", salt="")
        self._id = -1
        self.usename = usename
        self._hashed_password = hashed_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, passowrd, salt=""):
        self._hashed_password = hash_password(passowrd, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """Select  INTO users(username, hashed_password)
                              VALUES(%s, %s) RETURNING id"""
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        return False
