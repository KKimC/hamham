# 손님이 주문한 부품이 모두 있는지 확인하자!: 있으면 yes 없으면 no

# 이진 탐색 소스 구현(반복문)
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]== target:
            return mid
        elif array[mid]> target:
            end = mid - 1 
        else:
            start = mid + 1 
    return None


# 부품 정보 입력 받기: 정렬도 미리해주기=> 이진탐색 해야되유
n = int(input())
array = list(map(int,input().split()))
array.sort()

# 회원이 원하는 부품 정보 받기 
m = int(input())
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호 하나씩 확인 
for i in x:
    result = binary_search(array,i,0,n-1)
    if result == None:
        print('no' ,end=' ')
    else:
         print('yes' ,end=' ')


