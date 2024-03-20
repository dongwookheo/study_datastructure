import queue


def stack_using_list():
    """
    @brief Example of using list as a stack

    push(), pop(), peek() -> append(), pop(), list_name[-1]
    is_empty() -> len(list_name) == 0
    Does not provide is_full() method, because list has infinite capacity
    """
    stack = list()

    msg = input("Enter a message: ")
    for c in msg:
        stack.append(c)

    print("The stack is: ", end=' ')
    while len(stack) > 0:
        print(stack.pop(), end='')


def stack_using_LifoQueue():
    """
    @brief Example of using LifoQueue as a stack

    push(), pop() -> put(), get()
    is_empty(), is_full() -> empty(), full()
    Does not provide 'peek()' method
    """
    stack = queue.LifoQueue()

    msg = input("Enter a message: ")
    for c in msg:
        stack.put(c)

    print("The stack is: ", end=' ')
    while not stack.empty():
        print(stack.get(), end='')


if __name__ == '__main__':
    stack_using_list()
    print('\n', '-' * 50)
    stack_using_LifoQueue()
