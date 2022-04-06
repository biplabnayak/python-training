aset = {10,10,20,20,20,30}
bset = {30,30,30,30,40,50}

print(aset)
print(bset)

aset.add(10)
print(aset)
aset.add(50)
print(aset)

aset.union(bset)
print(aset.union(bset))

print()
