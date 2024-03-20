import queue
import random


def queue_using_Queue():
    q = queue.Queue(20)

    print("Order of insertion: ")
    while not q.full():
        value = random.randint(0, 100)
        q.put(value)
        print(value, end=' ')
    print()

    print("Order of deletion: ")
    while not q.empty():
        print(q.get(), end=' ')
    print()


if __name__ == '__main__':
    queue_using_Queue()
