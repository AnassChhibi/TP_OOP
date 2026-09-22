import unittest

# Importation des classes depuis les modules précédents
from village import Habitant, Village
from personnes import Adulte, Enfant

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l'encapsulation."""
    
    def setUp(self):
        """Initialisation d'un habitant pour les tests."""
        self.habitant = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

    def test_compte_animal_usuel(self):
        """Cas usuel : vérifie le décompte d'un animal possédé."""
        self.assertEqual(self.habitant.compte_animal("vaches"), 3)

    def test_compte_animal_invalide(self):
        """Cas limite : vérifie le décompte d'un animal non possédé (doit retourner 0)."""
        self.assertEqual(self.habitant.compte_animal("moutons"), 0)

    def test_age_setter_valide(self):
        """Cas usuel : modification de l'âge avec une valeur valide."""
        self.habitant.age = 26
        self.assertEqual(self.habitant.age, 26)

    def test_age_setter_invalide(self):
        """Cas limite : âge négatif (doit lever une ValueError)."""
        with self.assertRaises(ValueError):
            self.habitant.age = -5


class TestVillage(unittest.TestCase):
    """Tests pour la classe Village (composition et agrégation)."""
    
    def setUp(self):
        """Initialisation de villages pour les tests."""
        self.village1 = Village("PyTown")
        self.village2 = Village("VillageVoisin")

    def test_ajouter_habitant_composition(self):
        """Cas usuel : ajout d'un habitant par composition (le village le crée)."""
        self.village1.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
        habitants = self.village1.get_habitants()
        
        self.assertEqual(len(habitants), 1)
        # On utilise le getter car les attributs sont privés dans village.py
        self.assertEqual(habitants[0].get_nom(), "Aldric")

    def test_ajouter_habitant_agregation(self):
        """Cas limite : un même habitant ajouté par agrégation à deux villages différents."""
        elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
        
        self.village1.ajouter_habitant_agregation(elise)
        self.village2.ajouter_habitant_agregation(elise)
        
        # Vérifie qu'elle est bien présente dans les deux listes
        self.assertIn(elise, self.village1.get_habitants())
        self.assertIn(elise, self.village2.get_habitants())
        
        # Vérifie qu'il s'agit strictement de la même instance en mémoire (partagée)
        habitant_v1 = self.village1.get_habitants()[0]
        habitant_v2 = self.village2.get_habitants()[0]
        self.assertIs(habitant_v1, habitant_v2)


class TestHeritage(unittest.TestCase):
    """Tests pour l'héritage (Adulte et Enfant) et le polymorphisme sur la retraite."""
    
    def test_calcul_retraite_adulte(self):
        """Cas usuel : calcul des années avant la retraite pour un adulte."""
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)
        
        adulte_retraite = Adulte("Martin", "Paul", 65, "Rue B")
        self.assertEqual(adulte_retraite.calcul_nombre_annee_avant_retraite(), "Deja a la retraite")

    def test_calcul_retraite_enfant(self):
        """Cas usuel : tentative de calcul de retraite pour un enfant."""
        enfant = Enfant("Martin", "Lucas", 12, "Rue C")
        self.assertEqual(enfant.calcul_nombre_annee_avant_retraite(), "Erreur: un enfant ne peut pas calculer sa retraite")

    def test_creation_enfant_invalide(self):
        """Cas limite : création d'un enfant de 20 ans (doit lever une ValueError)."""
        with self.assertRaises(ValueError):
            # On utilise la signature sans prénom car c'est celle qui lève proprement 
            # la ValueError dans la surcharge implémentée de personnes.py
            Enfant("Oups", 20, "Rue D")


if __name__ == '__main__':
    unittest.main(verbosity=2)