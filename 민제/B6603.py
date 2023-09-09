#백준 6603번 로또

#idea
#while문을 돌려 list를 받고 0을 받으면 종료되도록 len(list)==1이 되면 break
#list에서 배열의 길이인 list[0]을 슬라이스로 제거(combinations)를 쓸거니까 deque로 popleft 사용x
#for문으로 combinations(list,6)으로 list를 조합하여 중복없이 6개가 되는 모든 경우의 수 출력

import sys
import itertools

input = sys.stdin.readline

while True:
    li=list(map(str,input().split()))
    if len(li)==1:break
    li=li[1:]
    for i in itertools.combinations(li,6):
        print(' '.join(i))
    print()