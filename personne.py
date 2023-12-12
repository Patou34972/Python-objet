from adresse_postale import *


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
per1 = Personne("ELIE DIT COSAQUE", "Patrice", adr1)
per2 = Personne("ELIE DIT COSAQUE", "Chrystelle", adr2)
print(per1.nom, per1.prenom, per1.adresse.numero_rue, per1.adresse.libelle_rue, per1.adresse.code_postal, per1.adresse.ville)
print(per2.nom, per2.prenom, per2.adresse.numero_rue, per2.adresse.libelle_rue, per2.adresse.code_postal, per2.adresse.ville)
