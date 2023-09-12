# 성적이 낮은 순서대로 이름 출력

# 학생수 입력 받기
n = int(input())

# 학생이름, 점수 입력받기 
array = []
for i in range(n):
    input_data =input().split()
    # 이름은 문자열로, 점수는 정수형으로 전환하여 저장 
    array.append((input_data[0],int(input_data[1])))

# key를 이용하여 점수기준으로 정렬하기
# 리스트의 요소를 student로 정의하고 student의 1번 인덱스를 기준으로 정렬  
array = sorted(array,key=lambda student: student[1])

# 출력 
for student in array:
    print(student[0],end=' ')
