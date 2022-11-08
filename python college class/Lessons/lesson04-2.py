def checkRange(value, lower, upper):
    if(value<lower or value>upper):
        print(value, " is outside the range.")
    else:
        print(value, " is within the range.")
checkRange(14, 1, 13)