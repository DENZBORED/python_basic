#example1
# y = [ 27, 18, 19, 23, 4]
# x = int( input('x = ') )
# found = -1; index = 0
# while index < len(y):
#     a = y[index]
#     if a == x:
#         print('x, is found at ', index )
#         found = index
#     index += 1

# if found == -1:
#     print(x, 'is not found')

#example2
# y = [ (64125,2.15), (64104, 2.87), (64402,3.54), (64110,3.15), (64500,2.05), (64064, 2.64) ]
# x = int( input('x =') )

# found = -1
# index = 0
# while index < len(y):
#     a = y[index]
#     if a[0] == x:
#         print('GPA of', x, ' = ', a[1])
#         found = index
#         break
#     index += 1
# if found == -1:
#     print(x, 'is not found')

#example 3
# y = [18, 19, 27]
# x = 28
# found = -1
# left = 0
# right = len(y)
# z = y[left:right]
# while len(z)>0:
#     m = (left+right)//2
#     if y[m == x]:
#         found = m
#         break
#     elif x > y[m]:
#         left=m+1
#         z = y[left:right]
#     else:
#         right = m
#         z = y[left:right]
# if found == -1:
#     print(x, 'is not found')
# else :
#     print(x, ' is found at', found)

#example4
# A = [27, 18, 4, 0.19, 0.9]
# print(A)
# A.sort()
# print(A)

# B = ['three', 'seven', 'hello']
# print(B)
# B.sort()
# print(B)

B2 = list('IAmSteve')
print(B2)
B2.sort()
print(B2)