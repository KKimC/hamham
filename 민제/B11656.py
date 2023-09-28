#백준 11656번 접미사 배열

#idea
#for 문으로 문자열 길이만큼 반복한 다음 [1:]슬라이싱으로 잘라서 배열에 넣어준다.
#배열을 정렬해준다.


s=input()
answer=[]

for i in range(len(s)):
    answer.append(s[i:])
answer.sort()
for i in answer:
    print(i)