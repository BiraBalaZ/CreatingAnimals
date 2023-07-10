class CreateAnimal:
    def __init__(self, size, temperament, type, legs='Undefined', description ='Nothing to declare'):

        # Iniciando um animal
        self.size = size
        self.temperament = temperament
        self.type = type
        self.legs = legs
        self.description = description

    # Criando um animal de fato
    def generatingAnimal(self):
        if (self.legs != 'Undefined'):
            return f'O Animal em questão tem {self.legs} patas, tem temperamento "{self.temperament}", tem tamanho "{self.size}" e é do tipo "{self.type}"\nDescrição: {self.description}\n'
        else:
            return f'O Animal em questão não possui patas, tem temperamento "{self.temperament}", tem tamanho "{self.size}" e é do tipo "{self.type}"\nDescrição: {self.description}\n'