from backstage import CreateAnimal

# Criando um cachorro
dog = CreateAnimal('Small', 'Passive', 'Terrestrial', 4, 'The best man´s friend')
print(CreateAnimal.generatingAnimal(dog))

# Criando um peixe (Dourado)
shark = CreateAnimal('Medium', 'Neutral', 'Aquatic')
print(CreateAnimal.generatingAnimal(shark))

# criando um passaro (Tucano)
dragon = CreateAnimal('Big', 'Agressive', 'Aerial')
print(CreateAnimal.generatingAnimal(dragon))
