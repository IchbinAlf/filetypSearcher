import os

path = "../../Documents/00_Dokumente"

for root, dirs, files in os.walk(path):
    for x in files:
        if x.endswith('.txt'):
            print(x)
        