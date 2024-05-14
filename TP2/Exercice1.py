import json
import csv

def lirejson(fichierjson):
    with open(fichierjson, 'r') as f:
        contenu = json.load(f)
        return contenu

def ecrirecsv(contenujson, fichiercsv):
    with open(fichiercsv, 'w') as csv:
        csvwriter = csv.writer(csv, delimiter="\n")
        csvwriter.writerow(["reel,imaginaire"])
