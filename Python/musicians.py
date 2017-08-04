class Musician:
    def __init__(self, name, instrument, song, recording):
        #self is the identity of the object
        self.name = name
        self.instrument = instrument
        self.song = song
        self.recording = recording

    def description(self):
        return "Hey my name is {0}, I play {1}, and my favorite song is {2}".format(self.name, self.instrument, self.song)

    def is_recording(self):
        if self.recording:
            return "woohooo I am recording!"
        else:
            return "nah maybe later, I'm napping!"

kanye = Musician('kanye', 'vocals', 'famous', True)
chance = Musician('chance', 'rapper', 'no problem', False)

# print kanye.name
# print kanye.instrument
# print kanye.song

# print kanye.description()
# print chance.description()

print kanye.is_recording()
print chance.is_recording()
