class CreateAnimal:
    def __init__(self, size, temperament, type, legs='Undefined', description ='Nothing to declare'):

        # Initializing an animal
        self.size = size
        self.temperament = temperament
        self.type = type
        self.legs = legs
        self.description = description

    # Creating animal
    def generatingAnimal(self):
        if (self.legs != 'Undefined' and self.legs != 0):
            return f'This animal has {self.legs} paws, has an {self.temperament} temperament, and he is {self.size} in his size and the "{self.type} type"\nDescription: {self.description}\n'
        else:
            return f'This animal do not have paws, has an {self.temperament} temperament, his is {self.size} and his type is "{self.type}"\nDescription: {self.description}\n'
        