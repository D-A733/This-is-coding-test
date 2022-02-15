from collections import deque
# BFS 구현하기 위해 deque 사용
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # queue가 빌 때까지 반복
    while queue:
        # queue의 왼쪽에서 하나 뽑기
        v = queue.popleft()
        print(v, end=" ")
        # 뽑은 노드에 연결된 노드중 방문하지 않은 노드들을 queue에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

visited = [False] * 9
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
bfs(graph, 1, visited)
