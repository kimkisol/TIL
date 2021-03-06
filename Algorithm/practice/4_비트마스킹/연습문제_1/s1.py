"""
연습 문제 1.

1번과 2번이 의미하는 바를 실행 결과를 토대로 간단하게 작성하시오.
(APS 기본 과정에서 했던 내용을 참고해보세요.)
"""

#1. 1 << n
# 직접 실행 결과를 확인해보세요!
print(1 << 0)
print(1 << 1)
print(1 << 2)
print(1 << 3)
print(1 << 4)
print(1 << 5)
print(1 << 6)

print('-------------------------------------------------')

#2. i & (1 << j)
# 직접 실행 결과를 확인해보세요!
for i in range(1 << 3):
    print(i, end=' ')
    for j in range(2, -1, -1):
        if i & (1 << j):
            print(1, end='')
        else:
            print(0, end='')
    print()