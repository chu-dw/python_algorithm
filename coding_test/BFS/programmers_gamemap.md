# 게임 맵 최단거리

## 문제
ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. </br>
따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다. </br>
지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다.  </br>
검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다.  </br>
캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다. </br>
게임 맵의 상태 maps가 매개변수로 주어질 때,  </br>
캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. </br>
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요. </br>

## 풀이 
(백준 사이트 오류로 프로그래머스 문제) </br>
기본적인 최단거리 구하는 bfs문제였다. </br>

 ```python
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]    

   
    distance = [[-1]*m for _ in range(n)]
    distance[0][0] = 1  
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    
    return distance[n-1][m-1]
```
