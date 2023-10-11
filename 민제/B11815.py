#백준 11815번 짝수?홀수?

#idea
#자신에게 루트를 씌운 값이 자연수로 나오는 값은 약수의 갯수가 홀수개이다.

int(input())
arr=list(map(int,input().split()))

for i in arr:
    if int(i**0.5)**2==i:
        print(1,end=' ')
    else:
        print(0,end=' ')
