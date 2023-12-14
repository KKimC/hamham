# 백준 15988번 1, 2, 3 더하기 3

# idea
# dp 테이블을 만들어 값들을 저장하고 꺼내어 사용한다.
# dp 테이블에는 방법 수를 저장한다.


dp=[0,1,2,4] + [0] * 999999

for i in range(4,len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
for _ in range(int(input())):
    print(dp[int(input())])

