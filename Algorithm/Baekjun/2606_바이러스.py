import sys

# input = sys.stdin.readline
sys.stdin = open('input_2606.txt')

def dfs(i, network, visited, visited_nodes):
  for j in network[i]:
    if visited[i][j] == 1 or visited[j][i]:
      continue
    visited[i][j] = 1
    visited[j][i] = 1
    visited_nodes.add(j)
    dfs(j, network, visited, visited_nodes)


N = int(input())
M = int(input())
network = {}
visited = [[0] * (N + 1) for _ in range(N + 1)]
visited_nodes = set([1])

for i in range(1, N + 1):
  network[i] = []

for _ in range(M):
  x, y = map(int, input().split())
  network[x].append(y)
  network[y].append(x)

dfs(1, network, visited, visited_nodes)
print(len(visited_nodes) - 1)