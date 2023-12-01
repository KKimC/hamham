# 백준 2309번 일곱난쟁이

# idea
# 수들을 다 더해서 100을 뺀다.
# 그 수에서 아홉 난쟁이의 수를 차례차례 빼고 뺀 수가 배열 안에 있는지 확인해본다.

arr = []

sumHeight = 0

for i in range(9):
    n = int(input())
    sumHeight += n
    arr.append(n)

for i in range(9):
    temp = arr.pop(0)
    sumHeight -= temp
    for j in range(8):
        if arr[j] == sumHeight:
            arr.pop(j)
            arr.sort()
            for num in arr:
                print(num)
            exit()
    sumHeight += temp
    arr.append(temp)
