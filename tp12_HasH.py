class Ville:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"{self.nom}"

    def __repr__(self):
        return f"Ville(nom='{self.nom}')"

    def __eq__(self, other):
        if not isinstance(other, Ville):
            return False
        return self.nom == other.nom

    def __hash__(self):
        return hash((self.nom))


vl1 = Ville("Montpellier")
vl2 = Ville("Bordeaux")
vl3 = Ville("Toulouse")
vl4 = Ville("Marseille")

sets = {vl1, vl2, vl3, vl4}
print(sets)
