# assert condition, error message

# In plain English, an assert statement says, “I assert that this 
# condition holds true, and if not, there is a bug somewhere in the program.”

# Unlike exceptions, your code should not handle assert statements with try 
# and except; if an assert fails, your program should crash. By failing fast 
# like this, you shorten the time between the original cause of the bug and 
# when you first notice the bug. This will reduce the amount of code you 
# will have to check before finding the code that’s causing the bug.

# Assertions are for programmer errors, not user errors. 
# For errors that can be recovered from (such as a file not being found 
# or the user enter-ing invalid data), raise an exception instead of 
# detecting it with an assert statement.

def divisors(num):
    assert num > 0, 'Only natural numbers'
    return [i for i in range (1, num+1) if num%i == 0]


def run():
    num = input("Ingrese un numero: ")
    # assert num.isnumeric(), 'Must be a number'
    print(divisors(int(num)))

if __name__ == "__main__":
    run()