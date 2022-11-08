def main():
    taxRate = 0.0
    shipping = 0.0
    totalCost = 0.0

    totalCost = getItemCosts()
    taxRate = getOtherCosts(1)
    shipping = getOtherCosts(2)
    printReceipt(totalCost, taxRate, shipping)

    print("Thank you!")

def getItemCosts():
    item = 0.0
    total = 0.0
    while item!=-1:
        item = float(input("Enter a Item Cost or -1 to exit: "))
        if item != -1:
            total += item
    return(total)

def getOtherCosts(x):
    if x == 1:
        tax = float(input("Enter the tax rate (i.e. 0.075 for 7.5%): "))
        return tax
    elif x == 2:
        shipping = float(input("Enter the shipping rate: "))
        return shipping

def printReceipt(total, rate, ship):
    print("Subtotal: $ ", total)
    print("Tax: $ ", rate)
    print("Shipping: $", ship)
    print("------------------------")
    totalTaxed= total + (total*rate)
    grandTotal = round(totalTaxed+ship, 2)
    print("Please pay: $ ", grandTotal)

main()