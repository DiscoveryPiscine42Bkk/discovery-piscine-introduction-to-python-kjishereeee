num = int(input("Enter a number less than 25:\n"))

if num < 25:
    for i in range(num, 25+1):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")