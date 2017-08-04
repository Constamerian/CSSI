#my_string = raw_input('Type something: ')

#upper() method on string would capitalize the string
#print "{} {}".format("", "") is the way to format a string
#Unlike JS, Python does not support ++, thus you should use += 1 instead

#print "print words in upper case"
#index = 0
#for my_word in my_string.split(): #return individual words in a string. Split it with white space
#    print "{} {}".format(index, my_word.upper()) #capitalize the words
#    index += 1

#print "Print each letter upper case"
#index = 0
#for letter in my_string:
#    print "{} {}".format


#while True: #infinite loop unless you hit the break keyword
#    input = raw_input("Type something here: ")



#some_numbers = [2, 52, 19, 46, 1000]
#index = 0
#for number in some_numbers:
#    print (some_numbers[index]+10)/2
#    index += 1



presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams"]
for president in presidents:
    reversedpresident = ""
    for letter in president:
        #print president[::-1]
        reversedpresident = letter +reversedpresident
    print reversedpresident
