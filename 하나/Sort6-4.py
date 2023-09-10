# 퀵 정렬 예제
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    # 원소가 1개인경우 종료
    if start >= end:
        return
    # 첫 원소를 피벗으로 
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗 보다 큰 데이터 찾을 떄 까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗 보다 작은 데이터를 찾을 때 까지 반복 
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 위치 엇갈린다면(left>rihgt인 경우) 피벗과 작은 데이터 교체 
        if  left>right:
            array[right],array[pivot]=array[pivot],array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체 
        else:
            array[right],array[left]=array[left],array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에대해 각각 정렬 수행 
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)