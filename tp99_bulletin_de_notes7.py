from datetime import date


class Note:
    def __init__(self, valeur, date, categorie):
        self.valeur = valeur
        self.date = date
        self.categorie = categorie


class Discipline:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def calculer_moyenne(self):
        if not self.notes:
            return 0
        somme_notes = sum(note.valeur for note in self.notes)
        return somme_notes / len(self.notes)


class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Bulletin:
    def __init__(self, etudiant, disciplines):
        self.etudiant = etudiant
        self.disciplines = disciplines

    def ajouter_note(self, discipline, note):
        discipline.ajouter_note(note)

    def calculer_moyenne(self):
        moyennes = {}
        for discipline in self.disciplines:
            moyenne_discipline = discipline.calculer_moyenne()
            moyennes[discipline.nom] = moyenne_discipline
        return moyennes

    def afficher_moyenne(self):
        moyennes = self.calculer_moyenne()
        for discipline, moyenne in moyennes.items():
            print(f"Moyenne en {discipline}: {moyenne}")


# Exemple d'utilisation
etudiant1 = Etudiant("Dupont", "Jean")
maths = Discipline("Mathématiques")
physique = Discipline("Physique")
anglais = Discipline("Anglais")

bulletin_etudiant1 = Bulletin(etudiant1, [maths, physique, anglais])

note_math1 = Note(15, date(2023, 1, 1), "DS")
note_math2 = Note(18, date(2023, 1, 15), "Interro")
bulletin_etudiant1.ajouter_note(maths, note_math1)
bulletin_etudiant1.ajouter_note(maths, note_math2)

note_physique1 = Note(14, date(2023, 1, 5), "DS")
bulletin_etudiant1.ajouter_note(physique, note_physique1)

note_anglais1 = Note(16, date(2023, 1, 10), "DS")
bulletin_etudiant1.ajouter_note(anglais, note_anglais1)

bulletin_etudiant1.afficher_moyenne()
