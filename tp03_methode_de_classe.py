class Zoo:
    liste_des_animaux = []
    nombre_total = 0

    @classmethod
    def ajouter_animaux(cls, espece: str, nombre_animaux: int):
        animal_existe = False
        for animal in cls.liste_des_animaux:
            if animal["espece"] == espece:
                animal_existe = True
                animal['nombre'] += nombre_animaux
                break

        if not animal_existe:
            cls.liste_des_animaux.append({'espece': espece, 'nombre': nombre_animaux})
        cls.nombre_total += nombre_animaux

    @classmethod
    def afficher_animaux(cls):
        print("Animaux dans le Zoo :")
        for animal in cls.liste_des_animaux:
            print(f"{animal['espece']} : {animal['nombre']}")

        print(f"Nombre total d'animaux dans le Zoo : {cls.nombre_total}")


# Exemple d'utilisation
Zoo.ajouter_animaux("Lion", 3)
Zoo.ajouter_animaux("Tigre", 2)
Zoo.ajouter_animaux("Lion", 2)
Zoo.afficher_animaux()

