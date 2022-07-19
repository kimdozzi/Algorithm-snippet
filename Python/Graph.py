from collections import deque
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
adj_matrix = [[0 for _ in range(v)] for _ in range(v)]
adj_list = [[] for _ in range(v)]


for _ in range(e):
    u, v = map(int, sys.stdin.readline().split())
# 인정 행렬
    # 방향 그래프
    adj_matrix[u][v] = 1
    # adj_matrix.append([u, v])

    # 무방향 그래프
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
    # adj_matrix.append([u, v])
    # adj_matrix.append([v, u])


# 인접 리스트
    # 방향 그래프
    # adj_list[u].append(v)

    # 무방향 그래프
    adj_list[u].append(v)
    adj_list[v].append(u)


# 딕셔너리와 set
k = 4
graph = {}
for _ in range(k):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)

    if y not in graph.keys():
        graph[y] = set([x])
    else:
        graph[y].add(x)

# ----------------------------------------------------
# BFS와 DFS
input = sys.stdin.readline
n, m, start = map(int, input().split())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]


def bfs(graph, start, visited):
    queue = deque([start])
    # stack = [start]  DFS
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, start, visited)
print()
visited = [False for _ in range(n+1)]
bfs(graph, start, visited)
