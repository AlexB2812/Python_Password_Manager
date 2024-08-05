# Python_Password_Manager
a console-based password manager


Technologie
Es muss ein Passwort Manager implementiert werden.
Das Programm muss in der Programmiersprache Python entwickelt werden.
Das Programm muss in Python Version 3.11.5 mit dem Betriebssystem Linux (Ubuntu 20.04 LTS)
lauffähig sein.
Das Programm muss eine grafische Oberfläche über die Kommandozeile bieten.
Folgende Standard Bibliotheken sind zulässig: datetime, time, os, sys, re, json, csv, pickle,
getpass, random, secrets, string, hashlib, requests, unittest, base64
Folgende Drittanbieter Bibliotheken sind zulässig: curses, cryptography
Die Verwendung weiterer Bibliotheken ist nur nach Absprache erlaubt


Funktionale Anforderungen

Passwortspeicherung:
Sichere und Verschlüsselte Speicherung von Benutzernamen, Passwörtern und
zugehörigen Website-URLs.
Verschlüsselung der gespeicherten Daten mit einem starken Algorithmus (z.B. AES-256).
Möglichkeit, zusätzliche Informationen zu speichern (z.B. Notizen, Kategorien).
Verschlüsselte Speicherung von Metadaten wie z.B. Erstelldatum und Uhrzeit.
Passwortverlauf: Speicherung von älteren Passwortversionen, um die Wiederverwendung
von Passwörtern zu verhindern und bei Bedarf auf ältere Passwörter zurückgreifen zu
können.

Passwortgenerierung:
Generierung sicherer, zufälliger Passwörter mit konfigurierbarer Länge und Zeichensatz
(Groß-/Kleinbuchstaben, Zahlen, Sonderzeichen).
Anpassung der Passwortstärke (z.B. Ausschluss bestimmter Zeichen, Erzwingen
bestimmter Muster).
Passwortabruf:
Suche und Anzeige gespeicherter Passwörter anhand von Website-URLs oder
Suchbegriffen.
Anzeige von Benutzernamen und zusätzlichen Informationen.
Passwortbearbeitung:
Änderung von Benutzernamen, Passwörtern und zusätzlichen Informationen.
Löschen von gespeicherten Passwörtern.
Master-Passwort:
Schutz der gespeicherten Daten durch ein Master-Passwort.
Sichere Speicherung des Master-Passworts (z.B. Hashing).



Benutzeroberfläche:
Intuitive Menüführung über die Konsole.
Klare Anweisungen und Fehlermeldungen.
Steuerung über Pfeiltasten oder alternative Eingabemethoden.
Nutzermanagement
Erstellung von mehreren Accounts mit jeweils eigenem Master-Passwort

Import/Export:
Export und Import der Passwörter in ein Text Format (z.B. CSV oder JSON).
Passwortprüfung:

Überprüfung der Stärke von Passwörtern anhand gängiger Kriterien (z.B. Länge,
Zeichensatz, Wiederverwendung).
Warnung vor schwachen Passwörtern.
Warnung bei gleichen Passwörtern.

Warnung bei von Datenlecks betroffenen Passwörtern:
Anbindung der Have I Been Pwned API
Dokumentation: https://haveibeenpwned.com/API/v3#PwnedPasswords
Überprüfung des Passwortes über folgenden request: GET
https://api.pwnedpasswords.com/range/{first 5 hash chars} (kein
API key nötig).
Korrektes Verhalten falls die API offline ist oder kein Internet zur Verfügung steht.

Nicht-funktionale Anforderungen
Sicherheit:
Schutz vor unbefugtem Zugriff auf die gespeicherten Daten.
Sichere Implementierung der Verschlüsselung und des Hashing.
Zuverlässigkeit:
Stabile Funktionalität ohne Abstürze oder Datenverlust.
Fehlertolerante Handhabung von ungültigen Eingaben oder unerwarteten Ereignissen.
Benutzerfreundlichkeit:
Einfache Bedienung auch für Benutzer ohne technische Vorkenntnisse.


Dynamische Code Analyse
Es müssen automatisierte Unittests entwickelt werden.
Es muss die Bibliothek unittest genutzt werden.
Pro Datei muss eine Testabdeckung von 75% erreicht werden (Prüfung über coverage).
Die Tests müssen logisch sinnvoll entwickelt sein.
Statische Code Analyse - Pylint
Es muss Pylint auf jede Python Datei ausgeführt werden.
Alle Pylint Warnungen müssen behoben werden.
Meldungen können durch eine gute Begründung unterdrückt werden.
Pylint muss über Konsole ausgeführt werden.
Keine Dokumentation in Tests nötig (In Test Dateien: #pylint: disable=C).
Es muss eine pylintrc Datei vorhanden sein


Type Checker - MyPy
Alle Python Dateien müssen von mypy überprüft werden.
Es müssen alle mypy Warnungen behoben werden.
Es muss folgende mypy.ini Datei genutzt werden
