# 백준 2606번 바이러스

# idea
# dfs를 통해 간선의 갯수를 구해준다.
# 양방향이기 때문에 간선을 추가해줄 때 주의해서 추가한다.

import sys

input = sys.stdin.readline


def dfs(node, visited=[]):
    visited.append(node)

    for i in arr[node]:
        if not i in visited:
            visited = dfs(i, visited)
    return visited


arr = [[] for i in range(int(input()) + 1)]
count = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

print(len(dfs(1, visited=[])) - 1)
