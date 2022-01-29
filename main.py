from cmath import log
import os
from traceback import print_tb

#   os.walk in eine Funktion verpacken (mit variablem "path" und "endswith")
#   -> Datei speichern als Grundlage für weitere Projekte

# while True:
#     path = "../../Documents/00_Dokumente"
#     filesearch = input("Which file are you searching?")
#     for root, dirs, files in os.walk(path):
#         for x in files:
#             if x.endswith(filesearch):
#                 print(str(root)+x)
#     break        

#Input prüfen: Was passiert falls kein String || kein "." als führends Zeichen || etc. eingegeben wird?

# Lösung für PyLance-Problem (Module konnten nicht gefunden werden)
# -> in VSCode wurde der der falsche Interpreter ausgewählt ((Ctrl+Shift+P) -> Python Select Interpreter)
# reddit: https://www.reddit.com/r/vscode/comments/o67qm5/import_could_not_be_resolved_pylance/

import win32com.client as win32
# from win32com.client import combrowse
# combrowse.main()

from pywinauto import application
from pywinauto import keyboard
import time

file = "C:\Users\flo_s\Documents\00_Dokumente\99_Arbeit\92_Roth_Baumschule\00_Webseite\Logo\00_Illustrator\Styleguide_2.ai"

app = application.Application()
app.start("C:\Program Files\Adobe\Adobe Illustrator 2021\Support Files\Contents\Windows\Illustrator.exe")
time.sleep(1)
keyboard.send_keys('^o')
time.sleep(1)
keyboard.send_keys(file)
time.sleep(1)
keyboard.send_keys('~')




