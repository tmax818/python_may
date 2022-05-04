
# TODO user story: As an admin user of the dojo tracker I would like to keep track of which ninjas and instructors are assigned to a dojo. Each dojo should be able to modify its motto if so desired.

dojos = [
    {'id': 1, 'location': 'Burbank', 'capacity': 30},
    {'id': 2, 'location': 'San Jose', 'capacity': 30}
]

ninjas = [
        {'id': 1, 'name': 'Aaron', 'dojo_id': 1},
        {'id': 1, 'name': 'Cesar', 'dojo_id': 2},
        {'id': 1, 'name': 'Devin', 'dojo_id': 1},
        {'id': 1, 'name': 'Tim', 'dojo_id': 2},
        {'id': 1, 'name': 'Frank', 'dojo_id': 2},
]

instructors = [
    {'id': 1, 'name': 'Davina', 'languages': ['JS', 'CSS', 'HTML'], 'dojo_id': 2},
    {'id': 2, 'name': 'Tyler', 'languages': ['Python'], 'dojo_id': 1},
    {'id': 3, 'name': 'Moses', 'languages': [], 'dojo_id': 1}
]
class Instructor:
    def __init__(self, name, languages, dojo_id) -> None:
        self.name = name
        self.languages = languages
        self.dojo_id = dojo_id
        pass

## TODO make a dojo class
class Dojo:
    motto = "Strength through struggle."
## TODO dojo attr: location, capacity and id
    def __init__(self, location, capacity, id, instructor) -> None:
        self.location = location
        self.capacity = capacity
        self.ninjas = []
        self.id = id
        self.instructor = instructor

    def add_ninja(self, ninja):
        self.ninjas.append(ninja)

    @classmethod
    def change_motto(cls, new_motto):
        cls.motto = new_motto
    
    @classmethod
    def show_motto(cls):
        print(cls.motto)

    @staticmethod
    def validate_instructor(instructor):
        is_valid = True
        if len(instructor['languages']) < 1:
            is_valid = False
        return is_valid


## TODO methods: display languages taught, show location, display instructor, register_ninjas

## TODO make a instructor class
## TODO also need instructors: name, languages, assigned to dojo, 
# TODO methodsstart class, give assignments


## TODO make a ninja class: name, id, assigned to dojo
class Ninja:

    def __init__(self, name) -> None:
        self.name = name
## TODO methods: study



instructor1 = Instructor('Tyler', ['Python'], 1)
Dojo.change_motto("Strength through 20 minutes of struggle.")
Dojo.show_motto()
ninja1 = Ninja('Frank')
dojo1 = Dojo('Burbank', 15, 1, instructor1)
print("is_valid: ", dojo1.validate_instructor(instructors[-1]))

dojo1.add_ninja(ninja1)
print(dojo1)
print(dojo1.location)

def add(a:int,b:int) -> int:
    return a+b

