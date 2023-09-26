#백준 1676번 팩토리얼 0의 갯수

#idea
#우선 입력받은 수의 팩토리얼을 구하고 그 수의 10을 나눈 나머지가 0일 때동안 while문으로 반복시키면서 answer+=1을 해준다

num=int(input())
fac=1
answer=0
for i in range(num,0,-1):
    fac*=i
while fac%10==0:
    if fac<10:
        break
    answer+=1
    fac//=10
print(answer)