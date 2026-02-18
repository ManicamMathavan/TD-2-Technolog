from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self, pizzas):
        self.pizzas=pizzas
    def is_empty(self):
        return len(self.pizzas)==0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)
        
    def remove_pizza(self,name):
        for pizza  in self.pizzas:
            if pizza.name==name:
                self.pizzas.remove(pizza)
                break
        raise CartePizzeriaException("pizza not found")
        # self.pizzas[:] = [pizza for pizza in self.pizzas if pizza.name!=name] 
    
a=CartePizzeria([Pizza(["salade"],"salade pizz",10)])
print(a.is_empty())
a.remove_pizza("salade pizza")
print(a.is_empty())
