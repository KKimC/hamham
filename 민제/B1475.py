#백준 1495번 방 번호

#idea
#1~9까지 배열을 만들고 수열을 하나씩 받아 인덱스에 +=1씩 해준다.
#6과 9를 비교해 6과 9의 차//2만큼 큰쪽은 빼주고 작은쪽에 더해준다.
#list에서 가장 큰값 출력

import sys

arr=[0]*10
n=sys.stdin.readline().rstrip()

for i in n:
    arr[int(i)]+=1
if (arr[6]+arr[9])%2==0:
    arr[6]=(arr[6]+arr[9])//2
    arr[9] = 0
else:
    arr[6] = (arr[6] + arr[9]) // 2
    arr[9] = arr[6] + 1
print(max(arr))
