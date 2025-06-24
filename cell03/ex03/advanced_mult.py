i = 0
while i < 11 :
    print(f"Table de {i}: ", end="")
    j = 0
    while j < 11:
        if j == 10:
            print(f"{i * j}")
        else:   
            print(f"{i * j}", end=" ")
        j += 1
    i += 1
