#백준 11399번 ATM

#idea
#시간이 짧게 걸리는 사람부터 먼저 하면 최대 효율의 시간을 도출할 수 있음.
#i번 사람의 인출 시간을 input으로 받음
#가장 작은 수부터 n-i+1만큼 곱해서 더해주면 됨
#test case -> n=5 arr=[3,1,4,3,2]
#(1*5)+(2*4)+(3*3)+(3*2)+(4*1)=32 -> 최대 효율의 시간
    # 1번. dynamic programming으로 각 인원의 걸리는 시간의 갯수를 체크한 다음 for문을 역으로 써서 곱해줌
    # 2번. arr을 sort한 다음 곱해줌

import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
answer=0

arr.sort()

for i in range(1,n+1):
    answer+=arr.pop()*i

print(answer)