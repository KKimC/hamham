#백준 1966번 프린터 큐

#idea
#dqeue을 만들어서 list를 만든 뒤 target을 맥스 값을 지정해 놓는다.
#while 문으로 m이 -1보다 큰 동안 반복되게 한뒤 1부터 num 길이 반복문
#num0이 num보다 작으면 num을 rotate
#for 문이 끝나면 answer+=1
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    num=deque(list(map(int,input().split())))
    target=max(num)
    answer=0
    while m>-1:
        for i in range(1,len(num)):
            if num[0]<num[i]:
                num.append(num.popleft())
                m-=1
                if m==-1:
                    m=len(num)-1
                break
        else:
            num.popleft()
            m-=1
            answer+=1
    print(answer)