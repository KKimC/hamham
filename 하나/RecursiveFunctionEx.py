# 팩토리얼 예제: 재귀함수 이용 

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    # n이 1이하인 경우 1을 반환
    if n <=1:
        return 1
    #n! = n * (n-1)!을 코드로 작성하기
    return n*factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))