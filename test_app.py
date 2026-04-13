import unittest
from app import calculer_prix_total, verifier_age

class TestApp(unittest.TestCase):
    
    def test_calculer_prix_total(self):
        # Test avec un panier vide
        self.assertEqual(calculer_prix_total([]), 0)
        
        # Test avec un seul article
        panier = [(10, 2)]  # 10€ x 2
        self.assertEqual(calculer_prix_total(panier), 20)
        
        # Test avec plusieurs articles
        panier = [(10, 2), (5, 3)]  # 20 + 15 = 35
        self.assertEqual(calculer_prix_total(panier), 35)
    
    def test_verifier_age(self):
        self.assertEqual(verifier_age(15), "Mineur")
        self.assertEqual(verifier_age(18), "Majeur")
        self.assertEqual(verifier_age(25), "Majeur")

if __name__ == '__main__':
    unittest.main()