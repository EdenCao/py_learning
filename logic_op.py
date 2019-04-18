a = 10
b = 20

if (a and b):
  print("1. both variable a and b are true")
else:
  print("1. some of a and b is not true")

if (a or b):
  print("2. both a and b are true or some of a and b is true")
else:
  print("2. nether a and b are true")

# change a
a = 0
if (a and b):
  print("3. both a and b are true")
else:
  print("3. some of a and b is not true")

if (a or b):
  print("4. both a and b are true, or some of them is true")
else:
  print("4. both a and b are not true")

if not (a and b):
  print("5. both a and b are false, or some of them if false")
else:
  print("5. both a and b are true")