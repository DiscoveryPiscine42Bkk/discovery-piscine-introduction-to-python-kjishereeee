# word = str(input
for i in range(0, 11):
    print(f"Table de {i}: ", end="")
    for j in range(0, 11):
        if j == 10:
            print(f"{i * j}")
        else:   
            print(f"{i * j}", end=" ")