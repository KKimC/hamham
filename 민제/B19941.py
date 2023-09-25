#백준 19941번 햄버거 분배

#idea
#배열에 순서대로 저장한다
#한개씩 빼서 햄버거와 사람의 인덱스를 배열로 따로 저장한다.
#사람의 인덱스를 한개씩 꺼내 햄버거의 배열과 비교하여 차례차례 비교하여 사람 인덱스 +- k 범위의 햄버거 인덱스가 있으면 햄버거 인덱스와 사람 인덱스 삭제 후 answer+=1

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
st = str(input().rstrip())
burger = deque()
people = deque()
b = 0
answer = 0

for i in range(len(st)):
    if st[i] == 'H':
        burger.append(i)
    else:
        people.append(i)
p = people.popleft()
b = burger.popleft()
while people:
    if p - k > b:
        b = burger.popleft()
    elif p + k < b:
        p = people.popleft()
    if p - k <= b and p + k >= b:
        answer += 1
        if not burger:
            b=10000
            break
        b = burger.popleft()
        p = people.popleft()
while burger:
    b=burger.popleft()
    if p - k <= b and p + k >= b:
        b=0
        p=1000
        answer += 1
        break
if p - k <= b and p + k >= b and not burger and not people:
    answer += 1
print(answer)