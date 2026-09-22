"""Tests unitaires pour le TP2."""

import io
import sys
import unittest
from personnes import Adulte, Enfant, Habitant, affichage


class TestPolymorphisme(unittest.TestCase):
  """Tests pour l'Exercice 8 : Polymorphisme et méthode __str__."""

  def setUp(self):
    self.adulte = Adulte("Dupont", "Marie", 35, "Rue A")
    self.enfant = Enfant("Martin", "Lucas", 12, "Rue B")

  def test_str_adulte(self):
    """Vérifie que __str__ formate correctement un Adulte."""
    self.assertEqual(
        str(self.adulte), "Marie Dupont, 35 ans, habite a Rue A"
    )

  def test_str_enfant(self):
    """Vérifie que __str__ formate correctement un Enfant."""
    self.assertEqual(
        str(self.enfant), "Lucas Martin, 12 ans, habite a Rue B"
    )

  def test_affichage_polymorphique(self):
    """Vérifie que la fonction affichage fonctionne pour Adulte et Enfant."""
    # Capture de la sortie standard (print)
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
      affichage(self.adulte)
      affichage(self.enfant)
    finally:
      sys.stdout = sys.__stdout__  # Restauration de stdout

    output_lines = captured_output.getvalue().strip().split("\n")
    self.assertEqual(output_lines[0], "Marie Dupont, 35 ans, habite a Rue A")
    self.assertEqual(output_lines[1], "Lucas Martin, 12 ans, habite a Rue B")


if __name__ == "__main__":
  unittest.main(verbosity=2)