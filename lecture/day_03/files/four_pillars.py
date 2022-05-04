# ##four pillars

# ## TODO benifits 

# # keeping our code DRY


# ## TODO encapsulation

class Pet:
    
    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")




# ## TODO inheritance ## TODO polymorphism


class Dog(Pet):
    pass

class Cat(Pet):
    pass


dog1 = Dog('poodle', 'fluffy')
print(dog1)


# ## TODO abstraction
