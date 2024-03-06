"""
@file: queue_test.py
@brief Test Queue class
@author: dongwook heo
@date: 2024-03-06
"""
import random
from data_structure.queue import queue


def test_queue1() -> None:
    """
    @brief Test queue if FIFO works correctly
    @return None
    """
    q = queue.CircularQueue(8)

    q.display_queue("Initial queue")
    while not q.is_full():
        q.enqueue(random.randint(0, 100))
    q.display_queue("Full queue")

    print("An order of deletion: ", end='')
    while not q.is_empty():
        print(q.dequeue(), end=' ')


def test_queue2() -> None:
    """
    @brief Test queue if enqueue works correctly for ringbuffer
    @return None
    """
    q = queue.CircularQueue(8)

    q.display_queue("Initial queue")
    for i in range(7):
        q.enqueue(i)
    q.display_queue("Full queue")

    q.enqueue_ringbuffer(7)
    q.enqueue_ringbuffer(8)
    q.display_queue("Insertion 7, 8")

    q.dequeue()
    q.display_queue("Deletion")


if __name__ == '__main__':
    test_queue1()
    print('\n', '-' * 30)
    test_queue2()
