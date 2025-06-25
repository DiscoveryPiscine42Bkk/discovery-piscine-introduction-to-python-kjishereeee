array = [2, 8, 9, 48, 9, 22, -12, 2]
print(f"Original: {array}")
new1 = []
new2 = []
for i in array:
    new1.append(i+2)
for i in new1:
    if i > 5 :
        new2.append(i)

print(new2)
