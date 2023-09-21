#백준 1764번 듣보잡

#idea
#처음 받는 배열을 리스트에 넣어놓고
#2번째에 받는 배열을 리스트를 넣지 않고 한개 in연산자로 비교하여 1번 리스트에 있으면 정답 리스트에 넣는다
# -> n,m은 50만개라서 시간초과날 듯
# -> set쓰면 in 시간 복잡도 O(1)이라서 ㄱㅊ을듯

import sys

input = sys.stdin.readline

n,m=map(int,input().split())
arr=set()
arr2=set()

# for i in range(n):
#     arr.add(str(input().rstrip()))
#
# for i in range(m):
#     s=str(input().rstrip())
#     if s in arr:
#         answer.append(s)
#         answer_num+=1
# answer.sort()
# print(answer_num)
# for i in answer:
#     print(i)
# 92ms 37400kb

for i in range(n):
    arr.add(str(input().rstrip()))

for i in range(m):
    arr2.add(str(input().rstrip()))
answer=list(arr&arr2)
answer.sort()

print(len(answer))
for i in answer:
    print(i)
#104ms 44060kb

# import sys
# n, m = map(int, input().split())
# nameList = sys.stdin.read().splitlines()
# hearset = set(nameList[:n])
# seeset = set(nameList[n:])
# ret = list(hearset & seeset)
# ret.sort()
# print(len(ret))
# for i in ret:
#     print(i)
#이건 퍼온건데 68ms 45232kb
#input받는 속도가 빠른건가 slicing은 시간 복잡도 for랑 같을텐데