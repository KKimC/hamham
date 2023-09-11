# 퀵 정렬 예제2 
array = [5,7,9,0,3,1,6,2,4,8]

# 퀵정렬 함수 만들기 
def quick_sort(array):
    # 원소 1개 이하 남으면 종료 
    if len(array) <= 1:
        return array
    
    # 피벗
    pivot = array[0]
    # 피벗 제외한 모든 리스트 
    tail = array[1:]

    # 왼쪽(피벗보다 작은 원소들의 리스트), 오른쪽 (피벗보다 큰 원소들의 리스트)
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    # 왼쪽 오른쪽 정렬 수행, 전체 리스트 반환 
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))