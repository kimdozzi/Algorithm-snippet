import sys
n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort(reverse=True)

sum = 0
for i in range(1, n+1):
    temp = lst[i-1] - (i - 1)
    if temp < 0:
        sum += 0
    else:
        sum += temp

print(sum)