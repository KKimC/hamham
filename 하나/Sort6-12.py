# A와 B배열을 K번 바꿔치기 해서 A배열의 합이 최대가 되게 만들자
# a는 오름차순, b는 내림차순으로 정렬하여 최솟값과 최댓값 바꿔주기

# n(배열 원소갯수), k(바꿔치기 최대횟수)
n,k = map(int,input().split())

# 배열 입력받기 
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# a는 오름차순, b는 내림차순 정렬 
a = sorted(a)
b = sorted(b,reverse=True)

for i in range(k):
        # b의 원소 보다 크거나 같으면 바꾸는 의미가 없음 
        if a[i] < b[i]:
            a[i],b[i] = b[i],a[i]
        else:
            break

print(sum(a))
    
