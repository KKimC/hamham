# 백준 24416번 알고리즘 수업 - 피보나치 수1

# idea
# 그냥 피보나치 수를 구현하는 메소드와 다이나믹 프로그래밍을 사용하는 메소드를 구현하여 count로 연산 횟수를 저장한다.

def fib(n):
    global count
    if n == 1 or n == 2:
        return 1
    count += 1
    return fib(n - 1) + fib(n - 2)

n = int(input())

count = 1
fib(n)
print(count, n-2)