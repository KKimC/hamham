#백준 2659번 십자카드 문제

#idea
#십자수를 배열로 받고 sort한뒤 숫자로 변환
#for 1111~시계수에서 시계수의 각 자리수가 오름차순이고 0이 포합되지 않은수가 있다면 answer+=1
#각 자리가 오름차순일 때를 조건으로 추가한 이유는 1122같은 경우 2112, -> 아니 넌 틀렸어
#우선 [0]*10000의 data라는 배열을 만들고 for 1111~input 한 뒤 이중 반복문으로 arr[시계수]=1로 바꾼다
#그 다음 if로 먼저 data[시계수]가 0인지 1인지 판별해주고 1이면 continue 0이면 계속 반복문 진행으로 한다.
#answer에 카운트
#list.insert(0,list.pop())로 배열을 rotate돌리면 O(N)이지만 deque.append(deque.popleft())를 사용하면 O(1)이기 때문에 Deque 사용

from collections import deque

arr=deque(map(int,input().split()))
num=10000
data=[0]*10000
answer=0

for i in range(4):
    num=min(arr[0]*1000+arr[1]*100+arr[2]*10+arr[3],num)
    arr.append(arr.popleft())

for i in range(1111,num+1):
    #다른 수의 시계수인지 판별
    if data[i]==1:continue
    #숫자에 0이 있는지 판별
    if i%10==0:
        continue
    if i%100//10==0:
        continue
    if i%1000//100==0:
        continue
    #카운트
    answer+=1
    #현재 수의 시계수 1로 저장
    data[i]=1
    temp=deque([i//1000,i//100%10,i//10%10,i%10])
    for j in range(3):
        temp.append(temp.popleft())
        data[temp[0]*1000+temp[1]*100+temp[2]*10+temp[3]]=1

print(answer)