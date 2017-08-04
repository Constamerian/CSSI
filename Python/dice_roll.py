import random

i = 0

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print "Rolls: {0} {1}".format(die1, die2)
    i += 1
    if die1 == 6 and die2 == 6:
        print "Got double sixes!"
        print "Took {} rolls to get double sixes!".format(i)
        break
    elif die1 == 1 and die2 == 1:
        print "Got snake eyes!"
