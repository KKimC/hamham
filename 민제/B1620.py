#백준 1620번 나는야 포켓몬 마스터 이다솜

#idea
#list에 포켓몬 배열을 저장해놓고 정답 배열을 찾는다.
#n과 m의 최대 갯수는 10만이므로 index를 쓰면 최대 10만 * 10만이다.
#그러므로 dict 자료구조를 사요하여 O(1)의 시간 복잡도로 index를 찾는다.
#dict는 순서가 없으므로 안에 item에 접근하는데 O(1) 시간이 걸린다,

import sys

input = sys.stdin.readline

n,m=map(int,input().split())
arr_str=[]
dict=dict()

for i in range(n):
    a=input().rstrip()
    arr_str.append(a)
    dict[a] = i

for i in range(m):
    com = input().rstrip()
    if com[0]>='1' and com[0]<='9':
        print(arr_str[int(com)-1])
    else:
        print(dict[com]+1)