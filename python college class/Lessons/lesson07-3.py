from random import randint

def main():
    guess = 0
    correctNum = 0
    high = 0
    low = 0
    correctNum = randint(1,10)
    while guess!=correctNum:
        guess = get1to10()
        if guess>correctNum:
            print("Too High!")
            high += 1
        elif guess<correctNum:
            print("Too Low!")
            low += 1
        else:
            print("You are correct!")

    print("Guesses too high:", high)
    print("Guesses too low:", low)
    print("Thank you for playing!")

def get1to10():
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