class Ville:
    def __init__(self, nom, population: int):
        self.nom = nom
        self.population = population

    def __lt__(self, autre):
        # return self.population < autre.population
        return self.nom < autre.nom


# Liste des villes
villes = [
    Ville("Nice", 343000),
    Ville("Carcassonne", 47800),
    Ville("Narbonne", 53400),
    Ville("Lyon", 484000),
    Ville("Foix", 9700),
    Ville("Pau", 77200),
    Ville("Marseille", 850700),
    Ville("Tarbes", 40600)
]

villes_triees = sorted(villes)
for ville in villes_triees:
    print(f"{ville.nom}: {ville.population}")
