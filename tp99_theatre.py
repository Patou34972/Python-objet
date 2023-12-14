class Theatre:
    def __init__(self, nom, capacite_max, total_clients=0, totale_recette=0):
        self._nom = nom
        self._capacite_max = capacite_max
        self._total_clients = total_clients
        self._totale_recette = totale_recette

# Méthode inscrire
    def inscrire(self, nombre_clients, prix_place):
        if self._total_clients + nombre_clients <= self._capacite_max:
            self._total_clients += nombre_clients
            recette = nombre_clients * prix_place
            self._totale_recette += recette
            print(f"Inscription réussie pour {nombre_clients} clients. Recette ajoutée : {recette} €")
        else:
            print(f"Capacité maximale atteinte. Impossible d'inscrire {nombre_clients} clients.")

# Création d'une instance de Theatre
theatre_example = Theatre(nom="Mon Théâtre", capacite_max=50)

# Appel de la méthode inscrire plusieurs fois
theatre_example.inscrire(30, 20)
theatre_example.inscrire(25, 20)

# Affichage du total de clients inscrits
print(f"Total de clients inscrits : {theatre_example._total_clients}")

# Affichage de la recette totale de l'établissement
print(f"Recette totale : {theatre_example._totale_recette} €")
