import random
import string


class Logic:

    allUsers = []
    alphabetLowercase = list(string.ascii_lowercase)
    alphabetUppercase = list(string.ascii_uppercase)
    numberList = list(map(str, range(10))) 
    symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '\\', '|', '~', '`']
    completeList = [alphabetLowercase,alphabetUppercase,numberList,symbolsList]

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

    def deleteUser(self,userToDelete):
            for user in self.allUsers:
                if user == userToDelete:
                    self.allUsers.remove(user)
    
    def updateUser(self, user):
        for i, u in enumerate(self.allUsers):
            if u.getUsername() == user.getUsername():
                self.allUsers[i] = user
                break


    
    def addEntry(self,Entry,loggedUser):
        loggedUser.myEntrys.append(Entry)

    def generatePassword(self,length,strongness):
        generatedPassword = ''
        while length > 0:
            randomList = random.randint(0, strongness - 1)
            choosenList = self.completeList[randomList]
            randomIndex = random.randint(0,len(choosenList)-1)
            generatedPassword = generatedPassword + choosenList[randomIndex]
            length -= 1
        return generatedPassword
    
    def checkIfSimmilarEntryExists(self,url,loggedUser):
        for entry in loggedUser.myEntrys:
            if entry.getUrl() == url:
                return entry
        return None
        
         

                


