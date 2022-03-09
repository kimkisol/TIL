import sys
from collections import deque

# KB / ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_12851.txt')

def bfs(start, goal):
    queue = deque()

    queue.append((start, 0])

    while queue:
        node = queue.popleft()
        if node == goal:
            cnt += 1
        nums = [node - 1, node + 1, node * 2]
        for num in nums:
            if num == goal:
                visited[num] = visited[node] + 1
            elif not visited[num]:
                visited[num] = visited[node] + 1
                queue.append(num)
        if res:
            print(cnt)
            print(res)
            return

N, K = map(int, input().split())
visited = [[0, 0] for i in range(100001)]
bfs(N, K)