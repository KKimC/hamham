# 백준 2204번 도비의 난독증 테스트

# idea
# 문자를 모두 대문자로 변환한 뒤 정렬하고 첫 번째 문자를 출력한다.

while True:
    num = int(input())
    if num == 0:
        break
    arr=dict()
    for i in range(num):
        s = input()
        arr[s.upper()] = s
    arr = sorted(arr.items())
    print(arr[0][1])
