# 백준 17314번 단어 뒤집기2

# idea
# 문자열을 입력받는다.
# temp라는 빈 문자열과 boolean을 만들어놓는다.
# 문자열을 하나씩 반복하여 '<'나 공백이 나오면 이때까지 문자열을 뒤집어서 출력하고 temp를 비워준다.

def reverse_print(temp):
    for i in range(len(temp)-1,-1,-1):
        print(temp[i],end='')

s = input()
temp = []
check = 0

for i in s:
    if check == 0:
        if i == '<' :
            check += 1
            reverse_print(temp)
            print('<',end='')
            temp=[]
        elif i == ' ':
            reverse_print(temp)
            print(' ',end='')
            temp=[]
        else:
            temp.append(i)
    else:
        if i == '>':
            print('>',end='')
            check-=1
        else:
            print(i,end='')

reverse_print(temp)