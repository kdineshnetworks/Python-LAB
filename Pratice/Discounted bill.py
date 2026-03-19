amount = float(input("Enter the bill amount: "))
if amount >= 1000:
    discount = 0.1 * amount
    discounted_amount = amount - discount
    print("Discounted bill amount:", discounted_amount , "original bill amount:", amount, "discount applied:", discount) 
elif amount >= 500:
    discount = 0.05 * amount
    discounted_amount = amount - discount
    print("Discounted bill amount:", discounted_amount , "original bill amount:", amount, "discount applied:", discount)
else:    print("No discount applied. Bill amount:", amount)
