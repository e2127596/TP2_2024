import json
import csv

def lirejson(fichierjson):
    with open(fichierjson, 'r') as f:
        contenu = json.load(f)
        return contenu #Extraire le contenu du json pour la fonction qui suivra

def ecrirecsv(contenujson, fichiercsv):
    with open(fichiercsv, 'w', newline="") as f:
        csvwriter = csv.writer(f) #Aucun delimiter spécifié, "," par défaut
        csvwriter.writerow(["reel","imaginaire"])
        for tuple in contenujson:
            csvwriter.writerow(tuple) #chaque tuple du json constitue une ligne du csv

contenujson = lirejson("data.json")
print(contenujson)
ecrirecsv(contenujson, "data.csv")