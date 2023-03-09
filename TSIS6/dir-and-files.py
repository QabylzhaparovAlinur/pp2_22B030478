import os

# 1
# for root, directories, files in os.walk(r'C:\Users\admin\Desktop'):
#     print(root)
#     for x in directories:
#         print(x)
#     for y in files:
#         print(y)
#     print()

# print([x.name for x in os.scandir(r'C:\Users\admin\Desktop')])


# 2
# f = r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS4'
# print(f'Exist: {os.access(f,os.F_OK)}')
# print(f'Rreadability: {os.access(f,os.R_OK)}')
# print(f'Writability: {os.access(f,os.W_OK)}')
# print(f'Executability: {os.access(f,os.X_OK)}')


# 3
# f = r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS4\json.py'
# if os.path.exists(f):
#     if os.path.isdir(f):
#         print(os.path.dirname(f))
#     else:
#         print(os.path.basename(f))
# else:
#     print("I could not find directory like this")


# 4
# with open("sample.txt", 'r') as file:
#     print(len(file.readlines()))


# 5
# mylist = ['One ', 'Two ', 'Three ', 'Four ', "Five "]

# with open(r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS6\listsample.txt', 'w') as file:
#     for x in mylist:
#         file.write(x)

# f = open(r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS6\listsample.txt')
# print(f.read())


# 6
# for x in range(65, 91):
#     f = open(chr(x)+'.txt', 'x')

# for delete all of this files:
# for i in range(65, 91):
#     os.remove(chr(i)+'.txt')


# 7
# with open('line.txt', 'r') as fromfile:
#     with open('ToCopy.txt', 'w') as tofile:
#         for x in fromfile.read():
#             tofile.write(x)


# 8 
f = r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS6\ToDelete.txt'

# if os.path.exists(f):
#     os.remove(f)
#     print(f'File {os.path.basename(f)} deleted!!!')
# else:
#     print("Doesn't exist")


# TO CREATE ToDelete:
# filepath = os.path.join(r'C:\Users\admin\PycharmProjects\pythonProject\pp2_22B030478\TSIS6', 'ToDelete.txt')
# with open(filepath, 'w') as f:
#     f.write('Hello, world!')