thistuple = ("apple", "banana", "cherry")

print(thistuple)

print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# <class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



