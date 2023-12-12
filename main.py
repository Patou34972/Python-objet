class Utilisateur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
ut1 = Utilisateur("Michel", 55)
ut2 = Utilisateur("Patrice", 35)

print(ut1.nom, ut1.age)
print(ut2.nom, ut2.age)

