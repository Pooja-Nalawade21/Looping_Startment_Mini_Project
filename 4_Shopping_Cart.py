num = int(input("Enter Number of Products : "))
subtotal = 0
for i in range(1, num + 1):
    price = float(input(f"Enter Price of Product {i} : "))
    quantity = int(input(f"Enter Quantity of Product {i} : "))
    if price < 0 or quantity < 0:
        print("Invalid Price or Quantity")
    else:
        subtotal = subtotal + (price * quantity)
if subtotal >= 3000:
    discount = subtotal * 10 / 100
else:
    discount = 0
amount = subtotal - discount
if amount < 1500:
    delivery = 100
else:
    delivery = 0
final_amount = amount + delivery

print("==============SHOPPING CART TOTAL===================")
print("Subtotal =", subtotal)
print("Discount =", discount)
print("Delivery Charge =", delivery)
print("Final Payable Amount =", final_amount)