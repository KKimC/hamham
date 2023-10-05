#백준 4949번 균형잡힌 세상

#idea
#문자열을 받아서 한개씩 반복한다음
# answer에 if '('면 list.append('(') elif ')'면 len(list)==0이면 break후 no 출력 list[-1]이 '('면 list.pop
# 대괄호에도 똑같은 로직 적용
# len(list)가 0이면 yes출력 0이 아니면 no출력

import sys

input = sys.stdin.readline

s=''
while True:
    answer_arr=[]
    s=input().rstrip()
    if s=='.':break
    for i in s:
        if i =='(' :
            answer_arr.append('(')
        elif i ==')':
            if len(answer_arr)==0:
                answer_arr.append(1)
                break
            if answer_arr[-1] == '(':
                answer_arr.pop()
            else:
                break
        elif i == '[':
            answer_arr.append('[')
        elif i == ']':
            if len(answer_arr)==0:
                answer_arr.append(1)
                break
            if answer_arr[-1] == '[':
                answer_arr.pop()
            else:
                break
    if len(answer_arr) == 0:
        print('yes')
    else:
        print('no')