a,b = 10,20
if a < b:
    print("A is less than B")
    print("inside if")
else:
    print("B is less then A")
    print("inside else")

name = "Python programming"
if name.startswith("p"):
    print("its python")
elif name.startswith("j"):
    print("its java")
else:
    print("its C")

if name.isupper():
    print("uppercase")
else:
    print("lowercase")