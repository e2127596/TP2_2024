import json
import csv

def lirejson(fichierjson):
    with open(fichierjson, 'r') as f:
        contenu = json.load(f)
        return contenu

def ecrirecsv(contenujson, fichiercsv):
    with open(fichiercsv, 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["reel","imaginaire"])
        for tuple in contenujson:
            csvwriter.writerow(tuple)

contenujson = lirejson("data.json")
print(contenujson)
ecrirecsv(contenujson, "data.csv")