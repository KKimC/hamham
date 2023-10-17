#백준 1302번 베스트셀러

#idea
#dictoinary에 dict[input]+=1형태로 받아준다.
#dict를 key를 기준으로 정렬하고 max값을 찾아준다.

import sys

di=dict()

for i in range(int(input())):
    n=sys.stdin.readline().rstrip()
    if not n in di:
        di[n]=1
    else:
        di[n]+=1
di = dict(sorted(di.items(), key = lambda item: item[0]))
print(max(di,key=di.get))