from mimetypes import add_type


atuple = (10,20,30)
# atuple[0] = 100 # will throw error while modifying
print("touple : ", atuple)


# Converting list to touple
list1 = [1,2,3]
tuple1 = tuple(list1)
print(tuple1)

btuple = (1,2,3,[4,5,6],7)
print(btuple)
print(btuple[2])
btuple[3].append(100)
print("After Changing internal list", btuple)