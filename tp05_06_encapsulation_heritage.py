class Livre:
    def __init__(self, titre, auteur, achetable=False):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, nv_titre):
        self._titre = nv_titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, nv_auteur):
        self._auteur = nv_auteur

    @property
    def achetable(self):
        return self._achetable

    @achetable.setter
    def achetable(self, nv_achetable):
        self._achetable = nv_achetable

    def afficher_infos(self):
        print("Titre:" + self._titre + " - Auteur:" + self._auteur + " - Achetable:" + str(self._achetable))


class LivrePapier(Livre):
    def __init__(self, titre, auteur, etat, achetable=False):
        super().__init__(titre, auteur, achetable)
        self._etat = etat

    def afficher_infos(self):
        print(
            "Titre:" + self._titre + " - Auteur:" + self._auteur + " - Etat:" + self._etat + " - Achetable:" + str(
                self._achetable))


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, format, achetable=False):
        super().__init__(titre, auteur, achetable)
        self._format = format

    def afficher_infos(self):
        print("Titre:" + self._titre + " - Auteur:" + self._auteur + " - Format:" + self._format + " - Achetable:" + str(
            self._achetable))


l_p1 = LivrePapier("Histoire de la Martinique", "Arman Nicolas", "neuf", False)
l_p2 = LivrePapier("Yasuke", "Bille Serge", "bon etat", True)
l_n1 = LivreNumerique("Yasuke", "Bille Serge", "PDF", True)
l_n2 = LivreNumerique("Le loup des Cordeliers", "Henri Loevenbruck", "PDF", True)
liste_livres = [l_p1, l_p2, l_n1, l_n2]
for livre in liste_livres:
    livre.afficher_infos()


