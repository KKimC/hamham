# 내림차 순 정렬 

# 갯수 입력 받기 
n = int(input())

# 데이터 입력 받기 
array = []
for i in range(n):
    array.append(int(input()))

# 파이선의 기본 정렬 라이브러리 이용: 내림차 순 
# 그냥 정렬은 sorted(array)
array = sorted(array,reverse=True)

# 출력 
for i in array:
    print(i, end=' ')