def main():
    main()
def checkEquality(num1, num2):
    n1 = str(num1)
    n2 = str(num2)
    if(num1 == num2):
        print("The values are equal.")
    elif(num1>num2):
        print(n1 + " is greater than " + n2)
    elif(num2>num1):
        print(n2 + " is greater than " + n1)
    else:
        print("What?")
checkEquality(8, 5)
checkEquality(6, 6)
checkEquality(5, 5)
checkEquality(5, 4)
checkEquality(-1, 4)