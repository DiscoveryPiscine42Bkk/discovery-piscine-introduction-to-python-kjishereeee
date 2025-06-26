#!/usr/bin/env python3
import sys

x = len(sys.argv)-1
if x == 0 :
    print("none")
else :
    print(f"parameters: {x}")
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")




