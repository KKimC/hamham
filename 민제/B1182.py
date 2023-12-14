# 백준 1182번 부분 수열의 합

# idea
# 우선 정수의 갯수 최대 20개
# 여기서 배열 조합의 수를 구하면 (20C2 ~ 20C10) * 2개 대애충 계산때려보 100만개
# 이거? 조합으로 경우의 수 다 구해도 되겠다~
# 488ms... 더 생각해보자..

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer=0

for i in range(1, n + 1):
    comb = list(combinations(arr, i))
    for i in comb:
        if sum(i) == m:
            answer+=1
print(answer)

