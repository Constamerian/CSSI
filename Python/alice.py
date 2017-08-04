#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.

UniqueWords = {}

def GetUniqueWords(text):
    arrayOfWords = text.split()
    for eachWord in arrayOfWords:
        if eachWord not in UniqueWords:
            UniqueWords[eachWord] = 1
        else:
            UniqueWords[eachWord] += 1
    print UniqueWords
    return len(UniqueWords)
#    return num
# num = len(set(text.split(" ")))

# for ex: the the the cat dog dog bull

# the - {"the" : 1}
# the - {"the" : 2}
# the - {"the" : 3}
# cat - {"the" : 3, "cat" : 1,}
# dog - {"the" : 3, "cat" : 1, "dog" : "1"}
# dog - {"the" : 3, "cat" : 1, "dog" : "2"}
# bull - {"the" : 3, "cat" : 1, "dog" : "1", "bull": 1}
# return len(UniqueWords)

def mostFrequent():
    sorted_words = sorted(UniqueWords, key=UniqueWords.get, reverse=True)
    i = 0
    while i < 10:
        word = sorted_words[i]
        print word + ": " + str(UniqueWords[word])
        i += 1

#reverse=False would show the least frequently used words

def moreThan100():
    for word in UniqueWords:
        if UniqueWords[word] >= 100:
            print word + ": " + str(UniqueWords[word])

def main():
  # Open the file, read it into memory as a single string.
  with open('alice_in_wonderland.txt') as alice_file:
    alice_text = alice_file.read()

  print 'Unique words:', GetUniqueWords(alice_text)
  mostFrequent()
  print "=========== more than 100 ============="
  moreThan100()

if __name__ == '__main__':
  main()

print "Number of times Alice occurs: " + str(UniqueWords['Alice'])
print "Number of times Wonderland occurs: " + str(UniqueWords['Wonderland'])
