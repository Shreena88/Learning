print("1. Visit Website")
print("2. View History")
print("3. go back")
print("4. View current page")
print("5. Exit")

history = []
current_page = None

while True:
    choice = int(input("Choose an option: "))
    if choice == 1:
        url = input("Enter website URL: ")
        if current_page:
            history.append(current_page)
        current_page = url
        print(f"Visiting {current_page}")
    elif choice == 3:   
        if history:
            current_page = history.pop()
            print(f"Going back to {current_page}")
        else:
            print("No history to go back to")
    elif choice == 2:
        print("Browsing History:")
        for page in history:
            print(page)
        print(f"Current page: {current_page}")
    elif choice == 4:
        if current_page:
            print(f"Current page: {current_page}")
        else:
            print("No page currently visited")
    elif choice == 5:
        print("Exiting...")
        break
    else:   
        print("Invalid option") 