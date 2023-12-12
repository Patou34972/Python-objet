class ChaineUtils:
    @staticmethod
    def est_anagramme(chaine1: str, chaine2: str):
        liste_chaine1 = list(chaine1)
        liste_chaine2 = list(chaine2)

        liste_chaine1.sort()
        liste_chaine2.sort()

        return liste_chaine1 == liste_chaine2

    @staticmethod
    def comptage_chaine(chaine_principale, sous_chaine):
        # Utiliser la méthode count pour compter les occurrences de la sous-chaîne
        return chaine_principale.count(sous_chaine)

# Exemple d'utilisation
if __name__ == "__main__":
    chaine1 = "listen"
    chaine2 = "silent"
    est_anagramme_resultat = ChaineUtils.est_anagramme(chaine1, chaine2)

    chaine_principale = "abababab"
    sous_chaine = "ab"
    comptage_resultat = ChaineUtils.comptage_chaine(chaine_principale, sous_chaine)

    print(f"Est anagramme : {est_anagramme_resultat}")
    print(f"Comptage de la sous-chaîne : {comptage_resultat}")
