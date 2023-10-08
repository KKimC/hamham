#백준 11279번 최대 힙

#idea
#heapq을 구현하여 heappush함수를 통하여 튜플로 (-입력값,입력값)를 넣고
# heappop 함수를 통하여 튜플[0]인 음수의 최솟값을 빼준 뒤 제거하고 튜플[1] 값을 출력해주면 최대값이 출력된다.

import heapq
import sys

input=sys.stdin.readline
heap=[]

for i in range(int(input())):
    n=int(input())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            m=heapq.heappop(heap)
            print(m[1])
    else:
        heapq.heappush(heap, (-n,n))