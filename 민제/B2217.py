#백준 2217번 로프

#idea
#중량을 드는 데에 사용되는 로프들의 최솟값 * 중량을 드는 데에 사용된 로프의 갯수가 로프가 들어올릴 수 있는 최댓값이 된다.
#수를 받을 때마다 받은 수를 더 하고 갯수만큼 나누고 최댓값 사용
#아니지 그렇게 하지말고 리스트 다 받은다음 정렬하고 반복문 [-1]부터 시작해서 max(이전에 리스트 더한거/i-1,현재 수까지 더한거/i)

import sys

input=sys.stdin.readline

arr=[]
answer=0
temp=0
temp_sum=0

for _ in range(int(input())):
    arr.append(int(input()))

arr.sort()

for i in range(len(arr)):
    temp=arr[-i-1]*(i+1)
    answer=max(answer,temp)

print(answer)