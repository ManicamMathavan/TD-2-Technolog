import unittest
from unittest.mock import Mock, patch
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException
class TestCartePizzeria(unittest.TestCase):
    
    def test_is_empty(self):
        pizzaMock= Mock()
        carte_pizza=CartePizzeria(pizzaMock)
        self.assertFalse(carte_pizza.is_empty())
        carte_pizza=CartePizzeria()
        self.assertTrue(carte_pizza.is_empty())
        
    def test_remove_pizza(self):
        pizzaMock= Mock()
        pizzaMock.ingredients=["salade"]
        pizzaMock.name="salade pizza"
        pizzaMock.price=10
        carte_pizza=CartePizzeria(pizzaMock)
        carte_pizza.remove_pizza("salade pizza")
        self.assertTrue(len(carte_pizza.pizzas)==0)
        carte_pizza=CartePizzeria()
        self.assertRaises(CartePizzeriaException,carte_pizza.remove_pizza,"salade pizza")
        
    def test_nb_pizzas(self):
        pizzaMock= Mock()
        pizzaMock.ingredients=["salade"]
        pizzaMock.name="salade pizza"
        pizzaMock.price=10
        carte_pizza=CartePizzeria(pizzaMock)
        self.assertTrue(carte_pizza.nb_pizzas()==1)
        carte_pizza=CartePizzeria()
        self.assertTrue(carte_pizza.nb_pizzas()==0)
        
    def test_add_pizza(self):
        pizzaMock= Mock()
        pizzaMock.ingredients=["salade"]
        pizzaMock.name="salade pizza"
        pizzaMock.price=10
        carte_pizza=CartePizzeria()
        carte_pizza.add_pizza(pizzaMock)
        self.assertTrue(len(carte_pizza.pizzas)==1)
        carte_pizza=CartePizzeria(pizzaMock)
        carte_pizza.add_pizza(pizzaMock)
        self.assertTrue(len(carte_pizza.pizzas)==2)

        
        
    
        
         
unittest.main()