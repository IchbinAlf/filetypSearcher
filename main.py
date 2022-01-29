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

# Lösung für PyLance-Problem (Module konnten nicht gefunden werden)
# -> in VSCode wurde der der falsche Interpreter ausgewählt ((Ctrl+Shift+P) -> Python Select Interpreter)
# reddit: https://www.reddit.com/r/vscode/comments/o67qm5/import_could_not_be_resolved_pylance/

import win32com.client as win32
