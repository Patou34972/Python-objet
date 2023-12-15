class Personne:
    def __init__(self, nom, prenom: int):
        self.nom = nom
        self.prenom = prenom

    def __lt__(self, autre):
        return self.prenom < autre.prenom
        #return self.nom < autre.nom


# Liste des villes
personnes = [
    Personne("ELIE DIT COSAQUE", "Patrice"),
    Personne("ELIE DIT COSAQUE", "Chrystelle"),
    Personne("GOJON-GERBELOT", "Melanie"),
    Personne("NIRDE", "Jean-Noêl"),
    Personne("BANCE", "Cedric"),

]

personnes_triees = sorted(personnes)
for personne in personnes_triees:
    print(f"{personne.nom}: {personne.prenom}")
