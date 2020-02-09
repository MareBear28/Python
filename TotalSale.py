
PurchaseAmount = float(input("Enter amount of purchase."))
salesTax = .05 * PurchaseAmount
countyTax = .025 * PurchaseAmount
TotalTax = salesTax + countyTax
print("The amount of purchase was $",PurchaseAmount,".")
print("The sales tax was $", salesTax,".")
print("The county tax was $", countyTax,".")
print("The total sales tax was $", TotalTax,".")
print("The total sale was $", PurchaseAmount + TotalTax,".")
