#백준 5347 LCM

# idea
# 파이썬 라이브러리 사용

import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    n,m =map(int,input().split())
    print(math.lcm(n,m))    