# SWEA 원형시계돌리기
'''
원형시계가 있습니다.
몇도 돌릴것인지 90도의 배수로 입력받아주세요.
그리고 시계를 시계방향으로 돌리고, 그 결과를 출력하세요.
'''

from collections import deque
watch = deque([12, 9, 6, 3])
degree = int(input())

for _ in range(degree//90):
    watch.append(watch.popleft())

watch[2], watch[3] = watch[3], watch[2]
print(*watch)
