def main():
    factorial = 1
    factorial2 = 1
    numnum = 100
    for i in range(1, numnum+1):
        factorial2 *= i
        print(factorial2)
    num = factorial2
    for i in range(1, num+1):
        factorial *= i
        print(factorial)
main()