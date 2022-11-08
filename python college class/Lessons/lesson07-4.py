from random import randint

def main():
    x = getRank()
    print(x)

def getRank():
    print("Is the following number, in your opinion, low (L), medium (M), or high (H)?")
    print(randint(1,1000))
    try:
        x = str(input(""))[0]
        x = x.lower()
        if(x == 'h' or x == 'm' or x == 'l'):
            return(x)
    except:
        print("Please enter a valid input.")

main()