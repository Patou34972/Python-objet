class Animal:
    def __init__(self, nom, categorie, comportement):
        self.nom = nom
        self.categorie = categorie
        self.comportement = comportement


class Zoo:
    def __init__(self, nom="Zoo"):
        self.nom = nom
        self.zones = []

    def ajouter_animal(self, animal):
        if animal["carnivore"] and animal["mammifere"]:
            self.placer_animal(ZoneCarnivore, animal)
        elif not animal["carnivore"] and animal["mammifere"]:
            self.placer_animal(SavaneAfricaine, animal)
        elif animal["poisson"]:
            self.placer_animal(Aquarium, animal)
        elif animal["reptile"]:
            self.placer_animal(FermeAuxReptiles, animal)
        elif animal["oiseau"]:
            self.placer_animal(VolierePython, animal)

    def placer_animal(self, zone_class, animal):
        zone = None
        for z in self.zones:
            if isinstance(z, zone_class):
                zone = z
                break
        if not zone:
            zone = zone_class([])
            self.zones.append(zone)
        zone.animaux.append(animal)

    def get_quantite_nourriture(self):
        total_nourriture = 0
        for zone in self.zones:
            total_nourriture += zone.get_quantite_nourriture()
        return total_nourriture

    def afficher_infos(self):
        for zone in self.zones:
            zone.afficher_info()


class Zone:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []

    def afficher_info(self):
        print(f"Zone : {self.nom}")
        print("Animaux :")
        for animal in self.animaux:
            print(f"- {animal}")
        print("\n")

    def get_quantite_nourriture(self):
        pass


class SavaneAfricaine(Zone):
    def __init__(self, animaux):
        super().__init__("Savane Africaine")
        self.animaux = animaux

    def get_quantite_nourriture(self):
        return len(self.animaux) * 100


class FermeAuxReptiles(Zone):
    def __init__(self, animaux):
        super().__init__("Ferme aux reptiles")
        self.animaux = animaux

    def get_quantite_nourriture(self):
        return len(self.animaux) * 0.1


class Aquarium(Zone):
    def __init__(self, animaux):
        super().__init__("Aquarium")
        self.animaux = animaux

    def get_quantite_nourriture(self):
        return len(self.animaux) * 1


class ZoneCarnivore(Zone):
    def __init__(self, animaux):
        super().__init__("Zone Carnivore")
        self.animaux = animaux

    def get_quantite_nourriture(self):
        return len(self.animaux) * 10


class VolierePython(Zone):
    def __init__(self, animaux):
        super().__init__("Volière Python")
        self.animaux = animaux

    def get_quantite_nourriture(self):
        return len(self.animaux) * 0.25

zoo = Zoo()

zoo.ajouter_animal({"nom": "Lion", "carnivore": True, "mammifere": True, "poisson": False, "reptile": False, "oiseau": False})
zoo.ajouter_animal({"nom": "Girafe", "carnivore": False, "mammifere": True, "poisson": False, "reptile": False, "oiseau": False})
zoo.ajouter_animal({"nom": "Requin", "carnivore": True, "mammifere": False, "poisson": True, "reptile": False, "oiseau": False})
zoo.ajouter_animal({"nom": "Serpent", "carnivore": True, "mammifere": False, "poisson": False, "reptile": True, "oiseau": False})
zoo.ajouter_animal({"nom": "Perroquet", "carnivore": False, "mammifere": False, "poisson": False, "reptile": False, "oiseau": True})

zoo.afficher_infos()

quantite_nourriture = zoo.get_quantite_nourriture()
print(f"Besoins en nourriture du zoo : {quantite_nourriture} kg")
