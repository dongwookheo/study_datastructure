"""
@file: stack_test.py
@brief Test Stack class
@author: dongwook heo
@time: 2024-02-29
"""
from data_structure import stack

if __name__ == '__main__':
    s = stack.Stack(100)
    msg = input("Enter message: ")
    for char in msg:
        s.push(char)

    print("Reversed message: ", end='')
    while not s.is_empty():
        print(s.pop(), end='')
