# main.py
from newcrud import add_student, view_students, update_student, delete_student

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_menu():
    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1.  Add Student")
    print("2.  View Students")
    print("3.  Update Student")
    print("4.  Delete Student")
    print("5.  Exit")

def handle_choice(choice):
    if choice == 1:
        name = input("Enter Name: ")
        age = get_valid_int("Enter Age: ")
        email = input("Enter Email: ")
        course = input("Enter Course: ")
        add_student(name, age, email, course)

    elif choice == 2:
        view_students()

    elif choice == 3:
        student_id = get_valid_int("Enter Student ID to update: ")
        name = input("Enter New Name: ")
        age = get_valid_int("Enter New Age: ")
        email = input("Enter New Email: ")
        course = input("Enter New Course: ")
        update_student(student_id, name, age, email, course)

    elif choice == 4:
        student_id = get_valid_int("Enter Student ID to delete: ")
        delete_student(student_id)

    elif choice == 5:
        print("👋 Exiting program. Goodbye!")
        return False

    else:
        print("Invalid choice. Please choose between 1-5.")
    return True

def main():
    while True:
        display_menu()
        choice = get_valid_int("Select an option (1-5): ")
        if not handle_choice(choice):
            break

if __name__ == "__main__":
    main()
