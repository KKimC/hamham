# key를 이용한 정렬 
array=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

# 데이터의 두번째 원소를 기준
result = sorted(array,key=setting)
print(result)