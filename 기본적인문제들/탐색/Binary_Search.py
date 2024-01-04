'''
[입력]
10
20 22 23 24 4 4 5 7 8 10
10
1 2 3 4 5 6 7 8 9 10

[출력]
XXXOOXOOXO
'''

n = int(input())
arr = list(map(int,input().split()))
k = int(input())
goal = list(map(int,input().split()))
arr.sort()

def search(num, arr):
    mid = len(arr) // 2
    if num == arr[mid]:
        return 'O'
    elif len(arr) == 1:
        return 'X'
    elif num < arr[mid]:
        return search(num, arr[:mid])
    elif num > arr[mid]:
        return search(num, arr[mid:])
    

result = []
for i in range(k):
    result.append(search(goal[i],arr))
print(''.join(result))