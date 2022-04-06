book = {"chap1":10 ,'chap2':20 ,"chap3":30}
print(book)


book = {"chap1":10 ,'chap2':20 ,"chap3":30 ,"chap1":1000}
print(book)


# add key:value
book["chap4"] = 40
print(book)
book["chap5"] = 50
print(book)


# only keys
print(book.keys())

# only values
print(book.values())


# items
print(book.items())

print(book['chap1'])
#print(book['chap11'])

print(book.get("chap11")) # if not existing returns None


if "chap11" in book:
    print(book["chap11"])
else:
    print("key doesn't exist")


newbook = {"chap8":80, "chap9":90}

book.update(newbook)
print(book)


finalbook = {**book,**newbook}
print("Output:",finalbook)





# display keys line by line
for key in book.keys():
    print(key)

for key in book:
    print(key)


# display values
for value  in book.values():
    print(value)


# display key,value
for key,value in book.items():
    print(key,value)