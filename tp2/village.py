class Habitant:

    def __init__ (self, nom, age, adresse, animaux=None):
        self.__nom=nom
        self.__age=age
        self.__adresse=adresse
        self.__animaux=animaux
    @property
    def get_nom(self):
        return self.__nom
    
    @property
    def set_nom(self,nom):
        self.__nom=nom
    
    @property
    def get_age(self):
        return self.__age
    
    @property
    def set_age(self,age):
        self.__age=age
    
    @property
    def get_adresse(self):
        return self.__adresse
    
    @property
    def set_adresse(self,adresse):
        self.__adresse=adresse
    
    @property
    def get_animaux(self):
        return self.__animaux
    
    @property
    def set_animaux(self,animaux):
        self.__animaux=animaux


    def affichage_adresse(self):
        print("{nom} habite a {adresse}".format(nom=self.__nom,adresse=self.__adresse))

    def compte_animal(self, animal):
        if animal in self.__animaux :
            return self.__animaux[animal]
        else:
            return 0

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,valeur):
        if valeur > 130 or valeur < 0 :
            raise ValueError
        self.__age=valeur
    

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass


class Village :

    def __init__(self, nom):
        self.nom = nom
        self.habitants=[]

    def get_habitants(self):
        return self.habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        self.habitants.append(Habitant(nom,age,adresse,animaux))

    def ajouter_habitant_agregation(self, habitant):
        self.habitants.append(habitant)

    def afficher_habitants(self):
        print(self.habitants)

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()


"""
ajouter_habitant_composition a une relation forte car il gère la création et ajout de l'habitant tout seul (le village est propriétaire). 
ajouter_habitant_agregation, lui a une relation plus faible avec le village qui se contente d'utiliser un objet Habitant externe qui existe indépendamment et peut être partagé entre plusieurs villages.
"""