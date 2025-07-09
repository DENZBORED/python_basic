#example1
# C1 = [ 27, 33, -63, 67]
# print(C1)
# C1.sort(reverse=True)
# print(C1)

# #example2
# C2 = list('Python3')
# print(C2)
# C2.sort(reverse=True)
# print(C2)

# #example3
# A = [2, 8.5, -6, 7]
# print(sorted(A))
# print(A)

# # #example4
# C2= list('Python3')
# C2s = sorted(C2)
# print(C2)
# print(C2s)

# example5
# tp = (6,7,2,7,6,3)
# tps = sorted(tp)
# print(tp)
# print(tps)

# #example6
# s3 = 'Python3'
# print(sorted(s3))
# print(s3)
# s3s = sorted(s3)
# print(s3s)
# print(s3)

# #example7
# tp = (6,7,2,7,6,3)
# tps = sorted(tp,reverse=True)
# print(tp)
# print(tps)

# #example8
# names = {'Andy', 'TINTIN', 'silvia', 'Kin'}
# rn = sorted(names,reverse=True)
# print(rn)
# print(names)

#example9
# words= input('Enter words here: ').split()
# print('Before sort')
# st = ''
# for w in words:
#     st += w + ' '
# print(st)
# words.sort()
# print('After Sort')
# st = ''
# for w in words:
#     st += w + ' '
# print(st)
# print(words)

#example10

nums = [float(x) for x in input().split()]
print('Before sort')
print(nums)
nums2 = sorted(nums)
print('After sort')
print(nums2)
mid = len(nums2)//2
if len(nums2)%2 != 0:
    md = nums2[mid]
else :
    md = (nums2[mid-1]+nums2[mid])/2
print('Median =', md)