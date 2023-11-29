# 백준 14501번 퇴사

# idea
# dynamic programming을 사용하여 반복문으로 bottom-up 방식을 사용하여 풀이한다.
# 현재 날짜애서 상담기간을 더한 기간이 마지막 날짜를 넘지않는 경우에만 고려해준다.
# 상담이 끝난 배열에서 상담이 끝난 배열의 값과 현재 배열의 값 + 상담 비용의 값 중 큰 것을 배열에 넣어준다.
# 상담을 하지 않았을 때도 고려하여 그 다음 날에 dp 테이블을 완성시켜준다,

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    if i + arr[i][0] <= n:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])
