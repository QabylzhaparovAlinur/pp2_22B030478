# 1
# my_list = [2, 4, 6, 8, 10]
# prod = 1 
# for i in my_list:
#     if type(i) == int:
#         prod = prod * i
#     else:
#         pass
# print(prod)


# 2 
# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     return (upper_count, lower_count)
# my_string = "Hello, World!"
# print(count_upper_lower(my_string))  


# 3
# def palindrome(string):
#     return string == string[::-1]
# print(palindrome("Lab6"))
# print(palindrome("level"))


# 4
# import time
# import math

# num = int(input("Enter a number: "))
# delay = int(input("Enter delay time in milliseconds: "))

# time.sleep(delay/1000)

# result = math.sqrt(num)
# print(f"Square root of {num} after {delay} milliseconds is {result}")


# 5 
# my_tuple = (True, True, False, True)

# if all(my_tuple):
#     print("All elements of the tuple are true")
# else:
#     print("Not all elements of the tuple are true")


