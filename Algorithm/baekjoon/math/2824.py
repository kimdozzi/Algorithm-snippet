import sys
import math
n1 = int(sys.stdin.readline())
lst1 = list(map(int,sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
lst2 = list(map(int,sys.stdin.readline().split()))
A, B = 1, 1
for i in lst1:
    A *= int(i)
for i in lst2:
    B *= int(i)

sum = str(math.gcd(A,B))

if len(str(sum)) > 9:
    sum = str(math.gcd(A, B) % 1000000000)
    while len(sum) < 9:
        sum = '0' + sum
    print(sum)

else:
    print(sum)
