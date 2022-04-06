# 1260 DFS, BFS 문제

import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1) :
    # graph[i] = sorted(list(set(graph[i])))
    graph[i].sort()
    

dfs(graph,v,visited)
print(end='\n')
visited = [False] * (n+1)
bfs(graph,v,visited)



'''
기본 DFS 문제

# DFS 함수 정의
def dfs(graph, v, visited):  #노드가 연결된 2차원 리스트 graph, v = 1 정점, visited = [0] * 9 (모두 false로 초기화되어 있음)
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

graph = [  # 리스트로 표현한 방식
  [],
  [2, 3, 8], # root 1과 연결된 2,3,8 자식노드
  [1, 7],    # (0,2) 2번노드 -> 2번과 연결된 root 1과 자식노드 7
  [1, 4, 5], # (0,3) 3번노드 -> 3번과 연결된 root 1과 자식 4,5
  [3, 5],    # (0,4) 4번노드 -> 4번과 연결된 부모노드 3과 연결된 노드 5
  [3, 4],    # (0,5) 5번노드 -> 5번과 연결된 부모노드 3과 연결된 노드 4
  [7],       # (0,6) 6번노드 -> 6번과 연결된 부모노드 7
  [2, 6, 8], # (0,7) 7번노드 -> 7번과 연결된 부모노드 2와 자식 6,8
  [1, 7]     # (0,8) 8번노드 -> 8번과 연결된 root 1과 부모 7
]

graph = { # 딕셔너리로 표현한 방식 -> 나는 이 방식이 더 보기 편하다.

  1 : [2, 3, 8], # root 1과 연결된 2,3,8 자식노드
  2 : [1, 7],    # (0,2) 2번노드 -> 2번과 연결된 root 1과 자식노드 7
  3 :[1, 4, 5], # (0,3) 3번노드 -> 3번과 연결된 root 1과 자식 4,5
  4 : [3, 5],    # (0,4) 4번노드 -> 4번과 연결된 부모노드 3과 연결된 노드 5
  5 : [3, 4],    # (0,5) 5번노드 -> 5번과 연결된 부모노드 3과 연결된 노드 4
  6 : [7],       # (0,6) 6번노드 -> 6번과 연결된 부모노드 7
  7 : [2, 6, 8], # (0,7) 7번노드 -> 7번과 연결된 부모노드 2와 자식 6,8
  8 : [1, 7]     # (0,8) 8번노드 -> 8번과 연결된 root 1과 부모 7
}


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
'''





'''
기본 BFS 문제
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = {
  1 : [2, 3, 8],
  2 : [1, 7],
  3 : [1, 4, 5],
  4 : [3, 5],
  5 : [3, 4],
  6 : [7],
  7 : [2, 6, 8],
  8 : [1, 7]
}

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
'''