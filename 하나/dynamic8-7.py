# 문제 요약:
# 가로길이가 N, 세로길이가 2인 바닥을 1x2, 2X1, 2X2의 덮개로 덮을떄 모든 경우의 수%796796?

# 해결 방법: 
# 현재를 기준으로 i-1까지 채워져있다면 남은 부분을 채우는 경우의수는 1가지 : 2x1 사용
# 현재를 기준으로 i-2까지 채워져있다면 남은 부분을 채우는 경우의수는 2가지 : 1x2 2개 사용 or 2x2 사용 
# 각 경우의 수를 저장해두고 활용

# N을 입력받는다. 
n = int(input())

# dp테이블 초기화 
d = [0] * 10001

# 보텀업 
# 가로 길이가 1인 경우: 2x1만 가능 d[1] = 1
# 가로 길이가 1인 경우: 2x1 2개, 1x2 2개, 2x2 1개 가능 d[1] = 3
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    # 796796을 나누라 하는 이유는 단순히 값을 줄이기 위해서임 
    d[i] = (d[i-1]+ 2*d[i-2]) % 796796

# 출력 
print(d[n])
