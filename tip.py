bill = float(input("Enter bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))
tip = bill * (tip_percent / 100)
total = bill + tip
print(f"Total amount: ${total:.2f} (Tip: ${tip:.2f})")
