# 출구(NxM)까지 움직여야하는 최소 칸 수: 1(괴물 없는)부분으로 이동해야
from collections import deque
# n,m입력받기
n,m = map(int,input().split())

#2차원 리스트 맵 정보 받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 방향 정의(상하좌우) 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# BFS구현 
def bfs(x,y):
    # 큐 구현
    queue = deque()
    queue.append((x,y))
    #큐 끝날때까지 반복 
    while queue:
        x,y = queue.popleft()
        # 4방향 위치 확인 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 미로 공간 벗어나면 무시 
            if nx<0 or nx>=n or ny<0 or ny>= m:
                continue
            # 벽 무시 
            if graph[nx][ny]==0:
                continue
            #처음 방문 하는 경우에만 최단거리 기록 
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 최단거리 반환
    return graph[n-1][m-1]
# bfs 수행결과 출력 
print(bfs(0,0))

