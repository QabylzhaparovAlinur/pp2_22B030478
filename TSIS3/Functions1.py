# 1
# def grammToOunces(n):
#     print(n * 28.3495231)
# grammToOunces(1000)
# grammToOunces(500)

# 2
# def FtoC(f):
#     c = (f - 32) * 5 / 9
#     print(c)
# FtoC(50)
# FtoC(100)

# 3
# def solve(heads, legs):
#     for i in range(1, heads):
#         if i * 2 + (heads - i) * 4 == legs:
#             return i, heads - i
#     return False, False
# ch, r = solve(35, 94)
# print(f"Chickens: {ch}\nRabbits {r}")

# 4
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return False
#     return True
# l = [int(x) for x in input().split()]
# primes = list(filter(lambda x: isPrime(x), l))
# print(primes)

# 5
# from itertools import permutations
# def per(s):
#     ans = list(permutations(s))
#     for i in ans:
#         print("".join(i), end="\n")
# s = input()
# print(per(s))

# 6
# def reverse_sentence(sentence):
#     words = sentence.split()
#     words.reverse()
#     print(' '.join(words))
# reverse_sentence("We are ready")
# reverse_sentence("You are not ready")

# 7
# def hash_33(l):
#     for i in range(len(l) - 1):
#         if l[i] == 3 and l[i+1] == 3:
#             print(True)
#             return True
#     print(False)
#     return False
# hash_33([1, 3, 3])
# hash_33([1, 3, 1, 3])
# hash_33([1, 2, 3, 3, 0, 4, 3, 3])

# 8
# def spy(l):
#     for i in range(len(l) - 2):
#         if l[i] == 0 and l[i+1] == 0 and l[i+2] == 7:
#             print(True)
#             return True
#     print(False)
#     return False
# spy([0, 0, 3])
# spy([1, 0, 0, 7])
# spy([1, 2, 3, 3, 0, 7, 3, 3])
# spy([0, 0, 0, 0, 0])
# spy([0, 7, 0, 0, 1])

# 9
# def vol(r):
#     print(4 * 3.14 * r ** 3 / 3)
# vol(1)
# vol(10)
# vol(4)

# 10
# def unique(list):
#     new = []
#     for i in list:
#         if i in new:
#             pass
#         else:
#             new.append(i)
#     print(new)
# unique([1, 1, 1, 1, 2, 2, 3, 3])
# unique([1, 3, 6, 7, 4, 3, 2, 1, 2])

# 11
# def check(s):
#     return s == s[::-1]
# print(check("ababa"))
# print(check("aaaaa"))
# print(check("python"))
# print(check("level"))
# print(check("pppypp"))

# 12
# def histogram(l):
#     for i in range(len(l)):
#         print('*' * l[i])
# histogram([4, 7, 9])
# histogram([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 13
# import random
# x = (random.randrange(1, 20))
# a = input('Hello! What is your name? ')
# print()
# print(f'Well, {a}, I am thinking of a number between 1 and 20.')
# print('Take a guess.')
# b = int(input())
# print()
# cnt = 0
# while b != x:
#     if b < x:
#         cnt += 1
#         print('Your guess is too low.')
#         print('Take a guess.')
#         b = int(input())
#         print()
#     if b > x:
#         cnt += 1
#         print('Your guess is too up.')
#         print('Take a guess.')
#         b = int(input())
#         print()
#     if x == b:
#         print('Good job, ' + str(a) +
#               '! You guessed my number in ' + str(cnt + 1) + ' guesses!')

# # 14
# import Functions2
# Functions2.check()