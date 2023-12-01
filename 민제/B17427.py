# 백준 17427번 약수의 합2

# idea
# N 이하의 자연수들의 약수에서 i들은 g(N)안에 (N // i) * i개만큼 있다.

n = int(input())

print(sum((n // i) * i for i in range(1, n + 1)))