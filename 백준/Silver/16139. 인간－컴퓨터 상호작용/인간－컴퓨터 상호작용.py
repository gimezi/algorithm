import sys
input = sys.stdin.readline

S = input().strip()
n = int(input())
arr = [[0 for _ in range(len(S))] for _ in range(26)]
for i in range(len(S)):
  # print('문자', S[i], '계산 값', ord(S[i]) - 97)
  arr[ord(S[i]) - 97][i] = 1  
 
for _ in range(n):
  a, start, end = input().split()
  print(sum(arr[ord(a) - 97][int(start):int(end)+1]))