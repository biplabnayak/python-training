name = "python programming"
print(name.upper())
print(name.startswith("p"))
print(name.endswith("p"))

template = "I Love {} and {}"
print(template.format("Java", "Python"))
print(template.format(1, 2))

aname = "   Hello     "
print(len(aname))
print(len(aname.strip()))
print(len(aname.lstrip()))
print(len(aname.rstrip()))

alist = ["java", "oracle", "python"]
name = "-".join(alist)
print(name)


# String slicing
# string[start:stop:step]
name = "python programming"
print(name[0])
print(name[1])
print(name[0:5])
print(name[::])
print(name)
print(name[:])
print(name[0:18:2])
print(name[1:18:2])
print(name[-1])  # g
print(name[-2])  # n
print(name[::-1])

""" 
print(10,20,30)
a = [1,2,3]
a.reverse()
print(a)
 """