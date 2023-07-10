class CreateAnimal:

    # Iniciando um animal
    def __init__(self, size, temperament, type, legs=None):
        self.type = type
        self.legs = legs
        self.size = size
        self.temperament = temperament

    def criar(self, size, temperament, type, legs = None):
        if (self.legs != None):
            return f'O Animal em questão tem {self.legs} patas, tem temperamento {self.temperament}, tem tamanho {self.size} e é do tipo {self.type}'
        else:
            return f'O Animal em questão tem temperamento {self.temperament}, tem tamanho {self.size} e é do tipo {self.type}'