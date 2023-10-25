# loop to count from 1 to 100
for i in range(1, 101):
    #  multiples of both three and five like html 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #  multiples of three
    elif i % 3 == 0:
        print("Fizz")
    #  the multiples of five
    elif i % 5 == 0:
        print("Buzz")
    # prints the number
    else:
        print(i)