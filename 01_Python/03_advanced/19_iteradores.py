# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you 
# can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the 
# iterator protocol, which consist of the methods __iter__() and __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

# ------------------------------------------------------------------------

# import time
from time import sleep

class FiboIter():

    def __init__(self, max_element: int = None, max_num: int = None ) -> None:
        """
        max_element: maximum number of elements in the sequence.
        max_num: maximum number of the output.
        """
        self.max_element = max_element
        self.max_num = max_num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if (
            (not self.max_element and not self.max_num) 
            or ((self.counter < self.max_element) and (self.n2 < self.max_num))
            ):

            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if __name__ == '__main__':
    fibonacci = FiboIter(max_num= 50)
    for element in fibonacci:
        print(element)
        sleep(0.1)