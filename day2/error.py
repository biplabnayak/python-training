import sys

try:
    # fobj acts like file cursor or pointer or reference
    with open("lang.txt","r") as fobj:
        for line in fobj:
            line = line.strip()    # remove whitespaces if any
            print(line)
except Exception as err:
    print("system generated error :", err)
    print("user error :","file not error")    
    print(sys.exc_info())

