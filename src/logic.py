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
            if user.getUsername() == username:
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

    def addOldPassword(self,oldPassword,loggedUser):
        loggedUser.oldPasswords.append(oldPassword)
        self.updateUser(loggedUser)

    def isOldPassword(self,newPassword,loggedUser):
        return newPassword in loggedUser.oldPasswords

    
    def addEntry(self,Entry,loggedUser):
        loggedUser.myEntrys.append(Entry)

    def deleteEntry(self,entryToDelete,loggedUser):
        for entry in loggedUser.myEntrys:
            if entry == entryToDelete:
                loggedUser.myEntrys.remove(entry)

    def updateEntry(self,entry,loggedUser,oldUrl):
        for i, u in enumerate(loggedUser.myEntrys):
            if u.getUrl() == oldUrl:
                loggedUser.myEntrys[i] = entry
                break
        self.updateUser(loggedUser)

    

    def goThroughEntry(entry,searchedFor):
        splittedNotice = entry.getUrl().split()
        if(entry.getUrl()== searchedFor or entry.getPassword() == searchedFor or searchedFor in splittedNotice):
            return True
        else:
            return False
        
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
    
    def getSafetyLevel(self,password):
        ammountOfDifferentChars = self.getAmmountOfDifferentChars(password)
        combinationPoints = self.combinationPoints(password)
        length = len(password)
        safetyPoints = 2*length + 2*ammountOfDifferentChars + 4*combinationPoints
        ammountOfAllChars = len(self.alphabetLowercase) + len(self.alphabetUppercase) + len(self.numberList) + len(self.symbolsList)
        if length >= ammountOfAllChars:
            maxDifferentChars = ammountOfAllChars
        else:
            maxDifferentChars = length

        maxSafetyPoints = 2 * length + 2 * maxDifferentChars + 400
        part = safetyPoints/maxSafetyPoints
        percent = round(part * 100)
        return percent

    
    def getAmmountOfDifferentChars(self,password):
        uniqueChars = set(password)
        return len(uniqueChars)
    
    def combinationPoints(self,password):
        if self.containsLower(password) and not self.containsUpper(password) and not self.containsNumber(password) and not self.containsSymbol(password):
            return 10
        elif self.containsLower(password) and self.containsUpper(password) and not self.containsNumber(password) and not self.containsSymbol(password):
            return 30
        elif self.containsLower(password) and not self.containsUpper(password) and self.containsNumber(password) and not self.containsSymbol(password):
            return 20
        elif self.containsLower(password) and not self.containsUpper(password) and not self.containsNumber(password) and self.containsSymbol(password):
            return 40
        elif self.containsLower(password) and self.containsUpper(password) and self.containsNumber(password) and not self.containsSymbol(password):
            return 50
        elif self.containsLower(password) and not self.containsUpper(password) and  self.containsNumber(password) and self.containsSymbol(password):
            return 60
        elif self.containsLower(password) and self.containsUpper(password) and not self.containsNumber(password) and self.containsSymbol(password):
            return 70
        elif self.containsLower(password) and self.containsUpper(password) and self.containsNumber(password) and self.containsSymbol(password):
            return 100
        elif not self.containsLower(password) and not self.containsUpper(password) and self.containsNumber(password) and not self.containsSymbol(password):
            return 8
        elif not self.containsLower(password) and self.containsUpper(password) and self.containsNumber(password) and not self.containsSymbol(password):
            return 28
        elif not self.containsLower(password) and not self.containsUpper(password) and self.containsNumber(password) and self.containsSymbol(password):
            return 48
        elif not self.containsLower(password) and self.containsUpper(password) and not self.containsNumber(password) and not self.containsSymbol(password):
            return 12
        elif not self.containsLower(password) and self.containsUpper(password) and not self.containsNumber(password) and self.containsSymbol(password):
            return 32
        elif not self.containsLower(password) and not self.containsUpper(password) and not self.containsNumber(password) and self.containsSymbol(password):
            return 14
        else: 
            return 0

        
    
    def containsLower(self,password):
        return any(char in self.alphabetLowercase for char in password)
    
    def containsUpper(self,password):
        return any(char in self.alphabetUppercase for char in password)
    
    def containsNumber(self,password):
        return any(char in self.numberList for char in password)
    
    def containsSymbol(self,password):
        return any(char in self.symbolsList for char in password)
    
    

  
        
         

                


