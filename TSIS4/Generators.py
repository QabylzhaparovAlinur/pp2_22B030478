# 1
# def squares(n):
#     for i in range(1, n+1):
#         yield i*i

# for i in squares(6):
#     print(i)



# 2
# def even(n):
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             yield i

# evens = ""
# for i in even(int(input())):
#     evens += str(i) + ','
# print(evens[:-1])



# 3
# def div(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# for i in div(100):
#     print(i)
 


# 4
# def squares(a, b):
#     for i in range(a, b+1):
#         if pow(i, 1/2) == round(pow(i, 1/2)):
#             yield i
# for i in squares(15, 90):
#     print(i)



# 5 
# def down(n):
#     for i in range(1,n+1):
#         yield n + 1 - i

# for i in down(6):
#     print(i)