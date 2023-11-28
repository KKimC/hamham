# 백준 1748 수 이어쓰기 2

# idea
# 수 - 그 수의 자릿수 +1 * 전체 숫자의 갯수로 제일 큰 자릿수의 숫자 갯수를 더해준다.
# 그 이후에는 일의 자리는 9개 십의 자리는 10~99까지 100*2개 100~999까지는 1000*3개로 규칙적으로 늘어나니 이를 계산하여 더해준다.

n = int(input())

num = 1
answer = 0
count = 1

while n >= num:
    num *= 10
    count += 1

num /= 10
count -= 1

answer += int((n - num + 1) * count)
count -= 1

for i in range(count - 1):
    answer += num * (count - i) * 0.9
    num = int(num / 10)

if n >= 10:
    answer += 9
    
print(int(answer))
