# 1
# class String2:
#     def __init__(self):
#         self.str = ""
#     def get_string(self):
#         self.str = input("Enter a string: ")
#     def print_string(self):
#         print(self.str.upper())

# new_string = String2()
# new_string.get_string()
# new_string.print_string()


# 2
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         print(0) 
# class Square(Shape):
#     def __init__(self):
#         self.length = 0
#     def init(self):
#         self.length = int(input("Input length: "))
#     def area(self):
#         print("Area: {} ".format(self.length ** 2))

# shape1 = Shape()
# shape1.area()
# shape2 = Square()
# shape2.init()
# shape2.area()


# 3
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         print(0) 
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print("Area of rectangle: {}".format(self.length * self.width))
# shape1 = Rectangle(5,10)
# shape1.area()


# 4
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"Coordinate: {self.x},{self.y}")
#     def move(self, nx, ny):
#         self.x += nx
#         self.y += ny
#     def dist(self, inner):
#         d = (abs(self.x - inner.x) ** 2 + abs(self.y - inner.y) ** 2) ** (1/2)
#         print(f"Distance: {d}")
# poi = Point(2, 6)
# poi.show()
# poi.move(10, 10)
# poi.show()
# poi2 = Point(0, 0)
# poi2.show()
# poi.dist(poi2)


# 5
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, cash):
#         self.balance += cash
#         print(f"Balance: {self.balance}")
#     def withdraw(self, cash):
#         if self.balance >= cash:
#             self.balance -= cash
#             print(f"Balance: {self.balance}")
#         else:
#             print("Not enough balance")
#             print(f"Balance: {self.balance}")

# acc = Account("John", 0)
# acc.deposit(1000)
# acc.withdraw(600)
# acc.withdraw(700)
# acc.deposit(300)
# acc.withdraw(700)


# 6
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return False
#     return True

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11]
# primes = list(filter(lambda x: isPrime(x), l))
# print(primes)