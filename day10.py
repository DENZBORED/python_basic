#example1
# A = []
# x = 0
# while x < 5:
#     a = input( )
#     A.append(a)
#     x += 1
# print('Last loop =', x)
# print(A)

#example2
# lst = []
# mystr = input()
# while len(mystr)>0:
#     lst.append(mystr)
#     mystr = input()
# print(lst)
# print(len(lst))

#example 3
A = [int(e) for e in input().split()]
x = 0
B = []
C = []
while x < len(A):
    if A[x]>=0:
        B.append(A[x])
    else :
        C.append(A[x])
    x+=1
print(A)
print(B)
print(C)