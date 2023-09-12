# 순차 탐색 예제 
# dolpin을 찾자

# 순차 탐색 소스코드 구현
def sequential_serch(n,target,array):
    # 각원소를 하나씩 확인 
    for i in range(n):
        # 현재 원소가 찾는 원소와 동일 한 경우 
        if array[i]==target:
            # 현재 위치 반환 
            return i+1

# 원소갯수, 찾을 문자열 입력 받기 
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

# 데이터 입력 받기
array = input().split() 

# 결과 
print(sequential_serch(n,target,array))