import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 도시크기(행/열), M: 하나의 집이 지불할 수 있는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]  # 도시
    max_homes = 0
    temp = [arr[r][:] for r in range(len(arr))]
    for K in range(1, N + 2):
    # for K in range(3, 0, -1):
        costs = K * K + (K - 1) * (K - 1)

        # 시작점
        for i in range(-K, N - K + 1):
            for j in range(N):
                homes = 0
                arr = [temp[r][:] for r in range(len(temp))]
                # 다이아몬드형 방범 범위(위~중간지점)
                for c in range(K):
                    a = i + c
                    for b in range(j - c, j + c + 1):
                        if 0 <= a < N and 0 <= b < N and arr[a][b]:
                            homes += 1
                        if 0 <= a < N and 0 <= b < N:
                            arr[a][b] = 9

                # 다이아몬드형 방범 범위(중간지점다음~아래)
                for c in range(K-2, -1, -1):
                    a = i + 2 * K - 2 - c
                    for b in range(j - c, j + c + 1):
                        if 0 <= a < N and 0 <= b < N and arr[a][b]:
                            homes += 1
                        if 0 <= a < N and 0 <= b < N:
                            arr[a][b] = 9
                # print(i, j)
                # print(homes)
                # for x in range(len(arr)):
                #     print(arr[x])

                if homes * M - costs >= 0 and max_homes < homes:
                    max_homes = homes

    print('#{} {}'.format(t, max_homes))
