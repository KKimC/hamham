# 계수 정렬 예제 

# 모든 원소가 0보다 크거나 같다고 가정 
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위의 데이터를 포함하는 리스트를 선언: 0으로 초기화
count = [0] * (max(array)+1)

# 각 데이터에 해당하는 인덱스 값 증가 
for i in range(len(array)):
    count[array[i]] +=1 

# count의 인덱스 출력: 정렬 완료 
for i in range (len(count)):
    # 데이터 값 만큼 반복해서 출력 
    for j in range(count[i]):
        print(i, end=' ')