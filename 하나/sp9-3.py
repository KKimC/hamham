# 플로이드 워셜 알고리즘 소스코드
# 방법:
# 노드->노드 모든 경우를 2차원 리스트로 만들어 최단거리를 저장한다.
# A->B 바로 가는 비용을 저장하고 1번 노드부터 N노드 까지 A->N + N->B 와 A->B 비교 작으면 교체 
 
INF = int(1e9)

# 노드 개수, 간선 개수 
n = int(input())
m = int(input())

# 2차원 리스트 무한대로 초기화 
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보 받기 
for _ in range(m):
    # a -> b 바로 가는 비용은 c
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 플로이드 워셜 : 각노드(k)를 거쳐서 가는 비용 vs a->b 바로 가는 비용
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 출력 
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print('무한', end=' ')
        else:
            print(graph[a][b], end = ' ')
    print()