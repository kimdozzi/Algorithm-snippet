import sys
from collections import deque
n = int(sys.stdin.readline())
Queue = deque()

for i in range(n) :
    command = list(sys.stdin.readline().split())

    if command[0] == 'pop':
        if Queue:
            print(Queue.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        if Queue:
            print(len(Queue))
        else:
            print(0)

    elif command[0] == 'empty':
        if Queue:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if Queue:
            print(Queue[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if Queue:
            print(Queue[-1])
        else:
            print(-1)

    else:
        Queue.append(command[1])


