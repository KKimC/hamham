#백준 2641번 다각형 그리기

#idea
#표본 모양과 비교 모양이 같다면 표본 모양수열을 두 번 이어놓으면 비교 모양수열의 겹치는 부분이 있을 것 이다.
#반대 방향까지 고려해주면 깔ㅡㅡㅡㅡ끔
#이중 배열로 그리고 난리부르스 칠 필요가 없다
#string+string은 비효율적이므로 list로 받고 append로 추가해준다음 join해주는게 pythonic way라고 한다..

import sys

input = sys.stdin.readline

length = int(input())
stand = list(map(str,input().split()))
reverse = []

for i in range(length-1,-1,-1):#회전방향과 상하좌우를 동시에 바꿔줍니다.
    if stand[i] == '1':
        reverse.append('3')
    elif stand[i] == '2':
        reverse.append('4')
    elif stand[i] == '3':
        reverse.append('1')
    elif stand[i] == '4':
        reverse.append('2')

#표본 수열 두 번 반복하기
temp=stand+stand
stand = ' '.join(temp)
temp=reverse+reverse
reverse = ' '.join(temp)

#모양 수열 비교
answer = []
for _ in range(int(input())):
    comp = ' '.join(input().split())
    if comp in stand or comp in reverse:
        answer.append(comp)

#정답 출력
print(len(answer))
for ans in answer:
    print(ans)