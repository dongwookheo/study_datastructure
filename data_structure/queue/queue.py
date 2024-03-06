"""
@file queue.py
@brief Queue Data Structure Class
@author dongwook heo
@date 2024-03-06
"""
import random
import sys
from typing import Union


class CircularQueue:
    """
    @brief Queue Data Structure Class (Circular Queue)

    In the case of the linear queue, insertion and deletion occur repeatedly.
    So, it is essential to move the entire element to fill the front space.
    Therefore, only a circular queue that may prevent such inefficient operation was written.
    """

    def __init__(self, capacity: int):
        """
        @brief Constructor for CircularQueue
        @param capacity The capacity of the CircularQueue
        @return None
        """
        ## The capacity of queue
        self.capacity = capacity
        ## The array of queue
        self.array = [None] * capacity
        ## The front index of queue
        self.front = 0
        ## The rear index of queue
        self.rear = 0

    def is_empty(self) -> bool:
        """
        @brief Returns whether the Queue is empty
        @return True if the Queue is empty, False otherwise
        """
        return self.front == self.rear

    def is_full(self) -> bool:
        """
        @brief Returns whether the Queue is full
        @return True if the Queue is full, False otherwise
        """
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, element: Union[str, int, float, bool]) -> None:
        """
        @brief Inserts a new element at the end of the Queue
        @param[in] element The element to be inserted at the end of the Queue
        @return None
        """
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = element
        else:
            sys.exit("Queue is full")

    def enqueue_ringbuffer(self, element: Union[str, int, float, bool]) -> None:
        """
        @brief Inserts a new element at the end of the Queue,
        if the queue is full then it will remove the element from the front.
        @param[in] element The element to be inserted at the end of the Queue
        @return None
        """
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = element
        if self.is_empty():  # front == rear
            self.front = (self.front + 1) % self.capacity  # remove the element

    def dequeue(self) -> Union[str, int, float, bool]:
        """
        @brief Removes the element at the front of the Queue
        @return The element at the front of the Queue
        """
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            dequeued_element = self.array[self.front]
            self.array[self.front] = None
            return dequeued_element
        else:
            sys.exit("Queue is empty")

    def peek(self) -> Union[str, int, float, bool]:
        """
        @brief Returns the element at the front of the Queue
        @return The element at the front of the Queue
        """
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print("Queue is empty")

    def size(self) -> int:
        """
        @brief Returns the size of the Queue
        @return The size of the Queue
        """
        return (self.rear - self.front + self.capacity) % self.capacity

    def display_queue(self, message: str) -> None:
        """
        @brief Displays all the elements in the Queue
        @return All the elements in the Queue
        """
        print(message, end=": [")
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=" ")
        print("]")
