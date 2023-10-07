#백준 1927번 최소 힙

#idea
#heapq을 구현하여 heappush함수를 통하여 변수를 넣고 heappop 함수를 통하여 최소값을 출력후 제거한다.

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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)
