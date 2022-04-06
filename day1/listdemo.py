from re import A


arr1 = [1,2,3,4,5,6,7,8,9,10]

# add 45 to the list - adding single object
arr1.append(11)
print('after appending :',arr1)

# list.extend()  --> adding multiple values
arr1.extend([12,13,14])
print("After extending :",arr1)


# list.insert(index,position)
arr1.insert(1,100)
print('After inserting :', arr1)

# list.remove(value to be removed)
arr1.remove(10)
print("After removing :",arr1)

if 10 in arr1:
    arr1.remove(10)
else:
    print("10 doesn't exist")


getcount = arr1.count(10)
if getcount > 0 :
    arr1.remove(10)


arr1.pop(); # remove last element
print(arr1)
arr1.pop(2); #value at INDEX 2 will be removed
print(arr1)

# list values in reverse order - in place
arr1.reverse()
print(arr1)


#
arr1.sort()
print("After sorting :", arr1)

arr1.sort(reverse = True)
print("After sorting :", arr1)



print("Iterate List - 1")
for val in arr1:
    print(val)

print("Iterate List - 2")
for i in range(0, len(arr1)):
    print(arr1[i])

 
list2 = [1,2,"dfsf","frf"]
# list2.sort() # Sort will fail for heterogenious list
