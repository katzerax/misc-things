def main():
    x = 0
    x = get1to10(x)
    print("Your input was", x)

def get1to10(num):
    try:
        num = int(input("Enter a number 1-10: "))
        if(num<=10 and num>=1):
            print("Valid Number")
            return num
        else:
            print("Invalid Number")
    except:
        print("Invalid Input Type")
main()