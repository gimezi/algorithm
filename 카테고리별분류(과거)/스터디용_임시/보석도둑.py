# 보석도둑
'''
2 1
5 10
100 100
11

10
'''
from collections import deque

N, K = map(int,input().split())
dias = []
for _ in range(N):
    M, V = map(int,input().split())
    