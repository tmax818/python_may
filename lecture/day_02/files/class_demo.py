my_str = "spam"

# print(type(my_str))

# print(my_str.upper())

class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def fetch(self):
        return f"{self.name} runs after the ball"

dog1 = Dog('fluffy', 'dobermann')

print("fluffy= ", dog1)
print(dog1.name)
print(dog1.breed)
print(dog1.fetch())