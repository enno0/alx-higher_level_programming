#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    
        kamal=len(argv) - 1
        plural_s = "s" if kamal != 1 else ""
        print("{} argument{}".format(kamal, plural_s),end="")
        print("{}".format(":" if kamal > 0 else "."))
        for i in range(kamal):
             print("{:d}: {}".format(i + 1, argv[i + 1]))
        
