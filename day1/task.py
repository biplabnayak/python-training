data = { "name"   : "John Smith",
  "sku"    : "20223",
  "price"  : 23.95,
  "shipTo" : { "name" : "Jane Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" },
  "billTo" : { "name" : "John Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" }
}

print(data)

for key,value in data.items():
    print(key)
    print("------")
    if type(value) is dict:
        print(",".join(value.values()), "\n")
    else:
        print(value,"\n")



'''
Name
-----
John Smith

sku
----
20223

price
-----
23.95

shipTo
---------
Jane Smith, 123 Maple Street, Pretendville ,NY, 12345

billTo
--------
Jane Smith, 123 Maple Street, Pretendville ,NY, 12345
'''




# info = [
# 	{
# 		'color': "red",
# 		'value': "#f00"
# 	},
# 	{
# 		'color': "magenta",
# 		'value': "#f0f"
# 	},
# 	{
# 		'color': "yellow",
# 		'value': "#ff0"
# 	},
# 	{
# 		'color': "black",
# 		'value': "#000"
# 	}
# ]



# for i in info:
#     print(i.get('color').ljust(10), "-", i.get('value'))



# data = {
# "id": "0001",
# "type": "donut",
# "name": "Cake",
# "image": {
# "url": "images/0001.jpg",
# "width": 200,
# "height": 200
# },
# "thumbnail": {
# "url": "images/thumbnails/0001.jpg",
# "width": 32,
# "height": 32
# }
# }

# for key, value in data.items():
    
#     if type(value) is dict:
#         for k, v in value.items():
#             print(key,".",k," : ", v, sep="")
#     else:
#         print (key, ":", value)


# ############

# for key,value in data.items():  
#     if isinstance(value,str):
#         print(key.ljust(15),":",value)
#     elif isinstance(value,dict):
#         for ikey,ivalue in value.items():
#             final = key  + "." + ikey
#             print(final.ljust(15),ivalue)


