"""
@file deque.py
@brief Deque Data Structure Class
@author dongwook heo
@date 2024-03-20
"""
import sys
from typing import Union

from data_structure.queue.queue import CircularQueue


class CircularDeque(CircularQueue):
    """
    @brief Deque Data Structure Class (Circular Deque)

    In the case of the linear deque, insertion and deletion occur repeatedly.
    So, it is essential to move the entire element to fill the front space.
    Therefore, only a circular deque that may prevent such inefficient operation was written.
    """

    def __init__(self, capacity: int) -> None:
        """
        @brief Constructor for CircularDeque
        @param capacity The capacity of the CircularDeque
        @return None
        """
        super().__init__(capacity)

    def is_empty(self) -> bool:
        """
        @brief Returns whether the Deque is empty
        @return True if the Deque is empty, False otherwise
        """
        return super().is_empty()

    def is_full(self) -> bool:
        """
        @brief Returns whether the Deque is full
        @return True if the Deque is full, False otherwise
        """
        return super().is_full()

    def size(self) -> int:
        """
        @brief Returns the size of the Deque
        @return The size of the Deque
        """
        return super().size()

    def display_deque(self, message: str) -> None:
        """
        @brief Displays all the elements in the Deque
        @param message The message to be displayed terminal with the Deque
        @return None
        """
        self.display_queue(message)

    def add_rear(self, element: Union[str, int, float, bool]) -> None:
        """
        @brief Adds an element to the end of the Deque
        @param element The element to be added
        @return None
        """
        self.enqueue(element)

    def delete_front(self) -> Union[str, int, float, bool]:
        """
        @brief Deletes the element from the front of the Deque
        @return The element to be deleted
        """
        return self.dequeue()

    def get_front(self) -> Union[str, int, float, bool]:
        """
        @brief Returns the element at the front of the Deque without removing it
        @return The element at the front
        """
        return self.peek()

    def add_front(self, element: Union[str, int, float, bool]) -> None:
        """
        @brief Adds an element to the front of the Deque
        @param element The element to be added to the front
        @return None
        """
        if not self.is_full():
            self.array[self.front] = element
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            sys.exit("The Deque is full")

    def delete_rear(self) -> Union[str, int, float, bool]:
        """
        @brief Deletes the element from the rear of the Deque
        @return The element to be deleted
        """
        if not self.is_empty():
            element = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return element
        else:
            sys.exit("The Deque is empty")

    def get_rear(self) -> Union[str, int, float, bool]:
        """
        @brief Returns the element at the rear of the Deque without removing it
        @return The element at the rear
        """
        if not self.is_empty():
            return self.array[self.rear]
        else:
            print("The Deque is empty")
