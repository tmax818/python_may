class Pet:

    def __init__(self, name, type, energy, tricks, health, noise) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.health += 10
        self.energy += 5

    def play(self):
        self.health += 5

    def make_noise(self):
        print(self.noise)
        print(f"{self.name} says {self.noise}")