# sys라이브러리 readline()예제 

import sys

# 하나의 문자열 데잍 입력 받기 
# readline()은 엔터가 줄바꿈기호로 입력되니까 
# 공백 문자를 제거하려면 rstrip()
input_data = sys.stdin.readline().rstrip()

# 입력 받은 문자 그대로 출력 
print(input_data)