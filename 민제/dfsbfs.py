'''
음료수 얼려먹기
n,m = 15,14
arr = [
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1]]

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if arr[x][y]==0:
        arr[x][y]=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)
'''
'''from collections import deque

n,m=5,6
arr=[[1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or ny<=-1 or nx>=n or ny>=m:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                queue.append((nx,ny))
    return arr[n-1][m-1]
print(bfs(0,0))'''
'''from collections import deque
import sys

input=sys.stdin.readline
n,m = map(int,input().split())
arr=[]
temp=[[0]*m for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:continue
        if temp[nx][ny]==0:
            temp[nx][ny]=2
            virus(nx,ny)
def score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result = max(result,score())
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j]==1
                count+=1
                dfs(count)
                arr[i][j]=0
                count-=1
    return answer
print(main())'''

'''from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX = 0
    maxY = 0

    for x,y,x2,y2 in rectangle:
        maxX = max(x2 * 2,maxX)
        maxY = max(y2 * 2,maxY)

    graph = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    #1로 안쪽 다 칠하고
    for x,y,x2,y2 in rectangle:
        for i in range((x * 2),(x2 * 2) + 1):
            for j in range((y * 2),(y2 * 2) + 1):
                graph[j][i] = 1

    #전체 돌면서 주위 8개중에 하나가 0이면서 자기 자신이 1이면 2로 바꿈 테두리 경로
    for y in range(1,maxY + 1):
        for x in range(1,maxX + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    dx = [1,0, 0, -1]
    dy = [0,1, -1, 0]
    queue = deque([(cx * 2,cy * 2,0)])
    ix *= 2
    iy *= 2
    while queue:
        x, y,length = queue.popleft()
        graph[y][x] = 1
        if x == ix and y == iy:
            answer = (length // 2)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                queue.append((nx,ny,length + 1))


    return answer

rectangle=[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX,characterY,itemX,itemY=1,3,7,8
print(solution(rectangle,characterX,characterY,itemX,itemY))'''

'''from collections import deque

for _ in range(int(input())):
    market=int(input())
    #미터가 마이너스로 들어왔을 때 고려해줘야할 것 같은데....
    start=list(map(int,input().split()))
    m=[]
    for _ in range(market):
        m.append(list(map(int,input().split())))
    end=list(map(int,input().split()))
    arr=[[0 for i in range((end[1]//50)-(start[1]//50)+1)] for i in range((end[0]//50)-(start[0]//50)+1)]
    for i in m:
        arr[i[0]//50][i[1]//50]=1
q=deque([start[0]//50,start[1]//50])
dx=[0,0,1,-1]
dy=[1,-1,0,0]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y'''



time=list(map(int,input().split(':')))
start=list(map(int,input().split(':')))
if time[0]>=start[0]:
    start[0]+=24
if start[2]>=time[2]:
    start[2]-=time[2]
else:
    start[1]-=1
    start[2]-=time[2]-60
if start[1]>=time[1]:
    start[1]-=time[1]
else:
    start[0]-=1
    start[1]-=time[1]-60
start[0]-=time[0]
if start[0]==24:start[0]=0
answer=[]
for i in start:
    if i <10:
        answer.append('0')
    answer.append(str(i))
    answer.append(':')
for i in range(len(answer)-1):
    print(answer[i],end='')