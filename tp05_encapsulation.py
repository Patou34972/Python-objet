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


l1 = Livre("Histoir de la Martinique", "Arman Nocol", False)
l1.titre = "Histoire de la Martinique"
l1.auteur = "Armand Nicolas"
l1.achetable = True
print(f"Titre : {l1.titre}, Auteur: {l1.auteur}, Achetable : {l1.achetable}")
