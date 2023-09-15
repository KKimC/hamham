# 손님이 요청한 길이M을 얻기 위한 절단기의 최댓값구하시오!!!
# 파라메트라서치 문제: 원하는 조건을 만족하는 알맞은값 구하는 문제에서 파라메트라서치이용(<-이진탐색 - 반복문이용)

# 해결 방법: 이진 탐색
# 0부터 최대 떡길이를 첫점, 끝점으로 하여 중간점 절단시 길이를 비교한다.
# 잘린 떡양이 주어진 값과 동일 한 경우 중간값이 절단기의 최대값이 된다.

# 떡 갯수 N, 손님 요청 떡길이M
n,m = list(map(int,input().split()))
# 개별 떡길이 
array = list(map(int,input().split()))

# 이진탐색을 위한 시작점과 끝점(최고 떡길이) 설정 
start = 0
end = max(array)

# 이진 탐색 수행(반복문이용:떡볶이 양에 따라서 자를 위치 결정해야하니 재귀적은 귀찮은 방법)
result = 0
while start<=end:
    # 잘린 떡양 
    total = 0 
    mid = (start+end)//2
    for x in array:
        # 각 떡마다 잘랐을때 떡양 계산(중간값보다 작은 떡은 total에 포함되지 않는다)
        if x > mid:
            total += x - mid
    # 떡양이 부족한 경우 왼쪽이동 
    if total < m:
        end = mid-1
    # 떡양이 충분한 경우 오른쪽 탐색 
    else:
        result = mid
        start = mid+1

print(result)