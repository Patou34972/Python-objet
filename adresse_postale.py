class AdressePostale:
    def __init__(self, numero_rue: int, libelle_rue: str, code_postal: str, ville: str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville

adr1 = AdressePostale(1, "Allée Michel Piquemal", 34830, "JACOU")
adr2 = AdressePostale(2, "Michel Rotin", 75000, "PARIS")

print(adr1.numero_rue, adr1.libelle_rue, adr1.code_postal, adr1.ville)
print(adr2.numero_rue, adr2.libelle_rue, adr2.code_postal, adr2.ville)

