from backstage import CreateAnimal

# Criando um cachorro
dog = CreateAnimal('Medium', 'Neutral', 'Terrestrial', 4, 'Lulu da Pomerânia')
print(CreateAnimal.generatingAnimal(dog))

# Criando um peixe
goldfish = CreateAnimal('Small', 'Passive', 'Aquatic')
print(CreateAnimal.generatingAnimal(goldfish))

# criando um passaro
toucan = CreateAnimal('Big', 'Agressive', 'Aerial')
print(CreateAnimal.generatingAnimal(toucan))
