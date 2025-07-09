#example1

# for x in range(1,11):
#     a = x*x
#     print(a)

#example2

# x = 1
# while x <= 10:
#     a = x*x
#     print(a)
#     x +=1
#     print('Dean')

#example 3

# s = ' '
# for x in range(10) :
#     s += str(x)+ ' '
# print(s)

#example4

# for x in range(1,101) :
#     print(x)

#example5

# for x in range(10, 0, -1):
#     print(x)

# example6

# for x in range(10,501,5):
#     print(x)

#example7

# A = [3,4,8,6,1]
# N = len(A)
# for x in range(N-1,-1,-1):
#     print(A[x])

#example8

# A = [3,4,8,6,1]
# N = len(A)
# s = ' '
# for x in range(-1, -N-1, -1):
#     s += str(A[x])+ ' ' 
# print(s)

#example9

# count = 0
# for x in range(1,101):
#     if x%7 == 0:
#         count+= 1
# print('Count =', count)

#example10
# lst = []
# for x in range(1,101):
#     if x%7 == 0:
#         lst.append(x)
# print('Count =', len(lst))
# print(lst)

#example11
# string = input('Enter your message ')
# count = 0
# for x in string :
#     if x in '0123456789':
#         count += 1
# print('Count digits =', count)

#example12

string = input('Enter your message ')
newStr = ' '
for x in string :
    if x in '0123456789':
        newStr += '#'
    else :
        newStr += x
print(newStr)
