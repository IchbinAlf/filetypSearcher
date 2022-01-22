import os

#   os.walk in eine Funktion verpacken (mit variablem "path" und "endswith")
#   -> Datei speichern als Grundlage für weitere Projekte

#   AI-SVG-Konverter mit filetypSearcher als Grundlage

path = "../../Documents/00_Dokumente"

for root, dirs, files in os.walk(path):
    for x in files:
        if x.endswith('.txt'):
            print(x)
        