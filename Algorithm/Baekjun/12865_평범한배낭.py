import sys

# KB / ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_12865.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    DP = [list(map(int, input().split())) for _ in range(N)]