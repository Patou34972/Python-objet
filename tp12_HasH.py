class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"{self.nom} - {self.prenom}"

    def __repr__(self):
        return f"Personne(nom='{self.nom}, prenom='{self.prenom}')"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self.nom == other.nom and self.prenom == other.prenom

    def __hash__(self):
        return hash((self.nom, self.prenom))


per1 = Personne("ELIE DIT COSAQUE", "Patrice")
per2 = Personne("GOJON-GERBELOT", "Melanie")
per3 = Personne("BANCE", "Cedric")
per4 = Personne("NIRDE", "Jean-Noêl")

sets = {per1, per2, per3, per4}
print(sets)
