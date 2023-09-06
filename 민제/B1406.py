#백준 1406번 에디터

#idea
#left와 right라는 list를 만들어서 left에는 전체 문자열을 받는다 (left[-1]과 right[0]사이가 커서의 위치가 된다)
    # L : right에 left[-1]을 append
    # D : left에 right[-1]을 append
    # B : left[-1]를 pop
    # P : P 뒤에 문자를 left에 append

import sys

input=sys.stdin.readline

left=list(input().rstrip())
right=[]
for _ in range(int(input())):
    arr=input().split()
    if arr[0]=='L' and left:
        right.append(left.pop())
    elif arr[0]=='D' and right:
        left.append(right.pop())
    elif arr[0]=='B' and left:
        left.pop()
    elif arr[0]=='P':
        left.append(arr[1])

print("".join(left), end="")
print("".join(right[::-1]))