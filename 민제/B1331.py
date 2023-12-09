# 백준 1331번 나이트 투어

# idea
# 우선 중복이 없어야하니 원래 배열 길이와 set으로 변환한 배열의 길이가 같은지 확인한다.
# 나이트의 이동은 알파벳 이동 2, 숫자 이동 1이거나 알파벳 이동 1, 숫자 이동 2 이므로 이를 벗어나면 Invalid 출력

import sys
def check_knight():
    for i in range(len(arr)):
        alp = abs(ord(arr[i - 1][0]) - ord(arr[i][0]))
        num = abs(int(arr[i - 1][1]) - int(arr[i][1]))

        if not ((alp == 2 and num == 1) or (alp == 1 and num == 2)) :
            return False
    return True


arr = [sys.stdin.readline().rstrip() for i in range(36)]

print("Invalid" if len(set(arr)) != len(arr) or check_knight() == False else "Valid")