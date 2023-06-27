from collections import deque
import sys


def front(d):
    try:
        return d.index(0)
    except:
        return -1

def back(d):
    try:
        return d.index(len(d)-1)
    except:
        return -1
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    deq = deque()

    input = {
        "push_back" : deq.append,
        "push_front" : deq.appendleft,
        "pop_front": -1 if len(deq) == 0 else deq.popleft(),
        "pop_back" : -1 if len(deq) == 0 else deq.pop(),
        "size" : len(deq),
        "empty" : 1 if len(deq) == 0 else 0,
        "front" : front(deq),
        "back" : back(deq),
    }

    for _ in range(N):
        tmp = sys.stdin.readline()
        if ' ' in tmp :
            command, value = map(str, tmp.split(' '))
            value = int(value)
            if command == 'push_back':
                deq.append(value)
            elif command == 'push_front':
                deq.appendleft(value)

        else:
            command = tmp
            print(input[command[:-1]])

    print(list(deq))

    
    
    

