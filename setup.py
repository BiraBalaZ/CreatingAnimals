from backstage import CreateAnimal

# Creating an terrestrial animal
dog = CreateAnimal('Small', 'Passive', 'Terrestrial', 4, 'The best man´s friend')
print(CreateAnimal.generatingAnimal(dog))

snake = CreateAnimal('Big', 'Neutral', 'Terrestrial', 0, 'Venomous')
print(CreateAnimal.generatingAnimal(snake))

# Creating an aquatic animal
shark = CreateAnimal('Medium', 'Neutral', 'Aquatic', 0, 'Sharks do not watch very well, be carefull')
print(CreateAnimal.generatingAnimal(shark))

# Creating an aerial animal
dragon = CreateAnimal('Big', 'Agressive', 'Aerial', 4, 'A terrible creature')
print(CreateAnimal.generatingAnimal(dragon))

# Creating an hybrid animal
duck = CreateAnimal('Small', 'Passive', 'Hybrid', 2, 'Just a duck...')
print(CreateAnimal.generatingAnimal(duck))
