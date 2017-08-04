import random

response = {"apple" : "I like apples too!",
            "water": "I can't drink water..",
            "fruit" : "I already told you I like apples!",
            "laptop" : "Are you trying to compare me with a laptop?",
            "light" : "Don't look right at it!"}

def walle_talk(word):
    if word in response:
        print response[word]
    if word == word.upper():
        print random.random() * 100
        #print random.randint(1,100)
        return "EEEEEEEEEEEVAAAAAAAAAA!"
    else:
        print random.random() * 100
        #print random.randint(1,100)
        return "Dirrrrr-ect-tivvve?"

# print walle_talk("hello")
# print walle_talk("fruit")
# print walle_talk("FRUIT")

def speak_to_walle():
    count = 0
    while(True):
        sentence = raw_input("What do you wanna say? ")
        if sentence == "BYE":
            count+=1
            if count == 3:
                break;
                print quit()
            else:
                print walle_talk(sentence)
        else:
            count = 0
            print walle_talk(sentence)
                #print sentence

speak_to_walle()
