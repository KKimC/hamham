# 백준 10972번 다음 순열

# idea
# python의 순열 라이브러리를 이용하여 순열을 구한다. -> x 메모리 초과
# 수열의 맨 뒤부터 현재 수보다 바로 앞의 수가 더 작은 경우를 찾는다.
# 없으면 -1 출력
# 다시 뒤에서부터 탐색하여 찾은 수의 바로 앞의 수와 비교하며 바로 앞의 수가 큰 경우를 찾아서 바꿔준다.

n = int(input())
arr = list(map(int, input().split()))

i = len(arr) - 1
while i > 0 and arr[i - 1] >= arr[i]:
    i -= 1

if i <= 0:
    print(-1)
else:
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1:i - 1:-1]
    print(' '.join(map(str, arr)))
