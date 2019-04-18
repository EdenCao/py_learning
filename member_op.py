a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
  print("1. variable a in list")
else:
  print("1. variable a not in list")

if (b not in list):
  print("2. variable b not in list")
else:
  print("2. variable b in list")

a = 2
if (a in list):
  print("3. variable a in list")
else:
  print("3. variable a not in list")
