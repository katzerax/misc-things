def main():
    hoursWorked = 0.0
    hourlyWage = 0.0
    totalPay = 0.0

    hoursWorked = getWageInfo(1)
    print("hoursWorked = ", hoursWorked)
    hourlyWage = getWageInfo(2)
    print("hourlyWage = ", hourlyWage)

    totalPay = calcTotalPay(hoursWorked, hourlyWage)
    print("Weekly pay is $: ", totalPay)

def getWageInfo(x):
    if x == 1:
        y = int(input("What is your hours? "))
        return(y)
    elif x == 2:
        y = int(input("What is your wage? "))
        return(y)

def calcTotalPay(x, y):
    if(x<40):
        total = x * y
        return(total)
    elif(x>=40):
        bonus = y*1.5
        total = (x * y) + bonus
        return(total)

main()