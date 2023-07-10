class CreateAnimal:
    def __init__(self, size, temperament, type, legs='Undefined', description ='Undefined'):

        # Iniciando um animal        
        self.size = size
        self.temperament = temperament
        self.type = type
        self.legs = legs
        self.description = description

    def generatingAnimal(self):
        if (self.legs != 'Undefined' or self.legs == 0):
            return f'O Animal em questão tem {self.legs} patas, tem temperamento "{self.temperament}", tem tamanho "{self.size}" e é do tipo "{self.type}"'
        else:
            return f'O Animal em questão não possui patas, tem temperamento "{self.temperament}", tem tamanho "{self.size}" e é do tipo "{self.type}"'