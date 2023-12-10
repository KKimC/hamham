# 백준 2485번 가로수
# idea
# 가로등 간경들의 최대 공약수들을 구해주면 간격들이 같아질 최소 간격을 알 수 있다.
# 간격에서 최대공약수를 나누고 1을 빼주면 심어야하는 가로수 갯수가 나온다!

import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
temp1 = int(input())
temp2 = int(input())
arr = [temp2 - temp1]
g = temp2 - temp1
temp1 = temp2
answer = 0

for _ in range(n - 2):
    temp2 = int(input())
    arr.append(temp2 - temp1)
    g = gcd(g, temp2 - temp1)
    temp1 = temp2

for i in arr:
    answer += i // g - 1

print(answer)
