#백준 10610번 30

#idea
# 우선 30의 배수가 되려면 수열에 0이 있어야한다. 0이 없으면 -1 출력
# 각 자릿수합이 3의 배수가 되면 그 수는 3의 배수이다.
# 수열의 합이 3의 배수이면 내림차순으로 정렬하여 출력
# 아니면 -1 출력

arr=list(map(int,str(int(input()))))
set_arr=set(arr)
if sum(arr)%3!=0:
    print(-1)
else:
    arr.sort(reverse=True)
    if arr[-1]!=0:
        print(-1)
    else:
        print(''.join(map(str,arr)))