# 백준 16466번 콘서트

# 리스트를 받아 처음부터 반복한다.
# 인덱스와 요소가 다른 인덱스의 번호를 출력한다.

import sys

input()
arr = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(len(arr)):
    if arr[i] != i + 1:
        print(i + 1)
        exit()
print(len(arr) + 1)
