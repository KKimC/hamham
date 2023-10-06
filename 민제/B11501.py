#백준 11501번 주식

#idea
#우선 10000*[0]의 빈배열을 만든다.
#입력받은 수열을 인덱스로 빈배열에 +=1씩 한다. 이를 인덱스 배열이라 한다.
#인덱스 배열을 0이면 pop하고 0이상이면 인덱스값을 max값으로 두어 진행 ---1번
#입력받은 수열을 반복하며 수가 max값이랑 같아질 때 까지 answer+=max-현재값을 해준다.
#현재 수가 max값이랑 같으면 인덱스 배열[max]-=1하고 다시 1번 진행 후 반복

import sys

input=sys.stdin.readline

def max_find():
    while index_arr[-1]==0:
        index_arr.pop()
        if len(arr) == 0: break
    return len(index_arr)-1

for _ in range(int(input())):
    answer = 0
    index_arr = [0] * 10001
    n=int(input())
    arr=list(map(int,input().split()))
    for i in arr:
        index_arr[i]+=1
    max = max_find()
    for i in range(0,len(arr)-1):
        index_arr[arr[i]] -= 1
        if max == arr[i]:
            max = max_find()
        else:
            answer+=max-arr[i]
    print(answer)