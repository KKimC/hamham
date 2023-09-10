#백준 2669번 직사각형 네개의 합집합의 면적 구하기

#idea
#100*100 배열을 만들어 0으로 저장
#for문으로 x1,y1,x2,y2를 받은뒤 arr[x1~x2][y1~y2]=1 -> 사각형이 있는 곳이 1로 저장됨
#arr[x1~x2][y1~y2]==1일 때 answer+=1
#최대 시간복잡도 100*100*2 = 20000

#수정
#sum(map(sum,arr))을 쓰면 2차원 배열의 합을 깔끔하게 표현할 수 있음
#시간복잡도나 공간복잡도의 변화는 없음

import sys

input = sys.stdin.readline

arr = [[0 for _ in range(101)] for _ in range(101)]
answer=0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1
print(sum(map(sum,arr)))
