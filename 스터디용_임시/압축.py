# 백준 1662 압축

'''
압축되지 않은 문자열 S가 주어졌을 때, 
이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. 
K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 
이 Q라는 문자열이 K번 반복된다는 뜻이다. 
압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.

[입력]
33(562(71(9)))

[출력]
19
'''
'''
3(5)
3

3(5)1
4

3(5(1))
15

3(5(1))1
16

4(3(5(1)))
60

4(3(5(1)))1
61

15(22)13(92(1111)42(222))
60

15(22)13(92(1111)42(222))123(1)45
67
'''


S = input()
# 괄호 밖의 숫자
stack = []


for letter in S:
    if letter == '(':
        pass
    elif letter == ')':
        pass
    else:
        num = int(letter)
        stack.append(num)

























# S = input()
# result = 0
# stack = []
# lst = []
# flag = False

# for letter in S:
#     if letter == '(':
#         flag = True
#         stack.append(lst)
#         lst = []
#         temp = 1
#     elif letter == ')':
#         if lst or temp:
#             stack.append(lst)
#             lst = []   
#         else:
#             pass
#         temp = 0
#     else:
#         num = int(letter)
#         lst.append(num)
# if lst:
#     stack.append(lst)

# if stack:
#     stack.reverse()
#     print(stack)
#     ans = 0
#     kq = 0
#     for i in range(len(stack) - 1):
#         if i:
#             now = len(stack[i]) + kq - 1
#         else:
#             now = len(stack[i]) + kq 
#         if not stack[i]:
#             now = 0
#         if stack[i + 1]:
#             k = stack[i + 1][-1]
#             kq = now * k
#         else:
#             k = 0
#             ans += now
#             kq = 0
#             pass
#     ans += kq + len(stack[-1]) - 1
#     print(ans)
# else:
#     print(len(S))




# S = input()
# result = 0
# stack = []
# lst = []
# flag = False
# temp = 0
# for letter in S:
#     print(letter, stack)
#     if letter == '(':
#         flag = True
#         stack.append(lst)
#         lst = []
#     # 닫는 괄호가 나오면
#     elif letter == ')':
#         if lst:
#             stack.append(lst)
#             now = stack.pop()
#             front = stack.pop()
#         else:
#             now = []
#             front = stack.pop()
#         lst = []
#         # 앞에 꺼의 마지막이 갯수
#         if front:
#             k = front.pop()
#             if k:
#                 # Q는 문자열 갯수니까 now의 길이
#                 q = len(now)
#                 for i in range(k * q):
#                     front.append(i+1)
#                 stack.append(front)
#             else:
#                 print(0)
#                 exit()           
#         else:
#             k = 0
        
#     else:
#         num = int(letter)
#         lst.append(num)

# if flag:
#     ans = 0
#     for a in stack:
#         ans += len(a)
#     print(ans)
# else:
#     print(len(lst))
