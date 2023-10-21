#백준 2822번 점수 계산

#idea
#dict를 이용해 key에 인덱스를 value에 점수를 넣어주고 점수를 기준으로 정렬한 뒤 앞의 다섯개의 합과 key를 출력

di=dict()
answer=0
answer_list=[]

for i in range(8):
    di[i+1]=int(input())
di = sorted(di.items(), key=lambda x:x[1])
for i in range(3,8):
    answer+=di[i][1]
    answer_list.append(di[i][0])
answer_list.sort()
print(answer)
for i in answer_list:
    print(i,end=' ')