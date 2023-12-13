from adresse_postale import *


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"Nom: {self.nom} - Prenom {self.prenom} - Adresse {self.adresse}"

    def __repr__(self):
        return f"Personne(nom='{self.nom}', prenom='{self.prenom}', adresse='{self.adresse}')"

liste = [Personne("HENRY", "Fernand", adr1)]
per3 = Personne("Michel", "henry", adr1)
print(liste)
print(per3)
