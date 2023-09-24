#백준 1193번 분수찾기

#idea
#배열 순서
#1 [0][0], 2 [0][1], 3 [1][0], 4 [2][0], 5[1][1],
#n에서 1,2,3,4...의 값을 뺀다5
#빼는 수의 값이 n보다 커졌으면 멈추고 배열에 넣고 y배열에는 i+1-x
#4 2 2 3
n=int(input())
i=1
x=0
y=0

while n>=i:
    n-=i
    i+=1
if n!=0:
    x=n
    y=i+1-x
else:
    x=1
    y=i-x

print(str(y) + '/' + str(x) if i%2!=0 else str(x) + '/' + str(y))