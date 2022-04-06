import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
sum = []
lst.sort()
flag = 0
if len(lst) % 2 != 0 and flag == 0:
    sum.append(lst.pop(-1))
    flag = 1

for i in range(len(lst)//2) :
    sum.append(lst[0] + lst[-1])
    lst.pop(0)
    lst.pop(-1)

print(max(sum))
