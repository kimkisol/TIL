import sys

# KB / ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_20057.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    grid = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]