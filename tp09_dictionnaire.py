dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}

# Mettre en place une boucle pour afficher l'ensemble des clés contenues dans le dictionnaire
for cle in dicoVilles.keys():
    print(cle)

# Mettre en place une boucle pour afficher l'ensemble des valeurs contenues dans le dictionnaire

for valeur in dicoVilles.values():
    print(valeur)

# Afficher la taille du dictionnaire
taille_dictionnaire = len(dicoVilles)

print(taille_dictionnaire)


# Mettez en place une fonction qui prend en paramètre une liste de clés et retourne un dictionnaire
def longueur_des_cles(liste_cles):
    resultat = {}
    for cle in liste_cles:
        resultat[cle] = len(cle)
    return resultat


liste_cles1 = ["Coucou", "Hi"]
resultat1 = longueur_des_cles(liste_cles1)
print(resultat1)


# Mettez en place une fonction qui prend en paramètre une liste de clés et retourne un dictionnaire
# dans lequel la valeur associée à chaque clé correspond au nombre de d’occurrences de la clé dans la liste.

def occurrences_des_cles(liste_cles):
    resultat = {}
    for cle in liste_cles:
        if cle in resultat:
            resultat[cle] += 1
        else:
            resultat[cle] = 1
    return resultat


liste_cles2 = ["Ananas", "Banane", "Orange", "Ananas", "Banane"]
resultat2 = occurrences_des_cles(liste_cles2)
print(resultat2)


# Créez une classe Salarie avec 3 attributs
class Salarie:
    def __init__(self, nom, matricule, service):
        self._nom = nom
        self._matricule = matricule
        self._service = service

# Créez une liste de Salariés contenant les salariés suivants :

liste_salaries = [
    Salarie("Antoine Dupont", 127, "DSI/JAVA"),
    Salarie("Berthe Casa", 238, "DSI/PHP"),
    Salarie("Fatima Ouassa", 478, "DSI/JAVA"),
    Salarie("Cassian Andor", 156, "DSI/PYTHON"),
    Salarie("Lee Wu", 559, "DSI/PHP"),
    Salarie("Hassan Missen", "096", "DSI/PYTHON"),
    Salarie("Aurélien PIC", 889, "DSI/JAVA")
]

# Créez un dictionnaire qui contient le comptage du nombre de salariés par service.
comptage_par_service = {}

for salarie in liste_salaries:
    service = salarie._service
    if service in comptage_par_service:
        comptage_par_service[service] += 1
    else:
        comptage_par_service[service] = 1


print("Comptage du nombre de salariés par service :")
for service, nombre in comptage_par_service.items():
    print(f"{service}: {nombre} salarié(s)")
