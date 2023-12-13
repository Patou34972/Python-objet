from abc import ABC, abstractmethod
from tp05_06_encapsulation_heritage import LivreNumerique, LivrePapier


class Sortie(ABC):
    def __init__(self, date, livre):
        self.date = date
        self.livre = livre

    @abstractmethod
    def get_montant(self):
        pass


class Emprunt(Sortie):
    def __init__(self, date, livre, duree):
        super().__init__(date, livre)
        self.duree = duree

    def get_montant(self):
        if isinstance(self.livre, LivrePapier):
            return self.duree * 0.5
        elif isinstance(self.livre, LivreNumerique):
            return self.duree * 0.25
        else:
            return 0


class Achat(Sortie):
    def __init__(self, date, livre, montant):
        super().__init__(date, livre)
        self.montant = montant

    def get_montant(self):
        return self.montant


# Création d'instances de livres
livre_papier = LivrePapier("Titre Livre Papier", "Auteur Papier", "Etat bon")
livre_numerique = LivreNumerique("Titre Livre Numérique", "Auteur Numérique", "Format PDF")

# Création d'instances de sorties (achats et emprunts)
emprunt = Emprunt("2023-01-01", livre_papier, 7)
achat = Achat("2023-02-01", livre_numerique, 15)

# Création d'une liste de sorties
liste_sorties = [emprunt, achat]


# Fonction pour calculer le montant global d'une liste de sorties
def montant_global(liste_sorties):
    total = 0
    for sortie in liste_sorties:
        total += sortie.get_montant()
    return total


# Appel de la fonction et affichage du montant global
montant_total = montant_global(liste_sorties)
print(f"Montant total : {montant_total}€")
