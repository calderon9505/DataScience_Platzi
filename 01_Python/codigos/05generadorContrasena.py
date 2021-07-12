import random

def generate_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F']
    minus = ['a', 'b', 'c' ,'d', 'e', 'f']
    symbol = ['!', '#', '$', '.', '-', '&', '/', '(', ')']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    character = mayus + minus + symbol + number

    password = []

    for i in range(15):
        password.append(random.choice(character))
    
    return ''.join(password) #convertir a string


def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()
