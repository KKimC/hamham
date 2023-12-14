# 백준 14582번 오늘도 졌다.

# idea
# 두 팀의 점수를 차례차례 반복문으로 더해주며 울림 제미니스가 한번이라도 이기고있으면 Yes 출력

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
t1_point = 0
t2_point = 0

for i in range(len(t1)):
    t1_point += t1[i]

    if t1_point > t2_point:
        print("Yes")
        exit()

    t2_point += t2[i]

print("No")
