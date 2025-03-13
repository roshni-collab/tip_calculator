bill = float(input("Enter bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))
tip = bill * (tip_percent / 100)
total = bill + tip
print(f"Total amount: ${total:.2f} (Tip: ${tip:.2f})")


try:
    bill = float(input("Enter bill amount: $"))
    tip_percent = float(input("Enter tip percentage: "))

    if bill < 0 or tip_percent < 0:
        print("Error: Amounts cannot be negative!")
    else:
        tip = bill * (tip_percent / 100)
        total = bill + tip
        print(f"Total amount: ${total:.2f} (Tip: ${tip:.2f})")
except ValueError:
    print("Error: Please enter a valid number!")
