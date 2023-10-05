#백준 3568번 isharp

#idea
#list 공백을 기준으로 받는다.
#list[0]을 frame에 넣어놓고 list[1]부터 반복하며 arr로 받는다.
#a=arr.pop if a==*or&면 frame.append(a) 해주고 a==']'면 frame.append('[]')
#else string을 따로 만들어서 넣어줌

from collections import deque

li=list(map(str,input().split()))
if len(li)==1:
    print(li[0]+';')
for i in range(1,len(li)):
    frame = list(li[0])
    temp=list(li[i])
    temp.pop()
    s=deque()
    while len(temp) != 1:
        a=temp.pop()
        if a == '*' or a == '&':
            frame.append(a)
        elif a == ']':
            frame.append(temp.pop())
            frame.append(a)
        else:
            s.appendleft(a)
    else:
        s.appendleft(temp.pop())
        frame.append(' ')
        frame.append(''.join(s))
        frame.append(';')
    print(''.join(frame))
