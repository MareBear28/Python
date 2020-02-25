def getPurchaseAmount():
    purchaseAmount = 0
    purchaseAmount = input('Enter the purchase amount: \t')
    # edited to check value
    ask = True
    while ask:
        if not (purchaseAmount.isdigit()):
            print('Input was not a number, try again!')
            purchaseAmount = input('Enter the purchase amount: \t')
            ask = True
        else:
            ask = False
    num = float(purchaseAmount)
    print(f'The purchase amount was ${num}')
    return num


def sales_Tax(amount):
    salesTaxRate = .05
    salesTax = salesTaxRate * amount
    print('Sales tax was $', salesTax)
    return salesTax


def county_Tax(amount):
    countyTaxRate = .025
    countyTax = float(countyTaxRate * amount)
    print('Your county tax is $', countyTax)
    return countyTax


def totalTax(Tsales, Tcounty):
    taxes = Tsales + Tcounty
    print('The total tax was $', taxes)
    return taxes


def TotalPurchase(amount, taxes):
    TotalAmount = amount + taxes
    print('The total purchase amount was $', TotalAmount)


def main():
    purchase = 0
    salesTax = 0
    countyTax = 0
    Tax = 0
    purchase = getPurchaseAmount()
    salesTax = sales_Tax(purchase)
    countyTax = county_Tax(purchase)
    Tax = totalTax(salesTax, countyTax)
    TotalPurchase(purchase, Tax)


main()
