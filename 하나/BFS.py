# BFS 예제 
from collections import deque

#bfs 메소드 정의 
def bfs(graph,start,visited):
    # 큐 구현 위한 deque라이브러리 사용 
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start]= True
    # 큐 빌때 까지 계속 
    while queue:
        #큐에서 하나의 원소 뽑아 출력 
        v = queue.popleft()
        print(v, end=' ')
        # 방문되지 않고 해당원소에 연결왼 원소를 큐에 삽입 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문한 정보를 리스트 자료형으로(1차원 리스트)
visited = [False]*9

# 정의된 BFS함수 호출
bfs(graph,1,visited)
