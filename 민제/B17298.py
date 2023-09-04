# 백준 오큰수 17298번

# idea
# deque애 수열 담은 후 popleft()로 하나씩 수를 꺼냄
    # for 문으로 n만큼 반복한 후 deque의 0번 배열부터 차례차례 비교해서 크면 출력 후 break
        # n의 최댓값 100만이므로 최악의 경우 50만 * 50만 = 2500만 -> 시간제한 1초라서 시간초과
    #popleft()로 꺼내어 num으로 선언, for 문으로 반복 후 num과 비교하여 큰 수를 찾으면 그 사이의 수들은 다 큰 수로 출력하면 됨
        #while arr : target=arr.popleft()으로 숫자 한 개씩 꺼내주고 while 중첩문으로 arr 한 개씩 꺼내준 다음 비교하여
        #target보다 작으면 i+=1, 크면 i만큼 큰 수 반복 arr사라지면 i만큼 -1 프린트
# list에 수열을 담고 빈 deque을 생성
    # 뒤에서부터 list를 돌아서 뒷 수가 바로 앞 수보다 크면 뒷 수 deque

import sys

input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
answer=[0]*n
li=[] #index를 담음

for i in range(n):
    while li and arr[li[-1]] < arr[i]:
        answer[li.pop()] = arr[i]
    li.append(i)
        
while li:
    answer[li.pop()] = -1

for i in answer : print(i,end=' ')

#python3 1280ms pypy3 648ms