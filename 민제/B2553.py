#백준 2533번 마지막 팩토리얼 수

#idea
#int는 20000!의 수를 다 표현할 수 없기 때문에 나머지연산으로 수를 적당하게 남겨 곱해준다.
#끝자리가 0이라면 나누기 연산을 통해 끝을 잘라준다.

answer=1
n=int(input())

for i in range(1,n+1):
    answer*=i
    temp=answer%10000000
    while temp%10==0:
        temp//=10
    answer=temp

print(answer%10)