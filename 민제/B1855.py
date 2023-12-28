# 백준 1855번 암호

# idea
# 문자열을 리스트로 받고 열의 갯수대로 슬라이싱하여 저장한다.
# 1번 리스트부터 한 개의 리스트씩 띄어가며 문자열을 반대로 바꿔준다.
# 모든 리스트를 인덱스 0부터 다 출력해준다.

n = int(input())
arr = list(input())
char = []

for i in range(0, len(arr), n):
    char.append(arr[i : i + n])
for i in range(1,len(char),2):
    char[i].reverse()

for i in range(len(char[0])):
    for j in range(len(char)):
        print(char[j][i],end='')