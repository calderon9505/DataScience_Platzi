#[element for element in iterable if condition if condition]
#[key : value for value in iterable if condition if condition]

from math import sqrt
# https://realpython.com/python-import/

def run():
    
    # square = []
    # for i in range (1,101):
    #     if i % 3:
    #         square.append(i**2)

    square = [i**2 for i in range(1,101) if i%3]
    cube = {i : i**3 for i in range (1,101) if i%3}
    
    # print(square)
    # print(cube)

    newList = [i for i in range(4,100_000, 4) if (i%6 or i%9) == 0]
    newDict = {i : round(sqrt(i),2) for i in range (1,101)}

    # print(newList)
    print(newDict)


if __name__ == "__main__":
    run()