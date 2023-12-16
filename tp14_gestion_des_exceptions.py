from tp11_redefinition_eq import *
from tp11_redefinition_eq import AdressePostale


class PersonneException(Exception):
    pass


class PersonneService:

    def valider(self,personne: Personne):

            if not personne.nom:
                raise PersonneException("Le nom doit être renseigné")
            if len(personne.nom) < 2:
                raise PersonneException("le nom doit avoir au moins 2 caractères")
            if not personne.prenom:
                raise PersonneException(" le prenom doit être renseigné")
            if len(personne.prenom) < 2:
                raise PersonneException("Le prenom doit avoir au moins 2 caractères")
            if not personne.adresse:
                raise PersonneException("L'adresse doit être renseigné")




# Création d'instances de Personne avec erreurs et sans erreurs
ad1 = AdressePostale(10, "rue du pont", "34500", "Ganges")
p1 = Personne("", "Patrice", ad1)
p2 = Personne("GOJON-GERBELOT", "M", ad1)
p3 = Personne("BANCE", "", ad1)
p4 = Personne("NIRDE", "Jean-Noel", "")

lpersonnes = [p1, p2, p3, p4]

for p in lpersonnes:
    try:
        PersonneService().valider(p)
    except PersonneException as e:
        print(f"Erreur de validation : {e}")
    else:
        print(f"Validation ok : {p}")

