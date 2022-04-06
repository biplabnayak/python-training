import sys

try:
    # fobj acts like file cursor or pointer or reference
    with open("numbers1.txt","r") as fobj:
        data =fobj.readlines()

except FileNotFoundError as err:
    print("system generated error :", err)
    print("user error :","file not error")    
    print(sys.exc_info())
except TypeError as err:
    print("system generated error :", err)
except ValueError as err:
    print("system generated error :", err)
except (KeyError,IndexError) as err:
    print(err)
except Exception as err:
    print(err)
else:
    for line in data:
        line = line.strip()
        print(line)
