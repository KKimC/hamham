# 백준 1476번 날짜 계산

# idea
# num을 1씩 더해가며 조건에 부합하는지 확인한다.

E, S, M = map(int, input().split())
num = max(E, S, M)

while (num - E) % 15 != 0 or (num - S) % 28 != 0 or (num - M) % 19 != 0:
    num+=1

print(num)
