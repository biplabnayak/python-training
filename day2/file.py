#fobj = open(r"D:\trainings\jpmc04042022\numbers.txt","w")  # raw string
#fobj = open("D:/trainings/jpmc04042022/numbers.txt","w")
#fobj = open("D:\\trainings\\jpmc04042022\\numbers.txt","w")

# traditional way  # legacy way
fobj = open("numbers.txt","w")

for val in range(1,10):
    fobj.write(str(val) + "\n")

fobj.close()


# Using Context manager
# autoclose the resource
with open("numbers1.txt","w") as fobj:
    for val in range(1,10):
        fobj.write(str(val) + "\n")
