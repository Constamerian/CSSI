class Spaceship:
    def __init__(self, color, fly, size):
        self.color = color
        self.fly = fly
        self.size = size

    def fix_spaceship(self):
        if self.fly:
            print "It doesn\'t need fixing!"
        else:
            self.fly = True
            print "All fixed!"

Constellation = Spaceship("blue", True, "medium")
soil = Spaceship("brown", False, "Extra large")

Constellation.fix_spaceship()
soil.fix_spaceship()
