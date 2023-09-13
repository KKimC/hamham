# 반복문을 이용한 이진탐색 

# 이진탐색 소스구현
def binary_search(array,target,start,end):
    while start<=end:
        # 중간값 지정 
        mid = (start+end)//2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid]==target:
            return mid
        # 중간값 이후 확인 할 필요 없으니 중간값-1을 마지막점으로 
        elif array[mid]>target:
            end = mid - 1
        # 중간값 이전 확인 할 필요 없으니 중간값+1을 시작점으로 
        else:
            start = mid + 1 
    
    return None

# 입력받기
n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

# 결과 출력 
result = binary_search(array,target,0,n-1)
if result == None:
    print('원소가 존재하지 않습니당')
else:
    print(result+1)