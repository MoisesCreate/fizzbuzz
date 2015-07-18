const_name = "Fizz buzz counting up to n"
import sys
n = 1,76
try:
    n >= 76
except TypeError:
    print("Stop Wait a Minute, Please enter a number")
print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))
for arg in sys.argv[1:]:
    len(sys.argv) <= 35
    print arg
my_input = raw_input("Enter a number, yo!")
print my_input
for n in range(1,76):
    if (n % 3 == 0) and (n % 5 != 0):
        print("Fizz")
    elif (n % 5 == 0) and (n % 3 != 0):
        print("buzz")
    elif (n % 5 == 0) and (n % 3 == 0):
        print("fizzbuzz")
    else:
        print(n)