import sys
from typing import Union


class Stack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.capacity - 1

    def push(self, element: Union[str, int, float, bool]) -> None:
        if not self.is_full():
            self.top += 1
            self.array[self.top] = element
        else:
            sys.exit("Stack overflow!")

    def pop(self) -> Union[str, int, float, bool, None]:
        if not self.is_empty():
            self.top -= 1
            popped_element = self.array[self.top + 1]
            self.array[self.top + 1] = None
            return popped_element
        else:
            sys.exit("Stack underflow!")

    def peek(self) -> Union[str, int, float, bool, None]:
        if not self.is_empty():
            return self.array[self.top]
        else:
            print("Stack is empty.")

    def size(self) -> int:
        return self.top + 1