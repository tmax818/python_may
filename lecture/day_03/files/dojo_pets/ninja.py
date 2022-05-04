from pet import Pet
class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.make_noise()

dog = Pet('Chewy', 'dog', 50, ['sits', 'shakes'], 50, 'woof')

alden = Ninja('Alden', 'Choe', dog, 'biscuts', 'alpo')