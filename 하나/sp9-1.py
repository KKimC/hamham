# 간단한 다익스트라 알고리즘 소스코드 
# 방법 :
# 방문하지 않은 노드, 현재 저장된 최단 거리중 가장 짧은 노드를 선택한다. 
# 연결된 노드 사이의 거리+ 저장된 데이터가 기존 데이터 보다 짧다면 새롭게 데이터에 저장 
# 반복후 전체 데이터 출력 

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
# 방문 확인용 
visited = [False]*(n+1)
# 최단 거리 테이블 무한대로 초기화 
distance = [INF] * (n+1)

# 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

#디익스트라 수행할 함수 
def dijkstra(start):
    # 시작노드의 최단거리데이터,방문여부 초기화 
    distance[start] = 0
    visited[start] = True
    # 시작노드와 연결된 노드들을 distance의 인덱스로
    # 거리들을 데이터 값으로 받기 
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복 
    for i in range(n-1):
        # distance에 저장된 최단거리중 가장 작은 노드를 꺼내고, 방문처리
        now = get_smallest_node()
        visited[now]=True

        # 현재노드와 연결된 다른 노드 확인 
        for j in graph[now]:
            cost = distance[now]+j[1]
            # 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
            if cost<distance[j[0]]:
                distance[j[0]]=cost

# 알고리즘 수행 
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    # 도달 할 수 없는 경우 무한으로 출력 
    if distance[i]==INF:
        print('무한')
    else:
        print(distance[i])
