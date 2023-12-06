# 백준 1919번 애너그램 만들기

# idea
# 알파벳 수만큼 배열을 만들고 각 알파벳의 10진수 변환 값 - 97한 값을 배열에 한개씩 쌓는다.

a = [0] * 26
b = [0] * 26
ans = 0

for i in input():
    a[ord(i) - 97] += 1
for i in input():
    b[ord(i) - 97] += 1
for i in range(len(a)):
    ans += abs(a[i] - b[i])
print(ans)
