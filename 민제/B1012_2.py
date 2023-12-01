# 백준 1012번 유기농 배추

# bfs를 통해 구현

import sys
from collections import deque

input = sys.stdin.readline


def bfs(arr, x, y):
    q = deque()
    q.append([x,y])

    while q:
        save = q.popleft()  # [x,y]
        if save[0] == -1 or save[1] == -1 or save[0] == len(arr[0]) or save[1] == len(arr): continue
        if arr[save[1]][save[0]] == 0: continue

        arr[save[1]][save[0]] = 0
        q.append([save[0] - 1, save[1]])  # -1,0
        q.append([save[0] + 1, save[1]])  # 1,0
        q.append([save[0], save[1] - 1])  # 0,-1
        q.append([save[0], save[1] + 1])  # 0,1


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = [[0 for j in range(n+1)] for i in range(m+1)]
    count = 0

    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
                bfs(arr, j, i)
    print(count)