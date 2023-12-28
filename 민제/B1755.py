# 백준 1755번 숫자놀이

# idea
# alp배열을 선언하고 배열에 [zero, one, two, three, ... nine]까지 넣어준다.
# 시작 숫자부터 끝 숫자까지 반복하며 해당 숫자마다 알파벳을 넣어준다.
# 알파벳을 정렬해준다.
# 이를 다시 숫자로 변환해준다.

alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

start, end = map(int, input().split())
arr = []
answer = []

for i in range(start, end + 1):
    temp = []
    for j in str(i):
        temp.append(alp[int(j)])
    arr.append(temp)

arr.sort()

for i in arr:
    temp = []
    for j in i:
        temp.append(str(alp.index(j)))
    answer.append(''.join(temp))

for i in range(len(answer)):
    print(answer[i], end=' ')
    if i % 10 == 9:
        print()
