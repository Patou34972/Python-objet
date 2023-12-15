class PersonneException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PersonneService:
    def inserDonnees(self, nom, prenom, adresse):
        try:
            if not nom:
                raise PersonneException("Le nom doit être renseigné")
            if len(nom) < 2:
                raise PersonneException("le nom doit avoir au moins 2 caractères")
            if not prenom:
                raise PersonneException(" le prenom doit être renseigné")
            if len(prenom) < 2:
                raise PersonneException("Le prenom doit avoir au moins 2 caractères")
            if not adresse:
                raise PersonneException("L'adresse doit être renseigné")

        except PersonneException as e:
            print(f"Erreur de validation : {str(e)}")
        else:
            print("Validation réussie.")
        finally:
            print("Fin de programme")


service = PersonneService()

service.inserDonnees("", "Patrice", "1 Allée Michel Piquemal, 34830 JACOU")
service.inserDonnees("GOJON-GERBELOT", "M", "25 Rue Moulin à vent, 73000 GERBAIX")
service.inserDonnees("BANCE", "", "Lieut dit Michel Gros, 97200 FORT DE FRANCE")
service.inserDonnees("NIRDE", "Jean-Noêl", "")

