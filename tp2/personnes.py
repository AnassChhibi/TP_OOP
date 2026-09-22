from abc import ABC
from multipledispatch import dispatch

class Habitant(ABC):

    def __init__ (self, nom, age, adresse, animaux=None):
        self.nom=nom
        self.age=age
        self.adresse=adresse
        self.animaux=animaux

    def __str__(self):
        return "{} {}, {} ans, habite a {}".format(self.prenom,self.nom,self.age,self.adresse)

def affichage(habitant):

    print(str(habitant))

class Adulte(Habitant):
    def __init__(self,nom,prenom,age,adresse):
        super().__init__(nom,age,adresse)
        self.prenom=prenom

    def calcul_nombre_annee_avant_retraite(self):
        if self.age < 18:
            raise ValueError
        elif self.age >= 62:
            return "Deja a la retraite"
        else:
            return 62-self.age

class Enfant(Habitant):
    @dispatch(str,str,int,str)
    def __init__(self, nom,prenom,age,adresse):
        super().__init__(nom, age, adresse)
        self.prenom=prenom

    @dispatch(str,int,str)
    def __init__(self, nom,age,adresse):
        super().__init__(nom, age, adresse)
        if age>=18:
            raise ValueError

    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= 18:
            raise ValueError
        else:   
            return "Erreur: un enfant ne peut pas calculer sa retraite"

# Adulte : leve une ValueError si age < 18
# calcul_nombre_annee_avant_retraite() renvoie :
# - "Deja a la retraite" si age >= 62
# - 62 - age sinon
# Enfant : leve une ValueError si age >= 18
# calcul_nombre_annee_avant_retraite() renvoie toujours :
# - "Erreur: un enfant ne peut pas calculer sa retraite"

if __name__ == "__main__":
  adulte = Adulte("Dupont", "Marie", 35, "Rue A")
  enfant = Enfant("Martin", "Lucas", 12, "Rue B")
  assert isinstance(adulte, Habitant)
  assert adulte.calcul_nombre_annee_avant_retraite() == 27
  assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

  try:
    Enfant("Oups", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
  except ValueError:
    pass

  adulte = Adulte("Dupont", "Marie", 35, "123 Rue de la Paix")
  enfant = Enfant("Mohamed", "ALGAZAR", 9, "123 VIVA L'ALGERIE")
  affichage(adulte)
  affichage(enfant)

"""
Rendre la méthode abstraite force toute nouvelle classe fille à l'implémenter explicitement sous peine de lever 
une erreur dès l'instanciation, ce qui garantit qu'aucun objet Habitant ne pourra manquer de cette méthode lors
 des futurs appels polymorphes
"""