import os

#   os.walk in eine Funktion verpacken (mit variablem "path" und "endswith")
#   -> Datei speichern als Grundlage für weitere Projekte

while True:
    path = "../../Documents/00_Dokumente"
    filesearch = input("Which file are you searching?")
    for root, dirs, files in os.walk(path):
        for x in files:
            if x.endswith(filesearch):
                print(x)
    break        

#Input prüfen: Was passiert falls kein String || kein "." als führends Zeichen || etc. eingegeben wird?

# Python PATH - weiter verfolgen
# import win32com.client as win32
