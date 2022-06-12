import sys
v = int(input())
e = int(input())
adj_matrix = []
for _ in range(e):
    u, v = map(int, sys.stdin.readline().split())
    adj_matrix.append([u, v])
print(adj_matrix)
