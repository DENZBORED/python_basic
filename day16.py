#example 1
# f = open("test.txt", "r")
# print(f.readline())
# print("----------------------------------------------------------------------------------------")
# f = open("test.txt", "r")
# print(f.readline())
# print(f.readline())
# print("----------------------------------------------------------------------------------------")
# f = open("test.txt", "r")
# for x in f:
#     print(x)
# print("----------------------------------------------------------------------------------------")
# f = open("test.txt", "r")
# print(f.readlines())

#example 2
# f = open("test.txt", "a")
# f.write("! Now the file has more content!!!")
# f.close()

# print("----------------------------------------------------------------------------------------")

# f = open("test.txt", "r")
# print(f.read())

# print("----------------------------------------------------------------------------------------")

# f = open("test.txt", "a")
# f.writelines(["See you soon!", "! Over and out."])
# f.close

# print("----------------------------------------------------------------------------------------")

# f = open("test.txt", "r")
# print(f.read())


#example 3

# import os
# if os.path.exists("test.txt"):
#     os.remove("test.txt")
# else:
#     print("File does NOT exist")

print("----------------------------------------------------------------------------------------")

with open('test.txt', 'r') as fhandler:
    data = fhandler.read()
    print(data)
with open('test.txt', 'w') as fhandler:
    fhandler.write('Hello World')

print("----------------------------------------------------------------------------------------")

try:
    with open('test.txt', 'r') as fhandler:
        data = fhandler.read()
        print(data)
except IOError as ex:
    print("Error performing I/O operations on the file womp womp", ex)