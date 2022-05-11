class User:
    def __init__(self, data) -> None:
        self.name = data['name']
        self.age = data['age']

    @classmethod
    def make_user(cls):
        User(results[0])




results = [
    {'name': 'Tyler', 'age': 39},
    {'name': 'Davita', 'age': 19},
    {'name': 'Yo Han', 'age': 35}
]
user1 = User(results[0])