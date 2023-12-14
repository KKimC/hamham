# 백준 9076번 점수 집계

# idea
# 리스트를 정렬하여 첫번째와 끝 수를 제외한다.
# 위 리스트에서 마지막 수와 첫 수의 차가 4가 넘으면 KIN, 아니면 세 수의 합을 출력한다.

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))[1:4]
    if arr[-1] - arr[0] >= 4:
        print("KIN")
    else:
        print(sum(arr))