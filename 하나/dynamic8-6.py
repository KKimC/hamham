# 문제 요약:
# 식량 창고 N 정보가 주어질때 인접하지 않은 창고를 약탈해서 얻을 수 있는 최대 식량?

# 식량창고 갯수 N
n = int(input())

# 식량창고 정보 
array = list(map(int,input().split()))

# dp테이블초기화 
d = [0] * 100

# 다이나믹 프로그래밍(보텀업)
d[0]=0
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])

#출력 
print(d[n-1])

