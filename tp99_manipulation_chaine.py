chaine = "durand;Marcel;2 523.5"

# Affichez le premier caractère de la chaine de caractères.
premier_caractere = chaine[6]
print("premier caractère: " + premier_caractere)

# Utilisez la fonction len() pour afficher la longueur de la chaine de caractères
longueur_chaine = len(chaine)
print(longueur_chaine)

# Utilisez la méthode index(c) pour afficher l’index du premier
# « ; » contenu dans la chaine de caractères.
index_point_virgule = chaine.index(";")
print("l'index du premier ';' est :", index_point_virgule)

# Utilisez l’opérateur [indexmin :indexmax] pour extraire une portion de chaine de caractères
# comprise entre un index de début (inclus) et un index de fin (exclu).
nom_de_famille = chaine[:index_point_virgule]
print("le nom de famille est :", nom_de_famille)

# Utilisez la méthode upper() pour afficher le nom de famille en majuscules.
majuscule = chaine.upper()
print(majuscule)

# Utilisez la méthode lower() pour afficher le nom de famille en minuscules.
minuscule = chaine.lower()
print(minuscule)

# Utilisez la méthode split(string) pour découper la chaine de caractères en morceaux.
morceaux = chaine.split()
print(morceaux)

# Créez une classe Salarie
class Salarie:
    def __init__(self, nom, prenom, salaire: int):
        self._nom = nom
        self._prenom = prenom
        self._salaire = salaire

# Chaine de caractères
chaine_nom = "durand"
chaine_prenom = "Marcel"
chaine_salaire = "2 523.5"

# Supprimer l'espace dans la chaine_salaire en utilisant la méthode replace
chaine_salaire = chaine_salaire.replace(" ", "")

# Convertir la chaine_salaire en float
salaire = float(chaine_salaire)

# Créer une instance de la classe Salarie
salarie_instance = Salarie(nom=chaine_nom, prenom=chaine_prenom, salaire=chaine_salaire)

# Affichage des attributs de l'instance créée
print("Nom :", salarie_instance._nom)
print("Prénom :", salarie_instance._prenom)
print("Salaire :", salarie_instance._salaire)
