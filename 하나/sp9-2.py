# 개선된 다익스트라 알고리즘 코드 
# 우선 순위 큐를 이용하여 현재 노드에서 가장 가까운 노드를 받게된다
# get_smallest_node()의 개선판 
# 나머지는 유사하다.

#PriorityQueue보다는 heapq를 이용
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수, 간선의 개수 입력받기 
n,m = map(int,input().split())
# 시작 노드 
start = int(input())
# 노드 정보 리스트 
graph=[[] for i in range(n+1)] # n+1로 리스트 만들어서 인덱스=노드
for _ in range(m):
    # a->b 가 c거리라는 뜻 
    a,b,c = map(int,input().split())
    # a 노드에 대한 정보(연결 노드, 거리)
    graph[a].append((b,c))
# 최단 거리 테이블 무한대로 초기화 
distance = [INF] * (n+1)

# 다익스트라 
def dijkstra(start):
    q = []
    # 우선순위 큐에 (거리,노드)넣기
    # 시작 노드를 가기 위한 최단 경로는 0으로 설정하여(자기자신이니까), 큐에 삽입 
    heapq.heappush(q,(0,start))
    distance[start]=0
   # 큐가 비어있지 않다면
    while q:
        #최단 거리가 가장 짧은 노드에 대한 정보 꺼내기 
        dist,now = heapq.heappop(q)
        # 이미 처리된적 있는 노드라면 무시 
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인 
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐서, 다른노드로 이동하는 거리가 더 짧은 경우
            # 교체하고 우선순위 큐에 넣기 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 알고리즘 수행 
dijkstra(start)

# 출력 
for i in range(1,n+1):
    if distance[i] == INF:
        print('무한')
    else:
        print(distance[i])