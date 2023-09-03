#백준 최솟값 찾기 11003

#idea
    # 1번. deque을 사용하여 popleft로 값을 하나씩 빼주고 min을 사용하여 출력 -> min 시간복잡도 O(n)이므로 최악의 경우 5,000,000*5,000,000
    # 2번. priority queue를 사용하여 [인덱스, 값]으로 하나씩 배열을 받고 받은 배열을 자동으로 정렬하여 맨 앞의 값을 출력 -> 나쁘지 않은 듯
    # 3번. deque을 두개 만들어 1번 deque에는 처음 수들을 넣고 2번 deque에 popleft로 하나씩 넘겨줌. 그리고 인덱스와 값으로 판별 -> 이게 제일 쉬울듯

#deque을 2개 만들어 1번 deque에 수들을 넣고 popleft로 2번 deque에 [인덱스, 값]로 한 배열씩 append
#2번 deque에서 최솟값 판별
    #우선 인덱스를 비교하여 현제 append된 인덱스 - L 보다 작거나 같은 인덱스 삭제
    #append된 수와 앞의 값들과 비교하며 앞의 값이 크다면 앞의 값 삭제 후 최솟값 출력
    #뒷 수가 크다면 뒷 수는 삭제하지 않고 앞의 최솟값만 출력

import sys
from collections import deque

input = sys.stdin.readline

n,l = map(int,input().split())
d1 = list(map(int,input().split()))
d2 = deque()

for i in range(n):
    while d2 and d1[i] <= d2[-1][-1]:
        d2.pop()
    d2.append([i,d1[i]])
    if d2[0][0] < i-l+1:
        d2.popleft()
    print(d2[0][1],end=' ')

#d1을 deque으로 만들어 popleft()로 뺴서 변수 선언하여 구현했으나 50%에서 시간 초과
#d1을 list로 만들어 d1[i]로 썼으나 50%에서 시간초과
#26번줄에서 d2.append([i,d1[i]]) -> d2.append((i,d1[i]))로 튜플 형태로 바꿔주니 통과
#tuple이 list보다 빠르다고 한다..