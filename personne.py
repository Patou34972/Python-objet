from adresse_postale import *

class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    # Ajoutez une méthode qui permet d’afficher (avec print) le nom et le prénom avec le nom en majuscules.
    def afficher_nom_prenom_majuscules(self):
        nom_majuscule = self.nom.upper()
        prenom_majuscule = self.prenom.upper()
        print("Nom en majuscule : ", nom_majuscule)
        print("Prenom en majuscule : ", prenom_majuscule)

    def set_nom(self, nom: str):
        self.nom = nom

    def set_prenom(self, prenom: str):
        self.prenom = prenom

    def set_adresse(self, adresse: AdressePostale):
        self.adresse = adresse
    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_adresse(self):
        return self.adresse

    def afficher_infos(self):

        print("Nom :", self.nom)
        print("Prénom :", self.prenom)
        print("Adresse :", self.adresse)


# Exemple d'utilisation
per1 = Personne("ELIE DIT COSAQUE", "Patrice", adr1)
per2 = Personne("ELIE DIT COSAQUE", "Chrystelle", adr2)

# Affichage des informations sur les personnes
print(per1.nom, per1.prenom, per1.adresse.numero_rue, per1.adresse.libelle_rue, per1.adresse.code_postal, per1.adresse.ville)
print(per2.nom, per2.prenom, per2.adresse.numero_rue, per2.adresse.libelle_rue, per2.adresse.code_postal, per2.adresse.ville)

# Appel de la méthode pour afficher le nom et prénom en majuscules
per1.afficher_nom_prenom_majuscules()
per2.afficher_nom_prenom_majuscules()

# Affichage des informations avant les modifications
print("Avant les modifications :")
per1.afficher_infos()

# Modification du nom
per1.set_nom("HENRY")
print(per1.get_nom())

# Modification du prénom
per1.set_prenom("Michel")
print(per1.get_prenom())

# Création d'une nouvelle adresse
nouvelle_adresse = AdressePostale(456, "Avenue des Champs-Élysées", "75008", "Paris")

# Modification de l'adresse
per1.set_adresse(nouvelle_adresse)
print(per1.get_adresse())

# Affichage des informations après les modifications
print("\nAprès les modifications :")
per1.afficher_infos()

