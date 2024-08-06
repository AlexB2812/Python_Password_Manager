class Logic:

    allUsers = []

    def tryToLogin(self,username,password):
        for user in self.allUsers:
            if user.getUsername() == username and user.getPassword() == password:
                return user
        return None  
    
    def alreadyUsed(self,username):
        for user in self.allUsers:
            if user.getUsername == username:
                return True
        return False
    
    def checkPasswordLength(self,password):
        length = len(password)
        if length >= 10:
            return True
        else:
            return False
        
    def addNewUser(self,newUser):
        self.allUsers.append(newUser)

    
    def addEntry(self,Entry,loggedUser):
        loggedUser.myEntrys.append(Entry)