num = 1
def fun1():
  global num
  print(num)
  num = 123
  print(num)

fun1()
print(num)

def outer():
  num = 10
  def inner():
    nonlocal num
    num = 100
    print(num)
  inner()
  print(num)

outer()