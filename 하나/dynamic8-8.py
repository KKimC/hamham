# 문제 요약
# N가지의 화폐를 M원이 되도록 하는 최소한의 개수

# n,m 입력 받기 
n,m = map(int,input().split())

# 화폐 정보 
array = []
for i in range(n):
    array.append(int(input()))

# dp 테이블 
d = [10001] * (m+1)

# 보텀업 
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        # (i-k)원을 만드는 방법이 존재하는 경우
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]+1])

# 출력 
# 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])