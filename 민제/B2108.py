#백준 2108번 통계학

#idea
# num_count=[0]*8002의 배열을 만들어준다.
# 수를 입력 받을 떄마다 음수면 양수로 바꿔서 *4000해준뒤 num_count[음수*(-1)+4000]+=1을 해주고 양수면 num+count[양수]+=1
# sum_num+=입력받은 수를 해준다.
# 그 수를 arr.append()로 arr배열에도 넣어준다.
# 입력을 다 받은 후 arr을 정렬해준다.
# 산술 평균은 round(answer//n)로 출력
# 중앙값은 arr[n//2}로 출력
# 최빈값은 max(num_count)를 구해준뒤 num_count.count(max)가 두 개 이상이 for i in num_cuont로 두 번째 max값인덱스 반환
# 한 개면 num_count.index(max)로 출력
# 범위는 arr[-1]-arr[0]으로 출력

import sys

num_count=[0] * 8000
sum_num=0
arr=[]

n=int(input())
for i in range(n):
    num=int(sys.stdin.readline())
    num_count[num+4000]+=1
    sum_num+=num
    arr.append(num)
arr.sort()
print(round(sum_num/n))
print(arr[n//2])
ma=max(num_count)
if num_count.count(ma)>1:
    count=0
    for i in range(len(num_count)):
        if num_count[i] == ma:
            count+=1
            if count==2:
                print(i-4000)
                break
else:
    ma_index = num_count.index(ma)
    print(ma_index-4000)
print(arr[-1]-arr[0])