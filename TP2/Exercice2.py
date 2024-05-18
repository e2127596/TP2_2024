import csv
# Cette fonction permet de mettre les données de Pokémon du fichier csv dans un dictionnaire.
def charger_pokémons_csv(csv_file):
    pokemon_dict = {} #On initialise le dictionnaire.
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader: 
            name = row[0]
            stats = list(map(int, row[1:]))
            pokemon_dict[name] = stats #le nom du Pokemon devient une clé dans le dictionnaire et les stats sont associe a cette clé.
    return pokemon_dict
#permet d'afficher les resultats de la commande dans le terminal.
pkmn = charger_pokémons_csv('pokemon.csv')
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")