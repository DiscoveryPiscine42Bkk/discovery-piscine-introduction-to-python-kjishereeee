#!/usr/bin/env python3
import sys
list1 = []
if len(sys.argv) == 3 :
    for i in range(int(sys.argv[1]), (int(sys.argv[2])+1)):
        list1.append(i)
    print(list1)
else:
    print("none")
