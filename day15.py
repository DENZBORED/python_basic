#example 1

# import random
# print(F'{random.random():.2f}')
# print(random.randint(1,9))
# sequence=["apple", "banana", "coconut" ]
# random.shuffle(sequence)
# print(sequence)

# random.seed(19)
# print(F'{random.random():.2f}')
# print(random.randint(1,9))

#ex2
# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%c"))
# date_format = "%d-%m-%Y"
# print(x.strftime(date_format))

# datetime_format = "%a %d %B %Y %H %M %S"
# print(x.strftime(datetime_format))

import pathlib
f = open("test.txt", "r")
print(f)
path = pathlib.Path("test.txt")
print(path)
print(path.exists())
print(path.is_dir())
print(path.is_file())

# print(f.readline())
# print(f.readline())
print("___________")
for x in f:
    print(x)