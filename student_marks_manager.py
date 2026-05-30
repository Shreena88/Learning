print("1. Add student")
print("2. View students")
print("3. Search student")
print("4. Find topper")
print("5. Sort by marks")
print("6. average marks")
print("7. Exit")

students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students.append((name, marks))
    print("Student added")

def view_students():
    for student in students:
        print(f"{student[0]}: {student[1]} marks")

def search_student():
    search_name = input("Enter student name to search: ")
    for student in students:
        if student[0] == search_name:
            print(f"{student[0]}: {student[1]} marks")
            return
    print("Student not found")

def find_topper():
    if not students:
        print("No students added")
        return
    topper = max(students, key=lambda x: x[1])
    print(f"Topper: {topper[0]} with {topper[1]} marks")

def sort_by_marks():
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    for student in sorted_students:
        print(f"{student[0]}: {student[1]} marks")

def average_marks():
    if not students:
        print("No students added")
        return
    average = sum(student[1] for student in students) / len(students)
    print(f"Average marks: {average:.2f}")

while True:
    choice = int(input("Choose an option: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        find_topper()
    elif choice == 5:
        sort_by_marks()
    elif choice == 6:
        average_marks()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid option")