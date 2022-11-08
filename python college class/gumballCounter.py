import math
pi = math.pi
loadFactor = 0.69

def main():
    x = 1
    rGum = askForInputs(x)
    x = 2
    rJar = askForInputs(x)
    x = 3
    hJar = askForInputs(x)
    totalGum = doMath(rGum, rJar, hJar)
    print("There is approximately", totalGum, "gumballs in the jar.")

def askForInputs(x):
    rJar = 0.0
    rGum = 0.0
    hJar = 0.0
    if(x == 1):
        while True:
            try:
                rGum = float(input("Enter the radius of the gumball:\n"))
            except:
                print("Please enter a float or integer next time.\n")
                continue
            break
        return(rGum)
    elif(x == 2):
        while True:
            try:
                rJar = float(input("Enter the radius of the jar:\n"))
            except:
                print("Please enter a float or integer next time.\n")
                continue
            break
        return(rJar)
    elif(x == 3):
        while True:
            try:
                hJar = float(input("Enter the height of the jar:\n"))
            except:
                print("Please enter a float or integer next time.\n")
                continue
            break
        return(hJar)

def doMath(rGum, rJar, hJar):
    jarVolume = pi*(rJar ** 2)*hJar
    gumVolume = ((4/3) * pi) * (rGum ** 3)
    totalGum = int((jarVolume/gumVolume) * loadFactor)
    return(totalGum)

main()