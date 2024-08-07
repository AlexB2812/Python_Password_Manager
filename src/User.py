class User:
    def __init__(self, username , password):
        self._username = username
        self._password = password
        self.myEntrys = []

    def getUsername(self):
        return self._username

    def setUsername(self, username):
        self._username = username

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password