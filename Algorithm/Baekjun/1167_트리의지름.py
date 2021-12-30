import sys

# KB / ms Python3
# input = sys.stdin.readline
'''
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
'''

sys.stdin = open('input_1167.txt')


def bfs(v):
    global max_d
    visited = [0] * (V + 1)
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        t = Q.pop(0)
        for i in range(1, len(tree[t])):
            if not visited[i]:
                visited[i] += tree[t][i][1]
                if visited[i] > max_d:
                    max_d = visited[i]
                Q.append(i)


V = int(input())
arrs = [list(map(int, input().split())) for _ in range(V)]
tree = [[] for _ in range(V + 1)]
max_d = 0

# 트리 만들기
for arr in arrs:
    idx = 1
    node = arr[0]
    while arr[idx] != -1:
        tree[node].append((arr[idx], arr[idx + 1]))
        idx += 2

for i in range(1, V + 1):
    bfs(i)

print(max_d)

# 메모리 초과

# def dfs(node, d):
#     global max_d
#     if max_d < d:
#         max_d = d
#
#     for i in range(1, V + 1):
#         if tree[node][i] and not visited[node][i]:
#             visited[node][i] = 1
#             visited[i][node] = 1
#             dfs(i, d + tree[node][i])
#
#
# V = int(input())
# arrs = [list(map(int, input().split())) for _ in range(V)]
# tree = [[0] * (V + 1) for _ in range(V + 1)]
# visited = [[0] * (V + 1) for _ in range(V + 1)]
# max_d = 0
#
# # 트리 만들기
# for arr in arrs:
#     idx = 1
#     node = arr[0]
#     while arr[idx] != -1:
#         tree[node][arr[idx]] = arr[idx + 1]
#         idx += 2
#
# for i in range(1, V + 1):
#     dfs(i, 0)