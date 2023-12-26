# 백준 15819번 너의 핸들은

# idea
# 리스트를 정렬한 뒤 인덱스를 출력한다.

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [input().rstrip() for i in range(n)]
arr.sort()
print(arr[m-1])