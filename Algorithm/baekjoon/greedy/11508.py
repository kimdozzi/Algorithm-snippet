import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort(reverse=True)
cost = 0
for i in range(len(lst)) :
    if (i+1) % 3 != 0:
        cost += lst[i]

print(cost)
