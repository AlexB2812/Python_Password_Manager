from logic import Logic
from User import User
from entry import Entry
import os
class Main:

    
    def __init__(self):
        self.functions = Logic()
        self.loggedUser = User('','')
        self.generatedEntry = Entry('','','')
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
            password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (generate) eingeben, um Passwort generieren zu lassen !")
            if password == "generate":
                password = self.generatePassword()
                print("Dein generiertes Passwort: ", password)
                choose = input("(1) Passwort nutzen (2) Vorgang wiederholen")
                if choose == "1":
                    break
            elif password != "generate":
                if self.functions.checkPasswordLength(password) == False:
                    os.system('cls') 
                    print("Das Passwort ist zu kurz ! Erneut probieren ")
                else:
                    break
        newUser = User(username,password)
        print("Nutzername: ",username, " Passwort: ", password)
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
        if choice == "1":
            self.createEntry()
        if choice == "4":
            self.openPersonalSite()
            
        
            

    


    def createEntry(self):
        while True:
            url = input("Bitte gib eine URL an: ")
            if url == '':
                print("Du musst eine URL oder einen anderen Verweis angeben !")
            else:
                simmilarEntry = self.functions.checkIfSimmilarEntryExists(url,self.loggedUser)
                if simmilarEntry == None:
                    break
                else:
                    if simmilarEntry.getNotice() == "":
                        print("Es besteht bereits ein Eintrag, welcher die selbe URL verwendet. Dieser Eintrag hat keine Anmerkungen")
                    else:
                        print("Es besteht bereits ein Eintrag, welcher die selbe URL verwendet. Dieser Eintrag hat folgende Anmerkungen: ",simmilarEntry.getNotice())
                    choose = input("(1) um trotzdem fortzufahren. Der andere ältere Eintrag bleibt bestehen und wird nicht überschrieben ! (2) um den Vorgang zu wiederholen: ")
                    if choose == 2:
                        break
        while True:
            password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (generate) eingeben, um Passwort generieren zu lassen !")
            if password == "generate":
                password = self.generatePassword()
                print("Dein generiertes Passwort: ", password)
                choose = input("(1) Passwort nutzen (2) Vorgang wiederholen")
                if choose == "1":
                    break
            elif password != "generate":
                if self.functions.checkPasswordLength(password) == False:
                    os.system('cls') 
                    print("Das Passwort ist zu kurz ! Erneut probieren ")
                else:
                    break
        notice = input("Gebe hier sonstige Notizen oder Anmkerungen ein oder drücke Enter um fortzufahren: ")
        choose = input("(1) um diesen Eintrag hinzuzufügen (2) um den Eintrag nochmal zu überarbeiten: ")
        if choose == "1":
            self.generatedEntry = Entry(password,url,notice)
            self.functions.addEntry(self.generatedEntry,self.loggedUser)
            print("Der Eintrag wurde erfolgreich hinzugefügt !")
            choose = input("(1) Weitere Einträge hinzufügen (2) Zurück zur Startseite: ")
            if choose == "1":
                self.createEntry()
            elif choose == "2":
                self.openMainPage()
        elif choose == "2":
            self.createEntry()
        


        


    def generatePassword(self):
        while True:
            try:
                length = int(input("Wie lange soll das Passwort werden? Mindestens 10 Zeichen: "))
                if length >= 10:
                    break
                else:
                    print("Das Passwort muss mindestens 10 Zeichen lang sein! Erneut probieren.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

        while True:
            try:
                strongness = int(input("Wie stark soll das Passwort sein? 1 Minimal, 4 Maximal: "))
                if 1 <= strongness <= 4:
                    break
                else:
                    print("Die Stärke muss zwischen 1 und 4 liegen! Erneut probieren.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
    
        generatedPassword = self.functions.generatePassword(length, strongness)
        return generatedPassword

        
    def openPersonalSite(self):
        while True:
            print("Hier kannst du deine Login Daten ändern")
            print("(1) Benutzername ändern")
            print("(2) Masterpasswort ändern")
            print("(3) Account löschen")
            print("(4) Zurück Zur Startseite")
            choosee = input("Wähle eine der Optionen aus: ")
        
            if choosee == "1":
                print("Aktueller Nutzername: ", self.loggedUser.getUsername())
                while True:
                    newUsername = input("Gib hier deinen neuen Usernamen ein: ")
                    if self.functions.alreadyUsed(newUsername):
                        print("Nutzername bereits vergeben. Anderen Nutzernamen verwenden: ")
                    else:
                        break
                newUsername1 = input("Gib den neuen Benutzernamen erneut ein: ")
                if newUsername == newUsername1:
                    choose = input("Möchtest du deinen Nutzernamen von " + self.loggedUser.getUsername() + " wirklich zu " + newUsername + " ändern? (1) Ja (2) Nein: ")
                    if choose == "1":
                        self.loggedUser.setUsername(newUsername)
                        print("Nutzername erfolgreich geändert!")
                    # Speichern des geänderten Nutzernamens im Logic-Objekt
                        self.functions.updateUser(self.loggedUser)
                        continue
                    elif choose == "2":
                        continue

            elif choosee == "2":
                while True:
                    tryPassword = input("Gib dein aktuelles Masterpasswort ein: ")
                    if tryPassword == self.loggedUser.getPassword():
                        break
                    else:
                        print("Masterpasswort nicht korrekt. Vorgang wiederholen")
                while True:
                    password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (generate) eingeben, um Passwort generieren zu lassen !")
                    if password == "generate":
                        password = self.generatePassword()
                        print("Dein generiertes Passwort: ", password)
                        choose = input("(1) Passwort nutzen (2) Vorgang wiederholen")
                        if choose == "1":
                            break
                    elif password != "generate":
                        if not self.functions.checkPasswordLength(password):
                            os.system('cls') 
                            print("Das Passwort ist zu kurz ! Erneut probieren ")
                        else:
                            break
                while True:
                    password1 = input("Wiederhole das Passwort nochmals: ")
                    if password == password1:
                        choose = input("Passwort wirklich ändern? (1) Ja (2) Nein: ")
                        if choose == "1":
                            self.loggedUser.setPassword(password)
                            print("Passwort erfolgreich geändert!")
                        # Speichern des geänderten Passworts im Logic-Objekt
                            self.functions.updateUser(self.loggedUser)
                            continue
                        elif choose == "2":
                            continue

            elif choosee == "3":
                choose = input("Account sicher löschen? Alle Daten gehen verloren! (1) Ja (2) Nein: ")
                if choose == "1":
                    self.functions.deleteUser(self.loggedUser)
                    self.loggedUser = None
                    input("Account erfolgreich gelöscht. Beliebige Taste drücken, um zur Anmeldeseite zu gelangen: ")
                    self.start()
                    break
                elif choose == "2":
                    continue

            elif choosee == "4":
                self.openMainPage()
                break




            
                

                               


  
        
if __name__ == "__main__":
    Main()
