# 백준 1246번 온라인 판매

# idea
# 빈 deque을 한 개 만들고 입력받은 list를 정렬한다.
# 만약 달걀 갯수가 사람보다 적으면 입력 배열을 뒤에서부터 달걀갯수만큼 잘라준다.
# (배열 길이 - i) * arr[i] 를 비교하며 최대값을 갱신해준다.


n,m = map(int,input().split())
arr = []
sum_num = [0,0]

for i in range(m):
    arr.append(int(input()))

arr.sort()

if n<m:
    arr=arr[m-n:]

for i in range(len(arr)):
    if (len(arr)-i) * arr[i] > sum_num[1]:
        sum_num[0] = arr[i]
        sum_num[1] = (len(arr)-i) * arr[i]

print(sum_num[0], end = ' ')
print(sum_num[1])


