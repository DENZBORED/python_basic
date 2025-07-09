#example1 

# a = "Dean 12"
# print(a.lower())
# print(a.upper())
# print(a.isalpha())
# print(a.isdigit())
# print(a[3])
# # a[3] = 'a'
# a = "Sachdev"
# print(a)

#example 2

# lst = [4,6,3,8,1]
# print(lst[3])
# print(lst[-5])
# print(len(lst))
# lst[3] += 3
# print(lst)
# lst[2] = lst[0] + lst[4]
# print(lst)
# lst[3] = 1
# print(lst)

#example3

lsta = [2,7,8]
lsta.append(10)
# print(lsta)
# lsta.remove(2)
# print(lsta)
lsta.pop()
print(lsta)
lsta.pop(2)
print(lsta)
lstb = [2,7,2,8,1]
c = lsta+lstb
print(c)

print(c[4:])
print(c[:6])
print(c[1:6:2])