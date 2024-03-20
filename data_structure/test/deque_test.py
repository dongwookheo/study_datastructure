from data_structure.deque.deque import CircularDeque

if __name__ == '__main__':
    d = CircularDeque(capacity=10)

    for i in range(9):
        # 짝수이면 후단, 홀수이면 전단에 삽입
        if i % 2 == 0:
            d.add_rear(i)
        else:
            d.add_front(i)
    d.display_deque("홀수는 전단, 짝수는 후단에 삽입:\n")

    for i in range(2):
        d.delete_front()
    for i in range(3):
        d.delete_rear()
    d.display_deque("전단 삭제 2, 후단 삭제 3")
    
    for i in range(9, 14):
        d.add_front(i)
    d.display_deque("전단에 9 ~ 13 삽입")
