# 문제 요약:
# 1->K->N 최소시간? 양방향가능, 건물간 시간은 1

# 해결 방법:
# 1번 노드 -> K -> 목적지 노드 = (1->K 최단시간)+ (K->목적지 최단시간)
INF = int(1e9)

# 노드 개수, 간선 개수 
n = int(input())
m = int(input())

# 2차원 리스트 무한대로 초기화 
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기자신으로 가는 비용은 0이다
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보 받기 
for _ in range(m):
    # a -> b 가는 비용은 1, 양방향 가능
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x와 최종 목적지 K 받기 
x,k = map(int,input().split())

# 플로이드 워셜 
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 출력:1번 노드 -> K -> 목적지 노드 = (1->K 최단시간)+ (K->목적지 최단시간)
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
