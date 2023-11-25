#백준 11053번 가장 긴 증가하는 부분수열

#idea
#이진 탐색을 통해 현재 값과 dp테이블의 최댓값과 비교하여 값을 추가하거나 갱신한다.

import bisect

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect.bisect_left(dp, i)] = i
print(dp)
print(len(dp) - 1)
