#백준 2621번 카드게임

#idea
#우선 리스트 형식으로 자료를 받는다
#색이 모두 같을 때 숫자가 모두 연속적이면 가장 높은 수+900 연속적이지 않을 떄 가장 높은 숫자+600
#카드 4장 숫자가 같을 때 같은 숫자+800, 3장끼리 같고 2장 같을 때 3장이 같은 숫자*10+700
#숫자만 연속적일 때 가장 높은 숫자+500
#3장의 숫자만 같을 때 같은 숫자+400
#2장의 같은 숫자가 2세트있으면 큰 수*10+작은 수+300
#2장의 같은 숫자가 1세트있으면 같은 수+200
#어떤 경우에도 해당하지 않을 때 가장 높은 수+100

#숫자만 연속적일 때와 색이 같을 때의 공통적인 점수가 없음
#조건문으로 다..?
#숫자가 연속적일 때 경우는 2개 밖에 없으니 if로 해놓고 else에서 숫자 조건 주면 될듯
#숫자는 1~9까지 배열만들어서 인덱스별로 넣어놓고 구분하면 될 듯

#반복 여러번 되는 것만 반복문으로 미리 변수 지정해주고 색이 같은지는 처음에 변수 받을 때 구분

answer=0
num_list=[0 for _ in range(10)]
color_equal=0
number_continue=0
num_max=0
temp_color="a"

for i in range(5):
    a,b=map(str,input().split())
    if temp_color==a:
        color_equal+=1
    temp_color=a
    b=int(b)
    num_list[b]+=1
    num_max=max(num_max,b)
temp=0
temp_sum=0

#수가 연속적인지, 수가 연속적이라면 temp_sum=5가 됨
for i in num_list:
    if i == 1 and temp == 0:
        temp_sum+=1
    elif i == 1 and temp == 1:
        temp_sum+=1
    elif temp == 1 and i == 0:
        break
    temp=i

if color_equal==4:
    if temp_sum==5:
        answer=num_max+900
    else:
        answer=num_max+600
else:
    if temp_sum==5:
        answer=num_max+500
    elif num_list.count(4)==1:
        answer=num_list.index(4)+800
    elif num_list.count(3)==1:
        a=num_list.index(3)
        if num_list.count(2)==1:
            answer=a*10+num_list.index(2)+700
        else:
            answer=a+400
    elif num_list.count(2)==2:
        for i in range(len(num_list)-1,0,-1):
            if num_list[i]==2:
                answer+=i*10+num_list.index(2)+300
                break
    elif num_list.count(2)==1:
        answer+=num_list.index(2)+200
if answer<100:
    answer+=num_max+100
    
print(answer)