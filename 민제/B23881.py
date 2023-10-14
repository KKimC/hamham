#백준 23881번 알고리즘 수업 - 선택정렬 1

#idea
# arr에 리스트를 입력받는다
# arr_sort에 arr을 오름차순으로 정리한 배열을 담는다.
# arr을 판별하며 arr_sort[-1]과 같으면 arr의 순서를 바꾼다.

import sys

n,k=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
arr_sort=sorted(arr)
count=0

while arr_sort:
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == arr_sort[-1] :
            a, b = arr.pop(), arr_sort.pop()
            if a==b:continue
            else:
                count+=1
                arr[i]=a
                if count==k:
                    print(a,b)
                    exit()
print(-1)