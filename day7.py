#example1

# n=int(input("Enter your number: "))
# if n>0:
#     if n%2 == 0:
#         print("Even Positive Number")
#     else: 
#         print('Odd Positive Number')
# else:
#     if n%2 == 0:
#         print('Even Negative Number')
#     else:
#         print('Odd Negative Number')

#example2
# score = float(input())
# if score%1 >= 0.5:
#     score +=1
# Score = int(score)
# print(Score)

# #example3
# hr = int(input())
# day = hr//24
# if hr%24 >= 15:
#     day += 1
# print(day)

# # #example4
# a = input()
# if a.isnumeric():
#     a = int(a)
# print(a, type(a))

#example5
midterm,final = input().split()
mt = float(midterm)
fn = float(final)
sm = mt+fn
if sm<50 or mt<15 or fn<15:
    print("FAIL ")
else: 
    print("PASS ")