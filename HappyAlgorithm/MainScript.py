# write down an integer
# square its digits and sum the results
# continue with this number
# repeat cycle until the answer is 1 (happy) or you get trapped in a cycle (unhappy)
# example: 4 is unhappy. 70 is happy

import random

# write down an integer
x = random.randint(1, 100)
b = x
print("random integer is", x)

def Happy_Algorithm(x, previous_numbers=None):
    if previous_numbers is None:
        previous_numbers = set()

    # separate into digits
    y = str(x)
    squared_digits = [int(char)**2 for char in y]
    #print(squared_digits)

    # square its digits
    x = sum(squared_digits)
    print("new value of x is", x)

    # check number
    if x == 1:
        print(x, "is Happy")
    elif x in previous_numbers:
        print(b, "is Unhappy")
    else:
        previous_numbers.add(x)
        Happy_Algorithm(x, previous_numbers)

Happy_Algorithm(x)