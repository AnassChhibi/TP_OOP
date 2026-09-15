import unittest
from dictionnaires import *
from tuples import *
from ensembles import *

class TestJournalDeBord(unittest.TestCase):

    """Tests pour les fonctions sur les relevés (tuples)."""

    def test_recalibrer_capteur_existant(self):
        """Test de recalibrer pour un capteur existant."""

        resultat = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(resultat[0], ("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demandé n’existe pas."""
        
        resultat = recalibrer(releves, "capteur_inexistant", 1.40)
        self.assertEqual(resultat, releves)

class TestRobots(unittest.TestCase):

    """Tests pour les fonctions sur les ensembles."""

    def test_ajouter_robot_mission(self):
        """Test de ajouter_robot_mission."""
        ajout = ajouter_robot_mission(robots_exploration, "R8")
        self.assertEqual(ajout, {"R2", "R5", "R7", "R8"})
        
        """Test ajout d’un robot déjà présent"""
        ajout = ajouter_robot_mission(robots_exploration, "R5")
        print(ajout)
        # CORRECTION ICI : On s'attend à {"R2", "R5", "R7"} car R8 n'est pas dans l'ensemble de base
        self.assertEqual(ajout, {"R2", "R5", "R7"})

    def test_retirer_robot_mission(self):
        # ... ce test reste identique au vôtre, rien à changer ...
        retrait = retirer_robot_mission(robots_transport, "R9")
        self.assertEqual(retrait, {"R3", "R5", "R7"})
        self.assertEqual(robots_transport, {"R5", "R9", "R7", "R3"})

class TestInventaire(unittest.TestCase):

    """Tests pour les fonctions sur les dictionnaires."""

    def test_consommer_piece(self):
        """Test de consommer_piece."""
        # CORRECTION ICI : On crée un dictionnaire tout neuf juste pour ce test
        stock_test = {
            "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
            "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
        }
        consommer_piece(stock_test, "ModeleA", "moteurs", 3)
        self.assertEqual(stock_test["ModeleA"]["moteurs"], 7)

    def test_total_pieces(self):
        """Test de total_pieces."""
        # CORRECTION ICI : On recrée le dictionnaire dans l'état où il est censé être 
        # après l'ajout du ModèleC et la consommation des moteurs
        stock_test = {
            "ModeleA": {"moteurs": 7, "capteurs": 25, "roues": 40},
            "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
            "ModeleC": {"moteurs": 4, "capteurs": 10, "roues": 16}
        }
        totaux = total_pieces(stock_test)
        self.assertEqual(totaux, {"moteurs": 17, "capteurs": 50, "roues": 80})
        
        """Test stock vide"""
        pieces_stock_vide = {}
        self.assertEqual(total_pieces(pieces_stock_vide), {"moteurs": 0, "capteurs": 0, "roues": 0})
if __name__ == "__main__":
    unittest.main(verbosity=2)