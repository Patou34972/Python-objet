from adresse_postale import AdressePostale


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale = None, ):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"Nom: {self.nom} - Prenom {self.prenom} - Adresse {self.adresse}"

    def __repr__(self):
        return f"Personne(nom='{self.nom}', prenom='{self.prenom}', adresse='{self.adresse}')"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self.nom == other.nom and self.prenom == other.prenom and self.adresse == other.adresse


per4 = Personne("ELIE DIT COSAQUE", "henry")
per5 = Personne("ELIE DIT COSAQUE", "henry")
print(per4 == per5)
