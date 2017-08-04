# FizzBuzz
# Takes in a number n
# Starting from 0 to n, print out each number in sequence
# BUT if the number is divisible by 3, print "Fizz"
# if the number is divisible by 5, print "Buzz"
# if it's divisible by both, print "FizzBuzz"

def FizzBuzz(n):
    for i in range (0, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i

def FizzBuzzLoop():
    while True:
        n = int(raw_input("Pick a number "))
        FizzBuzz(n)
        response = raw_input("Quit? ")
        if response == "Yes":
            break
    print "Goodbye"

FizzBuzzLoop ()
