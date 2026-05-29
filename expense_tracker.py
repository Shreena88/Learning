print("1. Add expense")
print("2. View expenses")
print("3. Show total spending")
print("4. store expenses in file")
print("5. Exit")

list = []
input1 = int(input("Choose an option: "))


while input1 != 5:
    if input1 == 1:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        list.append((name, amount))
    elif input1 == 2:
        for expense in list:
            print(f"{expense[0]}: ${expense[1]:.2f}")
    elif input1 == 3:
        total = sum(expense[1] for expense in list)
        print(f"Total spending: ${total:.2f}")
    elif input1 == 4:
        with open("expenses.txt", "w") as file:
            for expense in list:
                file.write(f"{expense[0]}: ${expense[1]:.2f}\n")
        print("Expenses saved to expenses.txt")
    else:
        print("Invalid option")

    input1 = int(input("Choose an option: "))