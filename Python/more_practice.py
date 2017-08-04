input = raw_input("Please input x: ")
#x = int(input)

#what if input is "abc" instead?

try:
    x = int(input)
except Exception as ex:
    print "x is invalid"
    exit()

if x > 500:
    print "x is really big"

elif x <= 500 and x > 50:
    print "x is sort of big"

elif x < 0:
    print "x is negative"

else:
    print "x is not very interesting"
