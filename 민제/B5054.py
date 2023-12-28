# 백준 5054번 주차의 신

# idea
# 리스트를 반복하여 리스트의 두 개씩 차를 구하여 더해준다.
# 합을 두 배로 하여 출력한다.

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    int(input())
    arr = sorted(list(map(int,input().split())))
    sum = 0

    for i in range(1,len(arr)):
        sum += arr[i] - arr[i-1]

    print(sum * 2)