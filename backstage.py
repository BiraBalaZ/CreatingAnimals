class Animal:
    # Initializing an animal
    def __init__(self, name, size, temperament, animal_type, description='...'):
        self.name = name
        self.size = size
        self.temperament = temperament
        self.animal_type = animal_type
        self.description = description

class Quadruped(Animal):
    def __init__(self, paws, name, size, temperament, animal_type, description='...'):
        super().__init__(name, size, temperament, animal_type, description)
        self.paws = paws
    
    # Returning animal
    def __str__(self):
        return f'\nThis animal have {self.paws} paws, has an {self.temperament} temperament, his is {self.size} and his type is {self.animal_type}\nDescription: {self.description}\n'

    def walking(self):
        print(f'{self.name} is walking in the grass.')
    
    def running(self):
        print(f'{self.name} is running to catch the ball!')

    def sleeping(self):
        print(f'{self.name} is lying, I THINK {self.name} is sleeping...')

class Aquatic(Animal):
    # Returning animal
    def __str__(self):
        return f'\nThis animal do not have paws, he swim like no other!, has an {self.temperament} temperament, he is {self.size} and his type is {self.animal_type}\nDescription: {self.description}\n'

    def swimming(self):
        print(f'{self.name} is swimming! Get out of his way now!')

class Aerial(Animal):
    def __init__(self, paws, wings, name, size, temperament, animal_type, description='...'):
        super().__init__(name, size, temperament, animal_type, description)
        self.paws = paws
        self.wings = wings

    # Returning animal
    def __str__(self):
        return f'\nThis animal have {self.paws} paws and {self.wings} wings, has an {self.temperament} temperament, he is {self.size} and his type is {self.animal_type}\nDescription: {self.description}\n'
    
    def flying(self):
         print(f'{self.name} is flying in your direction, is this a Boss Fight?!')