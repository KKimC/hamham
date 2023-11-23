# 백준 14425번 문자열 집합

# idea
# 집합 자료형의 in은 시간복잡도가 O(1)이니 이를 사용한다.

n, m = map(int, input().split())

answer = 0
se = set()
arr = []

for i in range(n):
    se.add(input())

for i in range(m):
    arr.append(input())

for i in arr:
    if i in se:
        answer += 1

print(answer)
