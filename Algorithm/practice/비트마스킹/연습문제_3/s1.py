"""
연습 문제 3.

0과 1로 이루어진 1차원 배열에서 7개씩 묶어서 10진수로 출력하기
- arr는 편의상 분리한 것이기 때문에 연속된 수로 간주할 것
"""

arr = [
       0,0,0,0,0,0,0, 1,1,1,1,0,0,0, 0,0,0,1,1,0,0, 0,0,0,0,1,1,1, 1,0,0,1,1,0,0,
       0,0,1,1,0,0,0, 0,1,1,1,1,0,0, 1,1,1,1,0,0,1, 1,1,1,1,1,0,0, 1,1,0,0,1,1,1
      ]

result = []

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        # arr[j] -> 0 or 1
        print(i, j, n, n * 2, arr[j])
        n = n * 2 + arr[j]  # 첫번째 자리수부터 << 1을 하고 그 다음 자리수가 추가돼 다시 << 1을 하는 형태
    result.append(n)
print(*result)

#  1,     1,     1,     1,     0,     0,    0
# 2^6    2^5    2^4    2^3    2^2    2^1   2&0