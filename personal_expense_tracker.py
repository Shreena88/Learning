import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#initialize file name
file_name = ("expenses.csv")

#function to load data
def load_data():
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Amount","Category","Notes"])

#Function to save data
def save_data(df):
    try:
        df.to_csv(file_name,index=False)
    except Exception as e:
        print(f"Error saving data: {e}")

#Function to add expenses
def add_Expense(df):
    # Date input and validation
    while True:
        date = input("Enter the date(yyyy-mm-dd): ")
        try:
            #validate date format
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.Please enter the date as yyyy-mm-dd.")

    #Amount input with error handling
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <=0:
                print("Amount must be greater than 0.Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount.Please enter a numeric value.")

    category = input("Enter the category (e.g.,Food,Transport,Entertainment): ")
    notes = input("Enter any notes:")

    #Append to the dataframe
    new_expense = pd.DataFrame([[date, amount, category, notes]], columns=["Date","Amount","Category","Notes"])

    #Drop empty or all-NA columns before concatenation
    new_expense = new_expense.dropna(axis=1,how="all")

    df=pd.concat([df, new_expense], ignore_index=True)
    save_data(df)
    print("Expense added successfully!")

#Function to view all expenses
def view_expenses(df):
    print("Expenses List:")
    print(df)

#Function to generate expense reports
def generate_report(df):
    print("Expense Report:")
    category_summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print(category_summary)

    #Visualizing the expenses
    category_summary.plot(kind="bar", title="Spending by Category")
    plt.ylabel("Amount")
    plt.show()

#Main function
def main():
    df = load_data()

    while True:
        print("Choose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Reports")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            add_Expense(df)
        elif choice == "2":
            view_expenses(df)
        elif choice == "3":
            generate_report(df)
        elif choice == "4":
            print("Existing program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
