# 백준 1952번 달팽이2

# 열보다 행이 작으면 (행-1)*2-1
# 아니면 (열-1)*2를 해준다.
# 수학적으로 풀!기!

m, n = map(int, input().split())

if m > n:
    print((n-1) * 2 + 1)
else:
    print((m-1) * 2)
