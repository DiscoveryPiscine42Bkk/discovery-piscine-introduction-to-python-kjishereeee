#!/usr/bin/env python3
import sys
if len(sys.argv) < 2 or "z" not in sys.argv[1]:
    print("none")
else:
    for i in sys.argv[1]:
        if i.count("z") == 1:
            print("z",end='')
    print()