#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in array:
    if i > 5:
        new.append(i+2)
print(f"{array}")
print(f"{set(new)}")



