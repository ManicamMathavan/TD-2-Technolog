from pizza import Pizza

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
        self.pizzas[:] = [pizza for pizza in self.pizzas if pizza.name!=name] 
    
a=CartePizzeria([Pizza(["salade"],"salade pizza",10)])
print(a.is_empty())
a.remove_pizza("salade pizza")
print(a.is_empty())
