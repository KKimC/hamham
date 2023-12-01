n = int(input())
arr = list(map(int, input().split()))

d = [0] * (n)

for i in range(n):
    d[i] = arr[i-1]
    for j in range(i):
        d[i] = max(d[i], d[i-j] + d[j])
print(d)
    