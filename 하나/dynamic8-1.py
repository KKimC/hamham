# 피보나치 수열 : 재귀 함수 이용 
# x가 커질 수록 시간이 기하급수적으로 늘어난다는 문제!

def fibo(x):
    if x == 1 or  x == 2:
        return 1  
    return fibo(x-1)+fibo(x-2)
print(fibo(6))