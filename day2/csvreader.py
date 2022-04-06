import csv
import sys

cities={}

try:
    # fobj acts like file cursor or pointer or reference
    with open("day2/files/realestate.csv","r") as fobj:
        # convert file object to csv object
        reader = csv.reader(fobj)
        for line in reader:
            s=line[1]
            if s in cities:
                count=cities[s]
                cities[s]=count+1
            else:
                cities[s]=1
        
except FileNotFoundError as err:
    print("system generated error :", err)
    print("user error :","file not error")    
    print(sys.exc_info())
except Exception as err:
    print(err)


for key,value in cities.items():
    print(key, "-", value)