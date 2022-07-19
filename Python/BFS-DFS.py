# BFS / DFS
# BFS (Queue) 활용 , DFS (Stack) 활용
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


print(bfs(0, 0))


# BFS (벽 부수고 이동하기)

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
visited = [[[0, 0] for _ in range(col)] for _ in range(row)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y, iscrash, visited, graph):
    # crash 0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((start_x, start_y, iscrash))
    visited[start_x][start_y][iscrash] = 1

    while queue:
        x, y, iscrash = queue.popleft()
        if x == row - 1 and y == col - 1:
            return visited[x][y][iscrash]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= row or ny <= -1 or ny >= col:
                continue
            # 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][iscrash] == 0:
                queue.append((nx, ny, iscrash))
                visited[nx][ny][iscrash] = visited[x][y][iscrash] + 1
            # 벽 부수고 이동
            if graph[nx][ny] == 1 and iscrash == 0:
                queue.append((nx, ny, iscrash + 1))
                visited[nx][ny][iscrash + 1] = visited[x][y][iscrash] + 1

    return -1


print(bfs(0, 0, 0, visited, graph))
