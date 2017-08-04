songs = ["uptown funk", "thinking out loud" , "blank space" , "take me to church" , "shake it off"]

# for song in songs:
#     print song

dictionaryOfSongs = {"1" : "uptown funk",
                     "2" : "thinking out loud",
                     "3" : "blank space",
                     "4" : "take me to church",
                     "5" : "shake it off"}

def list_songs(listOfSongs):
    print listOfSongs

def play_songs(listOfSongs):
    list_songs(listOfSongs)
    userSong = raw_input("Enter a song number to play! ")
    print "Playing {}".format(dictionaryOfSongs[userSong])

def search_songs(listOfSongs):
    userSearch = raw_input("What are you searching for? ")
    for eachSong in songs:
        if userSearch in eachSong:
            print eachSong

while True:
    userInput = raw_input("Options: List, Play, Search, Quit ")
    userInput = str.lower(userInput)
    if userInput == "list":
        list_songs(songs)
    if userInput == "play":
        play_songs(songs)
    if userInput == "search":
        search_songs(songs)
    if userInput == "quit":
        print "Goodbye"
        print quit()
