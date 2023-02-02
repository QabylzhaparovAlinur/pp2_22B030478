thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
# brand
# model
# year

for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964 







