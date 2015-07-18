const_name = "Fizz buzz counting up to n"
for n in range(1,101):
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("buzz")
    if (n % 5 == 0) and (n % 3 == 0):
        print("fizzbuzz")
    else:
        print(n)