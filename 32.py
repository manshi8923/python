import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
dice=Dice()
print(dice.roll())

from pathlib import Path
#absolute path
#relative path
path=Path("emails")
print(path.mkdir())
print(path.rmdir())
