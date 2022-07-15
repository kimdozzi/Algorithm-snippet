import sys
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위를 초과하면 무시
                continue
            if graph[nx][ny] == 0:  # 벽이라면 무시
                continue
            if graph[nx][ny] == 1:  # 벽이 아니라면, 갈 수 있는 길이라면
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))


# 토마토
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()
for tomatoes in graph:
    for tomato in tomatoes:
        if tomato == 0:
            print(-1)
            exit(0)
    res = max(res, max(tomatoes))
print(res-1)
