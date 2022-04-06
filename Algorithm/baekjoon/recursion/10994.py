from collections import deque
def stars(lst,i) :
    temp_que = deque(lst) #이전 패턴을 출력하기 위함.
    if i == 1:
        lst.append('*')
        return lst

    cnt = len(lst)
    que = deque() # 패턴을 저장하고 반환할 queue
    star = '*'
    pattern = star + ((i-1) * '****')

    que.append(pattern)
    s = star + (' ' * (cnt+2)) + star
    que.append(s)

    for i in range(len(temp_que)) :
        x = star + ' ' + temp_que.popleft() + ' ' + star
        que.append(x)

    s = star + (' ' * (cnt + 2)) + star
    que.append(s)
    que.append(pattern)
    return que

if __name__ == '__main__' :
    n = int(input())
    lst = []
    for i in range(1,n+1) :
        lst = stars(lst,i)
    for i in lst:
        print(i)
