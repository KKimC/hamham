# 집합 자료형 이용: 
# 제품데이터를 set 자료형에 넣고 고객 요청 부품이 있는지 확인
# 집합 자료형은 특정 데이터가 존재하는지 검사할 때 매우 효과적 

# 부품 정보 입력 받기
n = int(input())
# 입력받은 제품을 집합(set) 자료형에 기록 
array = set(map(int,input().split()))

# 고객이 원하는 부품 정보 받기 
m = int(input())
x = list(map(int,input().split()))

# 확인하기 
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
         print('no', end=' ')