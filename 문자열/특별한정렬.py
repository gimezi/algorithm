# 4843 특별한 정렬


# def SpecialSort(a):
#     b = []
#     while len(a) > 0:
#         i = 0
#         b.append(a[len(a) - 1 - i])
#         b.append(a[i])
#         a.pop(i)
#         a.pop(len(a) - 1 - i)
#         i += 1
#     return b


def SpecialSort(arr):
    result =[]
    while len(arr) > 0:
        result.append(max(arr))
        result.append(min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return result


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sorted_list = SpecialSort(arr)
    # print(f'#{tc}', end = ' ')
    # for i in range(10):
    #     print(sorted_list[i], end = ' ')
    # print()
    print(f'#{tc} ',*sorted_list[:10]) # unpacking 이용해서 출력하기


# 최대값이랑 최소값을 찾아서 출력출력 하면 되겠녜
# def SpecialSort(arr):
#     result =[]
#     while len(arr) > 0:
#         result.append(max(arr))
#         result.append(min(arr))
#         arr.remove(max(arr))
#         arr.remove(min(arr))
#     return result