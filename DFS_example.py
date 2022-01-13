# 재귀함수를 사용하여 DFS 구현
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드에 연결된 노드 중 방문하지 않은 노드들을 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)
