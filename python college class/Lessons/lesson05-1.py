value = -1
while value!=0:
    value = int(input("Enter a value to be cubed or 0 to quit: "))
    if value != 0:
        cube = value**3
        print(value, " cubed is ", cube)