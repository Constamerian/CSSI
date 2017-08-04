VOWELS = ["A", "E", "I", "O", "U"]

def LongShout(word, multiplier):
    word = word.upper()
    count = 1
    for vowel in VOWELS:
        long_vowels = vowel * multiplier * count
        word = word.replace(vowel, long_vowels)
        count = count + 1
        #or count = count += 1
    return word

print LongShout('COOKIE', 4)
print LongShout('cookie', 4)




# groceries = {'eggs': 5, 'butter': 4, 'chocolate': 2}
# for item in groceries:
#     #items: $(price)
#     print item + ": $" + str(groceries[item])
