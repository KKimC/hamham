# 삽입 정렬 예제
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    # i번째에서 0번째까지 -1씩 인덱스 감소
    for j in range(i,0,-1):
        if array[j] < array[j-1]:          
            # 지금 인덱스가 작다면 앞의 인덱스와 자리바꾸기 반복: 앞으로 땡기기 
            array[j],array[j-1] = array[j-1],array[j]
        else:
            # 지금 인덱스가 더 크다면 전진 끝!
            break
print(array)
