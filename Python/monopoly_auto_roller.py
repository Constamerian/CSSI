import random

def rollDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    if die1 == die2:
        print "Doubles! Move {} spaces and roll again".format(total)
    else:
        print "Move {} spaces. Next player's turn!".format(total)

rollDice()
rollDice()
rollDice()

def RollDungeonsAndDragonsDie(numOfSides, modifier):
    die = random.randint(1, numOfSides)
    print die + modifier

RollDungeonsAndDragonsDie(6,3)




#task:
#write a function called RollManyDungeonsAndDragonsDice that takes one argument. A list of number of sides

#takes in a list of numbers (of sides)
#[4, 5, 7] = one 4 sided die, one 5 sided die, one 7 sided die

def RollManyDungeonsAndDragonsDice(sides):
    total = 0
    for side in sides:
        roll = random.randint(1, side)
        total += roll
    print "You may move " + str(total) + " spaces!"

RollManyDungeonsAndDragonsDice([4,3,6])
