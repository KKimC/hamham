#백준 5704번 팬그램

#idea
#문자열을 str로 받고 arr=[0]*26으로 빈배열을 만들어준다.
# for str한 다음 arr[ord(list[i])]+=1을 해준다
#arr배열에 0이 있으면 No

while True:
    arr=[0]*26
    str=input()
    if str=='*':break
    for i in str:
        if i>='a' and i<='z':
            arr[ord(i)-97]+=1
    for i in arr:
        if i==0:
            print('N')
            break
    else:
        print('Y')