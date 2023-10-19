#백준

#idea
#배열을 정렬하여 반복해주고 현재 뱀길이보다 작으면 뱀길이 +=1을 해준다.

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
for i in arr:
    if i<=m:m+=1
    else:break
print(m)