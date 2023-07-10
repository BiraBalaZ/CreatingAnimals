from random import randint
from backstage import Quadruped, Aquatic, Aerial

choice = randint(1, 3)

# Creating an terrestrial animal
dog = Quadruped(
    name='Alice',
    size='Small', 
    temperament='Passive',
    animal_type='Terrestrial',
    paws=4,
    description='The best man´s friend'
)
print(dog)

# Sorteando ação do cachorro
if (choice == 1):
    Quadruped.walking(dog)
elif (choice == 2):
    Quadruped.running(dog)
elif (choice == 3):
    Quadruped.sleeping(dog)

# Creating an aquatic animal
shark = Aquatic(
    name='Bruce',
    size='Medium',
    temperament='Neutral',
    animal_type='Aquatic',
    description='Sharks do not watch very well, be carefull'
)
print(shark)
Aquatic.swimming(shark)

# Creating an aerial animal
dragon = Aerial(
    name='Ancient Dragon',
    size='Big',
    temperament='Agressive',
    animal_type='Aerial',
    paws=2,
    wings=2,
    description='A terrible creature'
)
print(dragon)
Aerial.flying(dragon)
