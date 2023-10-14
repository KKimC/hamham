#백준 1057번 토너먼트

#idea
#현재 라운드 번호에서 n//2+(n%2)를 하면 다음 라운드에서 받을 번호를 알 수 있다.
#다음 라운드에서 만나려면 둘의 차가 1이며 둘 중에 큰 번호가 짝수가 되어야하므로 나머지 연산으로 검증할 수 있다.

n,a,b= map(int,input().split())
answer=1

while True:
    ma=max(a,b)
    mi=min(a,b)
    if ma%2==0 and ma-mi==1:
        break
    a = a//2+(a%2)
    b= b//2+(b%2)
    answer+=1
print(answer)