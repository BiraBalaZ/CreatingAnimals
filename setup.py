from backstage import CreateAnimal

# Criando um cachorro
dog = CreateAnimal('Small', 'Passive', 'Terrestrial', 4, 'The best man´s friend')
print(CreateAnimal.generatingAnimal(dog))

# Criando um peixe (Dourado)
shark = CreateAnimal('Medium', 'Neutral', 'Aquatic', 'Undefined', 'Sharks do not watch very well, be carefull')
print(CreateAnimal.generatingAnimal(shark))

# criando um passaro (Tucano)
dragon = CreateAnimal('Big', 'Agressive', 'Aerial', 4, 'A terrible creature')
print(CreateAnimal.generatingAnimal(dragon))
