#백준 5704번 팬그램

#idea
#list에 알파벳을 넣어놓고 문자열을 str로 받음
#list를 반복문 돌려서 str안에 없으면 N 출

while True:
    str=input()
    if str == '*': break
    for i in range(97,123):
        if not chr(i) in str:
            print('N')
            break
    else:
        print('Y')