# 문제 요약
# N가지의 화폐를 M원이 되도록 하는 최소한의 개수

# 해결방법:
# 화폐단위를 0원부터 M원까지 금액-화폐단위 값(화폐 최소 갯수)이 존재하는지 확인: 무한대가 아닌경우
#(존재하면 주어진화폐단위들로 만들수 있는 금액)
# 값이 존재한다면 +1 해준다 (이전 값에서 화폐단위를 더한게 지금의 금액이기 떄문)
# 모든 화폐단위에 대해 가장 작은 갯수를 저장해준다. 

# n,m 입력 받기 
n,m = map(int,input().split())

# 화폐 정보 
array = []
for i in range(n):
    array.append(int(input()))

# dp 테이블:  왜 10001?
# 특정 금액을 만들수 있는 화폐구성이 가능하지 않다는 의미: M의 최대값을 넘으니까 => 10000보다 큰 수 다 가능
# 각 인덱스를 금액으로 생각: 화폐의 최소갯수를 데이터로 저장 
d = [10001] * (m+1)

# 보텀업 
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        # (i-j)원을 만드는 방법이 존재하는 경우
        # 금액(j)-확인 중인 화폐 단위(i)가 10001이 아니라는것은 화폐조합으로 만들수 있는 금액이라는 뜻 
        if d[j-array[i]] != 10001:
            # # d[j-array[i]+1] 이유: 
            # 원래값인 i는 i-k에서 k가 더해진 값이므로 화폐갯수가 1개 더 추가된다.
            # 만들었던 d[j]의 데이터는 다른 화폐를 통해 만들어진 데이터가 더 작다면 바꾼다.     
            d[j] = min(d[j],d[j-array[i]+1])

# 출력 
# 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])