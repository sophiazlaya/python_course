
class Dog:
    def __init__(self, name, is_hungry):
        self.name = name
        self.is_hungry = is_hungry

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_food(self, dog):
        if dog.is_hungry:
            dog.is_hungry = False

Sharik = Dog('Sharik', True)
Alex = Human('Alex', 20)
Alex.get_food(Sharik)
print(Sharik.is_hungry)