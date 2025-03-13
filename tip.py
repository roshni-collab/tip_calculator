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

print("Select a tip percentage: ")
print("1. 10%  2. 15%  3. 20%  4. Custom")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    tip_percent = 10
elif choice == 2:
    tip_percent = 15
elif choice == 3:
    tip_percent = 20
else:
    tip_percent = float(input("Enter custom tip percentage: "))
