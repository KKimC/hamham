# 백준 10973번 이전 순열

# idea
# 다음 순열을 구하는 방법에서 조건만 수정하여준다.

n = int(input())
arr = list(map(int, input().split()))

i = len(arr) - 1
while i > 0 and arr[i - 1] <= arr[i]:
    i -= 1

if i <= 0:
    print(-1)
else:
    j = len(arr) - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[i:][::-1]
    print(' '.join(map(str, arr)))
