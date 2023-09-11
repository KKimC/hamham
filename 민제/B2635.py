#백준 2635번 수 이어가기

#idea
#1부터 input number까지의 배열 만듬
#for문으로 이 배열 반복돌리고 temp배열로 input number와 input number-i한 배열을 만든 뒤 배열 갯수를 변수 k로 놔둠
# ->매번 len(temp)하면 효율 안좋을 듯
#k가 answer보다 크면 answer과 answer배열 갱신

num=int(input())

arr=[i for i in range(num+1)]
answer=0
an=[]
for i in arr:
    te=[num,num-i]
    k=2
    while True:
        if te[-2]-te[-1]<0:break
        te.append(te[-2]-te[-1])
        k+=1
    if answer<k:
        answer=k
        an=te
print(answer)
for i in an:
    print(i,end=' ')