#!/usr/bin/env python3
import sys
import sys

if len(sys.argv) == 3:
    find = sys.argv[1] 
    word = sys.argv[2] 
    count = word.count(find)
    if count == 0:
        print("none")
    else:
        print(count)

else:
    print("none")