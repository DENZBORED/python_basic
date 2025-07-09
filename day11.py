#example1
# n=1; count=0
# while n <= 100: 
#     if n%7 == 0:
#         count += 1
#     n+= 1
# print('Count =', count)

#example2
# A = [float(e) for e in input().split()]
# B = []
# x = 0
# while len(B)<5 :
#     if x<len(A):
#         a = A[x]
#     else : 
#         break
#     x += 1
#     if a<0 : 
#         continue
#     B.append(a)
# else :
#     print('List B is complete.')
# print(B)

#example3
# m = 5; n = 3
# for x in range(m):
#     print(x, end=' : ')
#     for y in range(n):
#         print(str(x)+str(y), end=' ')
#     print()

#example4
# n=int( input() )
# while n>0:
#     for x in range(1,n+1):
#         if n%x == 0:
#             print(x, end=' ')
#     print()
#     n=int(input() )

#example5
n=int( input('n=') )
for x in range(n):
    for y in range(n):
        print ('*',end=' ')
    print()