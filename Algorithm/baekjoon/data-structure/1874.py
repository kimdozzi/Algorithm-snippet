import sys
input = sys.stdin.readline
n = int(input())
cnt,flag = 1,0
stack = []
ans = []
for _ in range(n):
    num = int(input())
    while num >= cnt:
        stack.append(cnt)
        cnt += 1
        ans.append('+')

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)