#백준 2839번 설탕 배달

#idea
#n을 입력받고 answer를 만든다
#while문으로 n에서 3씩 빼가면서 answer+=1 뺄 때마다 n%5==0이 되는지 체크하고 되면 answer+(n//5).
#끝까지 가서 3으로 빼져서 0이 되면 answer출력 안되면 -1 출력

n=int(input())
answer=0

while n>0:
    if n%5==0:
        print(answer+(n//5))
        break
    answer+=1
    n-=3
else:
    if n==0:
        print(answer)
    else:
        print(-1)