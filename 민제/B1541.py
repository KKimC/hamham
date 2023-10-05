#백준 1541번 잃어버린 괄호

#idea
#이 문제는 적절히 괄호를 사용하여 최솟값을 만들어주면 되는 문제이다.
#최솟값을 만들려면 - 부호 뒤에 오는 +들을 다 괄호로 묶어서 더해주고 빼고를 반복하면 된다.
#-를 기준으로 split을 받아서 각 리스트들을 다 더해주고 리스트 순서대로 빼주면 될거같다.

arr=list(map(str,input().split('-')))
temp = sum(map(int,arr[0].split('+')))
for i in range(1,len(arr)):
    temp-=sum(map(int,arr[i].split('+')))
print(temp)