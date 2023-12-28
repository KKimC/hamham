# 백준 14647번 준오는 조류혐오야!!

#idea
#판의 9의 개수를 구한다.
# 한줄씩 차례차례 탐색하며 9의 최대 갯수을 찾아준다.
# 두 개를 빼준다.

n,m=map(int,input().split())
total=0
nine=0
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))

for i in range(len(arr)):
    temp = 0
    for j in range(len(arr[i])):
        temp += arr[i][j].count('9')
        total += arr[i][j].count('9')
    nine = max(nine, temp)


for i in range(len(arr[0])):
    temp = 0
    for j in range(len(arr)):
        temp += arr[j][i].count('9')
    nine = max(nine,temp)

print(total - nine)