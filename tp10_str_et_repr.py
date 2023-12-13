from adresse_postale import AdressePostale


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale = None,):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"Nom: {self.nom} - Prenom {self.prenom} - Adresse {self.adresse}"

    def __repr__(self):
        return f"Personne(nom='{self.nom}', prenom='{self.prenom}', adresse='{self.adresse}')"

liste = [Personne("HENRY", "Fernand")]
per3 = Personne("Michel", "henry")
print(liste)
print(per3)
