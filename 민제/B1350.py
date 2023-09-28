#백준 1350번 진짜 공간

# idea
# num=0을 초기화하고 리스트에 수를 넣는다.
# 리스트에 수를 하나씩 꺼내어 0이면 continue 0이상이면 //클러스 크기 +1 해준뒤 num에 더해준다.
# 마지막에 num * 클러스터 크기를 해준다.

n=int(input())
arr=list(map(int,input().split()))
clu=int(input())
num=0

for i in arr:
    if i == 0 : continue
    else:
        if i % clu == 0 :
            num += i // clu
        else :
            num += i // clu + 1
print(num*clu)