# 이진 탐색: 재귀함수 이용 
# 중간점과 타겟 크기비교에따라 다른 리턴 값(중간값 반환 or 분할된 부분 재탐색: 재귀함수)을 통해 타겟을 찾는다.

def binary_search(array,target,start,end):
    if start > end:
        return None
    # 중간값 정수 부분만 반환 
    mid = (start+end)//2 
    
    # 찾은 경우 중간점 인덱스 반환 
    if array[mid]== target:
        return mid
    # 중간점이 더 큰경우 왼쪽 부분 확인
    elif array[mid]> target:
        return binary_search(array,target,start,mid-1)
    # 중간점이 더 작은 경우 오른쪽 부분 확인 
    else:
        return binary_search(array,target,start+1,end)

# 원소의 갯수와 target입력받기 
n, target =list(map(int,input().split()))

# 전체 원소 입력 받기 
array = list(map(int,input().split()))

# 이진 탐색 수행결과 
result = binary_search(array,target,0,n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)