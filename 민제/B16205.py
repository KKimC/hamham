# 백준 16205번 변수명

# idea
# 1번 카멜 표기법으로 주어질 경우
# 1번 그대로 출력 2번 문자열을 반복하여 아스키코드가 97보다 작을 경우 앞에 _삽입 3번 첫 문자를 대문자로 변환
# 2번 스네이크 표기법으로 주어질 경우
# 문자열을 _로 split 1번 첫 요소를 제외한 리스트의 문자열을 capitalize 2번 그대로 출력 3번 1번에서 모든 리스트 capitalize
# 3번 파스칼 표기법으로 주어질 경우
# 1번 첫 문자 소문자로 변환 2번 1번에서 대문자 앞에 _삽입 후 소문자로 전부 변 3번 그대로 출력

import sys

def camelCase(s):
    print(s)
    for i in s:
        if ord(i) < 97:
            print("_", end='')
            print(chr(ord(i) + 32), end='')
        else:
            print(i, end='')
    print()
    for i in range(len(s)):
        if i == 0:
            print(chr(ord(s[i]) - 32), end='')
        else:
            print(s[i], end='')

def snakeCase(s):
    arr = list(s.split("_"))
    for i in range(len(arr)):
        if i == 0:
            print(arr[i], end='')
        else:
            print(arr[i].capitalize(), end='')
    print()
    print(s)
    for i in arr:
        print(i.capitalize(), end='')

def pascalCase(s):
    for i in range(len(s)):
        if i == 0:
            print(chr(ord(s[i]) + 32), end='')
        else:
            print(s[i], end='')
    print()
    for i in range(len(s)):
        if i != 0:
            if ord(s[i]) < 97:
                print("_", end='')
                print(chr(ord(s[i]) + 32), end='')
            else:
                print(s[i], end='')
        else:
            if ord(s[i]) < 97:
                print(chr(ord(s[i]) + 32), end='')
            else:
                print(s[i], end='')
    print()
    print(s)

n, s = map(str, sys.stdin.readline().rstrip().split())
n = int(n)

if n == 1:
    camelCase(s)
elif n == 2:
    snakeCase(s)
elif n == 3:
    pascalCase(s)