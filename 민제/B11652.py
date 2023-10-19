#백준 11652번 카드

#idea
# 빈 dictionary를 만들어준다.
# 수를 한개씩 입력받아 if dict[입력받은수]가 없다면 dict[입력받은 수]+=1을 해주고 dict[입력받은 수]=1읋 해준다.
# dict를 정렬해주고 max값을 반환해준다..

import sys

di=dict()

for i in range(int(input())):
    n=int(sys.stdin.readline())
    if not n in di:
        di[n]=1
    else:
        di[n]+=1
di = dict(sorted(di.items(), key = lambda item: item[0]))
print(max(di,key=di.get))