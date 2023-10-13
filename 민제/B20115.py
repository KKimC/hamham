#백준 20115번 에너지 드링크

#idea
# answer=0으로 초기화해준다.
# 수열을 list로 받아주고 list값의 최대값을 찾아준다.
# 가장 많은 에너지 드링크에 나머지 에너지 드링크를 다 부어주면 된다.
# for문으로 arr을 반복해준 뒤 i==최댓값이라면 그대로 answer에 추가해주고 최대값을 0으로 초기화해준다.
# 최대값을 0으로 초기화해준 이유는 최대값의 중복이 있을 때 다 그대로 더하면 안되기 때문이다.
# i==최댓값이 아니라면 i/2를 해준 뒤 출력해준다.
# answer-int(answer)가 0이라면 int로 변환 뒤 출력해주고 0이 아니라면 그대로 출력한다.

import sys

int(input())
arr=list(map(int,sys.stdin.readline().split()))
m = max(arr)
answer=0

for i in arr:
    if i==m:
        answer+=m
        m=0
        continue
    answer+=i/2
if answer-int(answer)==0:
    print(int(answer))
else:
    print(answer)