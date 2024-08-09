import time
from logic import Logic
from User import User
from entry import Entry
import os
import sys

class Main:
    def __init__(self):
        self.functions = Logic()
        self.loggedUser = None
        self.generatedEntry = Entry('', '', '')
        self.start()

    def start(self):
        while True:
            os.system('cls') 
            print("Willkommen beim Passwortmanager! Bitte wählen eine der Optionen:")
            print("(1) Anmelden")
            print("(2) Neues Konto erstellen")
            print("(3) Beenden")
            choice = input("Gib zum Auswählen der Option die Nummer ein:    ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.createAccount()
            elif choice == '3':
                print("Passwortmanager wird beendet. Bis zum nächsten Mal!")
                break
            else:
                print("Ungültige Wahl, bitte versuchen Sie es erneut.")
        sys.exit()
        

    def login(self):
        os.system('cls')
        while True:
            os.system('cls')
            username = input("Benutzername eingeben (Enter drücken, um Anmeldung abzubrechen):    ")
            if username == "":
                print("Anmeldung abgebrochen.")
                return  
            password = input("Passwort eingeben (Enter drücken, um Anmeldung abzubrechen):    ")
            if password == "":
                print("Anmeldung abgebrochen.")
                return

            loggedUser = self.functions.tryToLogin(username, password)
            if loggedUser is None:
                os.system('cls') 
                print("Anmeldung fehlgeschlagen. Benutzername oder Passwort falsch!")
                time.sleep(2)
            else:
                self.loggedUser = loggedUser
                self.openMainPage()
                break

    def createAccount(self):
        os.system('cls') 
        print("Neuen Account erstellen ")
        while True:
            username = input("Wähle einen Benutzernamen:    ")
            if self.functions.alreadyUsed(username):
                print("Nutzername", username, "bereits vergeben!")
                time.sleep(2)
                os.system('cls') 
            else:
                break
        while True:
            password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (g) eingeben, um Passwort generieren zu lassen!:    ")
            if password == "g":
                password = self.generatePassword()
                print("Dein generiertes Passwort:", password)
                choose = input("(1) Passwort nutzen (2) Vorgang wiederholen:    ")
                if choose == "1":
                    break
                elif choose == "2":
                    os.system('cls')     
            elif password != "g":
                if not self.functions.checkPasswordLength(password):
                    os.system('cls') 
                    print("Das Passwort ist zu kurz! Erneut probieren.") 
                    time.sleep(2)
                    os.system('cls') 
                else:
                    os.system('cls') 
                    passwordPoints = self.functions.getSafetyLevel(password)
                    print("Das Passwort ist zu : " + str(passwordPoints) + " Prozent sicher")
                    if passwordPoints >= 0 and passwordPoints <= 20:
                        print("Das entspricht einem sehr schwachen Passwort !")
                    elif passwordPoints > 20 and passwordPoints <= 40:
                        print("Das entspricht einem schwachen Passwort !")
                    elif passwordPoints > 40 and passwordPoints <= 60:
                        print("Das entspricht einem einigermaßen sicheren Passwort !")   
                    elif passwordPoints > 60 and passwordPoints <= 80:
                        print("Das entspricht einem starken Passwort !")
                    elif passwordPoints > 80 and passwordPoints <= 100:
                        print("Das entspricht einem sehr starkem Passwort !")
                    change = input("Drücke Enter wenn du dieses Passwort nutzen möchtest. Drücke (1) wenn du das Passwort nochmal ändern möchtest ! :    ")
                    if change == "1":
                        os.system('cls') 
                        continue
                    else:
                        break
        os.system('cls') 
        newUser = User(username, password)
        print("Nutzername:", username, "Passwort:", password)
        self.functions.addNewUser(newUser)
        print("Du hast erfolgreich einen Account erstellt!")
        time.sleep(2)
        self.login()

    def openMainPage(self):
        os.system('cls') 
        if self.loggedUser:
            print("Anmeldung erfolgreich. Aktueller Nutzer:", self.loggedUser.getUsername())
        else:
            print("Fehler: Kein Benutzer angemeldet.")
            return
        
        while True:
            print("Bitte wähle eine der Optionen: ")
            print("(1) Neuen Eintrag erstellen")
            print("(2) Eintrag anzeigen")
            print("(3) Eintrag bearbeiten")
            print("(4) Zugangsdaten ändern")
            print("(5) Abmelden")
            choice = input("Gib zum Auswählen der Option die Nummer ein:    ") 
            if choice == "1":
                self.createEntry()
            elif choice == "2":
                self.searchForEntry()
            elif choice == "3":
                self.listAllEntrys()
            elif choice == "4":
                self.openPersonalSite()
            elif choice == "5":
                self.loggedUser = None
                self.start()
                break
            else:
                print("Ungültige Wahl, bitte versuchen Sie es erneut.")

    def createEntry(self):
        os.system('cls')
        while True:
            url = input("Bitte gib eine URL an:    ")
            if url == '':
                print("Du musst eine URL oder einen anderen Verweis angeben!")
                continue  # Fordert den Benutzer auf, erneut einzugeben
            else:
                similarEntry = self.functions.checkIfSimmilarEntryExists(url, self.loggedUser)
                if similarEntry is None:
                    break
                else:
                    if similarEntry.getNotice() == "":
                        print("Es besteht bereits ein Eintrag, welcher die selbe URL verwendet. Dieser Eintrag hat keine Anmerkungen.")
                    else:
                        print("Es besteht bereits ein Eintrag, welcher die selbe URL verwendet. Dieser Eintrag hat folgende Anmerkungen:", similarEntry.getNotice())
                
                    choose = input("(1) um trotzdem fortzufahren. Der andere ältere Eintrag bleibt bestehen und wird nicht überschrieben! (2) um den Vorgang zu wiederholen:     ")
                    if choose == "2":
                        os.system('cls') 
                        continue  # Fordert den Benutzer auf, erneut einzugeben
                    if choose == "1":
                        os.system('cls') 
                        break

        while True:
            password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (g) eingeben, um Passwort generieren zu lassen!   ")
            if password == "g":
                password = self.generatePassword()
                print("Dein generiertes Passwort:", password)
                choose = input("(1) Passwort nutzen (2) Vorgang wiederholen:    ")
                if choose == "1":
                    os.system('cls') 
                    self.functions.addOldPassword(password,self.loggedUser)
                    break
                else:
                    os.system('cls') 
            elif not self.functions.checkPasswordLength(password):
                os.system('cls')
                print("Das Passwort ist zu kurz! Erneut probieren.")
            elif self.functions.isOldPassword(password,self.loggedUser):
                os.system('cls')
                print("Du hast dieses Passwort in der Vergangenheit bereits benutzt! Erneut probieren.")

            else:
                os.system('cls') 
                passwordPoints = self.functions.getSafetyLevel(password)
                print("Das Passwort ist zu : " + str(passwordPoints) + " Prozent sicher")
                if passwordPoints >= 0 and passwordPoints <= 20:
                    print("Das entspricht einem sehr schwachen Passwort !")
                elif passwordPoints > 20 and passwordPoints <= 40:
                    print("Das entspricht einem schwachen Passwort !")
                elif passwordPoints > 40 and passwordPoints <= 60:
                    print("Das entspricht einem einigermaßen sicheren Passwort !")   
                elif passwordPoints > 60 and passwordPoints <= 80:
                    print("Das entspricht einem starken Passwort !")
                elif passwordPoints > 80 and passwordPoints <= 100:
                    print("Das entspricht einem sehr starkem Passwort !")
                change = input("Drücke Enter wenn du dieses Passwort nutzen möchtest. Drücke (1) wenn du das Passwort nochmal ändern möchtest ! :    ")
                if change == "1":
                    os.system('cls') 
                    continue
                else:
                    self.functions.addOldPassword(password,self.loggedUser)
                    break

        notice = input("Gebe hier sonstige Notizen oder Anmerkungen ein oder drücke Enter um fortzufahren:    ")
        os.system('cls') 
        print(url)
        print(password)
        print(notice)
        choose = input("(1) um diesen Eintrag hinzuzufügen (2) um den Eintrag nochmal zu überarbeiten:    ")
        if choose == "1":
            self.generatedEntry = Entry(password, url, notice)
            self.functions.addEntry(self.generatedEntry, self.loggedUser)
            os.system('cls') 
            print("Der Eintrag wurde erfolgreich hinzugefügt!")
        
            while True:  # Eine Schleife, um weitere Einträge hinzuzufügen oder zur Hauptseite zurückzukehren
                choose = input("(1) Weitere Einträge hinzufügen (2) Zurück zur Startseite: ")
                if choose == "1":
                    self.createEntry()  # Rekursion für das Hinzufügen eines neuen Eintrags
                    return  # Rückkehr zur Methode, um sicherzustellen, dass sie richtig endet
                elif choose == "2":
                    self.openMainPage()  # Zurück zur Hauptseite
                    return  # Beenden Sie die Methode

        elif choose == "2":
            self.createEntry()  # Ermöglicht es dem Benutzer, den Eintrag zu überarbeiten


    def searchForEntry(self):
        searchFor = input("Gib einen Suchbegriff ein, um einen Eintrag zu finden oder drücke Enter um den Vorgang abzubrechen ! :    ")
        for e in enumerate(self.loggedUser.myEntrys):
            if(self.functions.goThroughEntry(e,searchFor)):
                print("Seitenname : " + e.getUrl())
                print("Passwort:    " + e.getPassword())
                print("Notizen:     " + e.getNotice())
                print("")
                print("")
                break

    def generatePassword(self):
        os.system('cls')
        while True:
            try:
                length = int(input("Wie lange soll das Passwort werden? Mindestens 10 Zeichen:    "))
                if length >= 10:
                    break
                else:
                    print("Das Passwort muss mindestens 10 Zeichen lang sein! Erneut probieren.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

        while True:
            try:
                strongness = int(input("Wie stark soll das Passwort sein? 1 Minimal, 4 Maximal:    "))
                if 1 <= strongness <= 4:
                    break
                else:
                    print("Die Stärke muss zwischen 1 und 4 liegen! Erneut probieren.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
    
        generatedPassword = self.functions.generatePassword(length, strongness)
        return generatedPassword

    def openPersonalSite(self):
        os.system('cls')
        while True:
            print("Hier kannst du deine Login-Daten ändern")
            print("(1) Benutzername ändern")
            print("(2) Masterpasswort ändern")
            print("(3) Account löschen")
            print("(4) Zurück zur Startseite")
            choice = input("Wähle eine der Optionen aus:    ")
            os.system('cls') 
        
            if choice == "1":
                print("Aktueller Nutzername:", self.loggedUser.getUsername())
                while True:
                    while True:
                        newUsername = input("Gib hier deinen neuen Benutzernamen ein:    ")
                        if self.functions.alreadyUsed(newUsername):
                            os.system('cls') 
                            print("Nutzername bereits vergeben. Anderen Nutzernamen verwenden: ")
                        else:
                            break
                    while True:
                        newUsername1 = input("Gib den neuen Benutzernamen nochmals ein:    ")
                        if newUsername == newUsername1:
                            choose = input(f"Möchtest du deinen Nutzernamen von {self.loggedUser.getUsername()} wirklich zu {newUsername} ändern? (1) Ja (2) Abbrechen und zurück zur Startseite:    ")
                            if choose == "1":
                                self.loggedUser.setUsername(newUsername)
                                print("Nutzername erfolgreich geändert!")
                                time.sleep(2)
                                os.system('cls') 
                                self.functions.updateUser(self.loggedUser)
                                self.openPersonalSite()
                                break
                                
                            elif choose == "2":
                                self.openPersonalSite()
                        else:
                            print("Nutzernmane stimmen nicht überein. Vorgang wiederholen !")
                            time.sleep(2)
                            os.system('cls') 
                            break
                            
                    

            elif choice == "2":
                while True:
                    tryPassword = input("Gib dein aktuelles Masterpasswort ein:    ")
                    if tryPassword == self.loggedUser.getPassword():
                        break
                    else:
                        print("Masterpasswort nicht korrekt. Vorgang wiederholen.")
                        time.sleep(2)
                        os.system('cls') 
                while True:
                    while True:
                        password = input("Wähle ein Passwort mit einer Mindestlänge von 10 Zeichen: / (generate) eingeben, um Passwort generieren zu lassen!:    ")
                        if password == "generate":
                            password = self.generatePassword()
                            print("Dein generiertes Passwort:", password)
                            choose = input("(1) Passwort nutzen (2) Vorgang wiederholen:    ")
                            if choose == "1":
                                self.functions.addOldPassword(password,self.loggedUser)
                                break
                        elif password != "generate":
                            if not self.functions.checkPasswordLength(password):
                                os.system('cls') 
                                print("Das Passwort ist zu kurz! Erneut probieren.")
                        elif self.functions.isOldPassword(password,self.loggedUser):
                            os.system('cls')
                            print("Du hast dieses Passwort in der Vergangenheit bereits benutzt! Erneut probieren.")
                        else:
                                os.system('cls') 
                                passwordPoints = self.functions.getSafetyLevel(password)
                                print("Das Passwort ist zu : " + str(passwordPoints) + " Prozent sicher")
                                if passwordPoints >= 0 and passwordPoints <= 20:
                                    print("Das entspricht einem sehr schwachen Passwort !")
                                elif passwordPoints > 20 and passwordPoints <= 40:
                                    print("Das entspricht einem schwachen Passwort !")
                                elif passwordPoints > 40 and passwordPoints <= 60:
                                    print("Das entspricht einem einigermaßen sicheren Passwort !")   
                                elif passwordPoints > 60 and passwordPoints <= 80:
                                    print("Das entspricht einem starken Passwort !")
                                elif passwordPoints > 80 and passwordPoints <= 100:
                                    print("Das entspricht einem sehr starkem Passwort !")
                                change = input("Drücke Enter wenn du dieses Passwort nutzen möchtest. Drücke (1) wenn du das Passwort nochmal ändern möchtest ! :    ")
                                if change == "1":
                                    os.system('cls') 
                                    continue
                                else:
                                    self.functions.addOldPassword(password,self.loggedUser)
                                    break

                    while True:
                        password1 = input("Wiederhole das Passwort nochmals:    ")
                        if password == password1:
                            choose = input("Passwort wirklich ändern? (1) Ja (2) Nein:    ")
                            if choose == "1":
                                self.loggedUser.setPassword(password)
                                print("Passwort erfolgreich geändert!")
                                self.functions.updateUser(self.loggedUser)
                                self.openPersonalSite()
                                break
                            elif choose == "2":
                                self.openPersonalSite()
                                break
                        else:
                            print("Passwörter stimmen nicht überein. Vorgang wiederholen ! ")
                            time.sleep(2)
                            os.system('cls') 
                            break

            elif choice == "3":
                choose = input("Account sicher löschen? Alle Daten gehen verloren! (1) Ja (2) Nein:    ")
                if choose == "1":
                    self.functions.deleteUser(self.loggedUser)
                    self.loggedUser = None
                    input("Account erfolgreich gelöscht. Beliebige Taste drücken, um zur Anmeldeseite zu gelangen:    ")
                    self.start()
                    break  # Zurück zur Startseite nach Löschen
                else:
                    self.openPersonalSite()
                    break

            elif choice == "4":
                self.openMainPage()
                break  # Zurück zur Startseite

    def listAllEntrys(self):
        os.system('cls') 
        count = 1
        for entry in self.loggedUser.myEntrys:
            print(count)
            print("Seitenname : " + entry.getUrl())
            print("Passwort:    " + entry.getPassword())
            print("Notizen:     " + entry.getNotice())
            print("")
            print("")
            count+=1
        print("")
        print("")
        while True:
            choose = input("Wähle einen Eintrag aus, indem du hier die Eintragsnummer eingibst oder drücke Enter um den Vorgang abzubrechen:    ")     
            if choose == "":
                os.system('cls')
                self.openMainPage()
                break
          
            choose = int(choose)  # Wandelt choose in eine Ganzzahl um
           
            if choose >= 1 and choose < count:
                choosenEntry = self.loggedUser.myEntrys[choose - 1]
                choice = input("Möchtest du diesen Eintrag löschen (1) oder überarbeiten (2) ?    ")
                if choice == "1":
                    os.system('cls')
                    self.functions.deleteEntry(choosenEntry,self.loggedUser)
                    os.system('cls') 
                    print("Eintrag : " + choosenEntry.getUrl() + " erfolgreich gelöscht !")
                    time.sleep(2)
                    os.system('cls')
                    self.listAllEntrys()
                if choice == "2":
                    os.system('cls')
                    oldUrl = entry.getUrl() 
                    print("Hier kannst du deine Einträge bearbeiten. Drücke Enter, wenn du etwas nicht verändern möchtest !")
                    changeUrl = input("Seitenname : " + oldUrl + " :    ")
                    if changeUrl != "":
                        entry.setUrl(changeUrl)
                    while True:
                        changePassword = input("Passwort:    " + entry.getPassword() + " (g) um Passwort zu generieren :    ")
                        if changePassword == "g":
                            changePassword = self.generatePassword()
                            print("Dein generiertes Passwort:", changePassword)
                            choose = input("(1) Passwort nutzen (2) Vorgang wiederholen:    ")
                            if choose == "1":
                                entry.setPassword(changePassword)
                                break
                        elif changePassword != "g" and changePassword != "":
                            if not self.functions.checkPasswordLength(changePassword):
                                os.system('cls') 
                                print("Das Passwort ist zu kurz! Erneut probieren.")
                            else:
                                entry.setPassword(changePassword)
                                break
                        
                    changeNotice = input("Notizen:     " + entry.getNotice() + " :    ")
                    if changeNotice == "":
                        emptyNotice = input("(1) wenn du die Notizen entfernen möchtest und Enter wenn du sie nicht bearbeiten möchtest :    ")
                        if emptyNotice == "1":
                            entry.setNotice(changeNotice)
                    else:
                        entry.setNotice(changeNotice)
                    os.system('cls')
                    self.functions.updateEntry(entry,self.loggedUser,oldUrl)
                    print("Du hast deinen Eintrag folgendermaßen erfolgreich geändert: ")
                    print("Seitenname : " + entry.getUrl())
                    print("Passwort:    " + entry.getPassword())
                    print("Notizen:     " + entry.getNotice())
                    time.sleep(2)
                    os.system('cls')
                    self.listAllEntrys()


                



if __name__ == "__main__":
    Main()