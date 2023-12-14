# 3-2 책의 풀이로 풀어보기 

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort() # sort 랑 sorted 의 차이점? sort는 원본 값이 바뀌고(그래서 정렬값 반환X=>None) sorted는 원본은 그대로 정렬값 반환
first = data[n-1]
second = data[n-2]

result = 0 

while True:
    for i in range(k): # 큰수를 k번(최대한 더할수 있는 갯수) 더하는 작업
        if m == 0: # m을 -1씩 빼며 m번 더할 수 있게 할거임(m=0되면 끝)
            break
        result += first
        m -= 1

    if m == 0: # 큰수를 k번 더한 후 두번째 큰수를 한번 더하는 작업 
        break
    result += second
    m -= 1 

print(result)

# sort와 sorted 차이 확인하기 
# list1 = [2,7,1]
# list2 = [6,1,3,0]

# list3 = list1.sort()
# list4 = sorted(list2)

# print(list1)
# print(list2)
# print(list3)
# print(list4)

