"""
@file stack.py
@brief Stack Data Structure Class
@author dongwook heo
@date 2024-02-28
"""
import sys
from typing import Union


class Stack:
    """
    @brief Stack Data Structure Class
    """

    def __init__(self, capacity: int) -> None:
        """
        @brief Constructor for Stack
        @param[in] capacity The capacity of the stack
        @return None
        """
        ## The capacity of the stack
        self.capacity = capacity
        ## The array of the stack
        self.array = [None] * capacity
        ## The top of the stack
        self.top = -1

    def is_empty(self) -> bool:
        """
        @brief Returns whether the stack is empty
        @return True if the stack is empty, False otherwise
        """
        return self.top == -1

    def is_full(self) -> bool:
        """
        @brief Returns whether the stack is full
        @return True if the stack is full, False otherwise
        """
        return self.top == self.capacity - 1

    def push(self, element: Union[str, int, float, bool]) -> None:
        """
        @brief Push an element to the top of the stack
        @param[in] element The element to be pushed to the top of the stack
        @return None
        """
        if not self.is_full():
            self.top += 1
            self.array[self.top] = element
        else:
            sys.exit("Stack overflow!")

    def pop(self) -> Union[str, int, float, bool]:
        """
        @brief Pop an element from the top of the stack
        @return The element at the top of the stack
        """
        if not self.is_empty():
            self.top -= 1
            popped_element = self.array[self.top + 1]
            self.array[self.top + 1] = None
            return popped_element
        else:
            sys.exit("Stack underflow!")

    def peek(self) -> Union[str, int, float, bool]:
        """
        @brief Return the element at the top of the stack
        @return The element at the top of the stack
        """
        if not self.is_empty():
            return self.array[self.top]
        else:
            print("Stack is empty.")

    def size(self) -> int:
        """
        @brief Return the size of the stack
        @return The size of the stack
        """
        return self.top + 1
