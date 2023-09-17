#백준 1647번 도시 분할 계획

#idea
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4 라는 노드,간선,가중치가 주어졌을 때 그림을 그려보니 1,2,3,4,5,6번 마을과 7번 마을을 분리해야 최소가 나옴
# 최소를 구하려면 가중치를 오름차순으로 정렬하고 사이클이 없도록 모든 노드를 연결해준 뒤 마지막에 연결한 가장 큰 간선을 제거하면 최소 가중치로 마을이 2개로 분리됨
#(7번 마을은 외롭긴 하겠다..)
# 가중치를 오름차순으로 구한 뒤에 크루스칼 알고리즘을 사용하면서 유니온 파인드로 사이클이 없도록 판별해주면 끄읏!!이 날 줄 알았지만 내 구현 능력을 과대평가한 듯
#하..
#가중치들을 굳이 배열에 안넣어주고 answer에 추가해가면서 마지막거만 빼주면 공간 애낄수 있을듯

import sys

input = sys.stdin.readline

def find(i):
    if i!=arr[i]:
        arr[i]=find(arr[i])
    return arr[i]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        arr[b]=a
    else:
        arr[a]=b

n,m=map(int,input().split())
arr=[i for i in range(n+1)]
graph=[]
answer=0

for i in range(m):
    a,b,c=map(int,input().split())
    graph.append([c,a,b]) #a,b,c 순서로 해주고 sort(lambda x:x[2])써도 되지만 그냥 sort쓰는게 편할거같아서 c,a,b 순으로 넣음

graph.sort()

for c,a,b in graph:
    #싸이클 판별
    if find(a)!=find(b):
        union(a,b)
        answer+=c
        last=c
answer-=last

print(answer)
