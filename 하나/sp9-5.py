# 문제 요약:
# C도시에서 최대한 많은 도시로 전보를 보낼 때 메세지를 받은 도시의 수와, 걸리는 시간?
# 단, 양방향이 가능할때만 전보를 보낼 수 있다.

# 풀이 방법:
# 한도시에서 다른 도시까지 최단거리 문제 => 다익스트라 알고리즘 
# N,M범위가 상당히 크므로 우선순위 큐를 이용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 도시 갯수N, 통로 갯수M, 메세지 보내는 start 입력 
n,m,start=map(int,input().split()) 

# 각노드의 관한 정보, 간선에 대한 정보
graph = [[]for i in range(n+1)]

for _ in range(m):
    # 특정도시 X -> 특정도시 Y로 이동하는 전달시간Z 입력받기 
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

# 최단거리 테이블(1차): 무한대로 초기화
distance = [INF] * (n+1)

# 다익스트라 
def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단경로는 0, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    # 큐가 비어있지 않다면
    while q:
        # 최단거리가 가장 짧은 노드 꺼내기
        dist,now=heapq.heappop(q)

        # 만약 처리된적 있는 노드면 무시 
        if distance[now] < dist:
            continue 
        # 현재 노드와 인접한 노드 확인 
        for i in graph[now]:
            cost = dist+ i[1]
            # 기존의 최단거리와 비교 후 짧으면 교체, 우선 순위 큐에 넣기
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달 할수있는 노드 갯수: count, 걸리는 시간(= 가장 멀리있는 노드와 거리): max_distance 
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count+=1
        max_distance = max(max_distance,d)
# 자기자신은 빼야하니까 count-1
print(count-1,max_distance)




   
