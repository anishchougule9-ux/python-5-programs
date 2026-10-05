cost_price = int(input("Enter cost price: "))
selling_price = int(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)

else:
    loss = cost_price - selling_price
    print("Loss =", loss)