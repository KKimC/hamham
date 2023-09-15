# 계수 정렬을 이용한 풀이:
# 최대값과 최소값 차이만큼의 데이터를 가진 리스트를 만들어(0으로 초기화)
# 가게 제품과 같은 인덱스의 데이터를 1로 바꾼다.
# 고객요청 제품과 같은 인덱스의 데이터가 1이라면 yes 아니면 no


# 제품 갯수 입력 받기 
n=int(input())
# 최소값 최댓값의 차이만큼 리스트 만들어주기 
array=[0]*1000001

# 가게에 있는 제품 부품 번호를 입력받아 기록 : array[제품]=1 해주기
for i in input().split():
    array[int(i)]=1

# 손님이 요청하는 제품 정보 
m = int(input())
x = list(map(int,input().split()))

# 확인하기 
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ') 