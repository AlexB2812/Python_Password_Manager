class Entry:
    def __init__(self,password,url,notice):
        self._password = password
        self._url = url
        self._notice = notice
        

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password

    def getUrl(self):
        return self._url

    def setUrl(self, url):
        self._url = url

    def getNotice(self):
        return self._notice

    def setNotice(self, notice):
        self._notice = notice

