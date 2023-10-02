#백준 1940번 주몽

# idea
# 우선 n과 m을 input받고 수열을 리스트로 받는다.
# 그 list를 sort하고 i와 j로 양 끝에 포인터를 둔다.
# while i<j한 뒤그 수들을 더해서 m을 넘으면 answer+=1한 후 i+=1,j-=1
# 넘지 못하면 i+=1을 해준다.

import sys

input = sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int,input().split()))
arr.sort()
i=0
j=len(arr)-1
answer=0

if n==1:
    print(0)
    exit()
while i<j:
    if arr[i]+arr[j]==m:
        answer+=1
        i+=1
        j-=1
    elif arr[i]+arr[j]<m:
        i+=1
    else:
        j-=1
print(answer)