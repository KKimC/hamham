# 백준 2435번 기상청 인턴 신현수

# idea
# 배열을 반복해주면서 큰값이 나타나면 갱신해준다.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = -1000000

for i in range(m, len(arr) + 1):
    answer = max(answer, sum(arr[i - m: i]))

print(answer)
