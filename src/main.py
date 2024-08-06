from logic import Logic
from User import User
import os
class Main:

    
    def __init__(self):
        self.functions = Logic()
        self.loggedUser = User('','')
        self.start()

    def start(self):
        
        while True:
            os.system('cls') 
            print("Willkommen beim Passwortmanager! Bitte wählen eine der Optionen:")
            print("(1) Anmelden")
            print("(2) Neues Konto erstellen")
            print("(3) Beenden")
            choice = input("Gib zum auswählen der Option die Nummer ein: ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.createAccount()
            elif choice == '3':
                print("Passwortmanager wird beendet. Bis zum nächsten Mal!")
                break
            else:
                print("Ungültige Wahl, bitte versuchen Sie es erneut.")




    def login(self):

        while True:
            username = input("Benutzername eingeben (Enter drücken, um Anmeldung abzubrechen): ")
            if username == "":
                print("Anmeldung abgebrochen.")
                return  
            password = input("Passwort eingeben (Enter drücken, um Anmeldung abzubrechen): ")
            if password == "":
                print("Anmeldung abgebrochen.")
                return  
            loggedUser = self.functions.tryToLogin(username,password)
            if loggedUser == None:
                os.system('cls') 
                print("Anmeldung fehlgeschlagen. Benutzername oder Passwort falsch !")
            else:
                self.openMainPage()
        




    def createAccount(self):
        os.system('cls') 
        print("Neuen Account erstellen: ")
        while True:
            username = input("Wähle einen Benutzernamen: ")
            if self.functions.alreadyUsed(username):
                os.system('cls') 
                print("Nutzername ", username , " bereits vergeben !")
            else:
                break
        while True:
            password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: ")
            if self.functions.checkPasswordLength(password) == False:
                os.system('cls') 
                print("Das Passwort ist zu kurz ! Erneut probieren ")
            else:
                break
        newUser = User(username,password)
        self.functions.addNewUser(newUser)
        print("Du hast erfolgreich einen Account erstellt !")
        self.login()
            
        


    def openMainPage(self):
        os.system('cls') 
        print("Anmeldung erolgreich. Aktueller Nutzer: ",self.loggedUser.getUsername())
        print("Bitte wähle eine der Optionen: ")
        print("(1) Neuen Eintrag erstellen")
        print("(2) Eintrag anzeigen")
        print("(3) Eintrag bearbeiten")
        print("(4) Zugangsdaten ändern")
        print("(5) Abmelden")
        choice = input("Gib zum auswählen der Option die Nummer ein: ")


  
        
if __name__ == "__main__":
    Main()
