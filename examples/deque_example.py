import collections


def deque_example():
    """
    @brief Example of deque with collections.deque

    addFront(), deleteFront() -> appendleft(), popleft()
    addRear(), deleteRear() -> append(), pop()
    is_empty() -> deque_name (but, False means it is empty)
    Does not provide 'is_full()', because collections.deque has infinite capacity
    Does not provide 'get_front()' and 'get_rear()' methods
    """
    deque = collections.deque()

    print("deque is not empty" if deque else "deque is empty")
    for i in range(9):
        if i % 2 == 0:
            deque.append(i)
        else:
            deque.appendleft(i)
    print("Odds are added front, evens are added rear:\n", deque)

    for i in range(2):
        deque.popleft()
    for i in range(3):
        deque.pop()
    print("Deletion from front 2, Deletion from rear 3:\n", deque)

    print(deque.extend([1, 2, 3]), deque)  # rear에 list를 붙임, extendleft()는 front에 붙임
    print(deque.rotate(3), deque)  # integer argument 만큼 우로 이동, 음수인 경우 좌로 이동
    print(deque.count(1), deque)  # argument 값이 몇 개 있는지 반환
    

if __name__ == "__main__":
    deque_example()
