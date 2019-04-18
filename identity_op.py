a = 10
b = 20

if (a is b):
  print("1. a has same identity with b")
else:
  print("1. a has different identity with b")

if (id(a) == id(b)):
  print("2. a has same identity with b")
else:
  print("2. a has different b with a")

b = 30
if (a is b):
  print("3. a has same identity with b")
else:
  print("3. a has different identity with b")

if (a is not b):
  print("4. a has not same identity with b")
else:
  print("4. a has same identity with b")
