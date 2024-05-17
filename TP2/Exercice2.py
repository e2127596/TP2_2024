import csv

def charger_pokémons_csv(csv_file):
    pkmn_dict = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            stats = list(map(int, row[1:]))
            pkmn_dict[name] = stats
    return pkmn_dict

pkmn = charger_pokémons_csv('pokemon.csv')
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")