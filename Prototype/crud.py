import mysql.connector
from connection import mydb 

def get_connection():
    return mydb

# Add student
def add_student():
    name = input("Enter student name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("❌ Age must be a number.")
        return
    email = input("Enter email: ")
    course = input("Enter course: ")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO students (name, age, email, course) VALUES (%s, %s, %s, %s)"
        values = (name, age, email, course)
        cursor.execute(query, values)
        conn.commit()
        print("✅ Student added successfully!")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
    finally:
        cursor.close()

# View students
def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            print("\n=== Student Records ===")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, Course: {row[4]}")
        else:
            print(" No students found.")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
    finally:
        cursor.close()

# Update student
def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return

    new_name = input("Enter new name: ")
    try:
        new_age = int(input("Enter new age: "))
    except ValueError:
        print("❌ Age must be a number.")
        return
    new_email = input("Enter new email: ")
    new_course = input("Enter new course: ")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE students
            SET name = %s, age = %s, email = %s, course = %s
            WHERE id = %s
        """
        values = (new_name, new_age, new_email, new_course, student_id)
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Student updated successfully!")
        else:
            print("⚠️ No student found with that ID.")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
    finally:
        cursor.close()

# Delete student
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Student deleted successfully!")
        else:
            print("⚠️ No student found with that ID.")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
    finally:
        cursor.close()
        conn.close()

# Main menu
def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Enter a number between 1-5.")

if __name__ == "__main__":
    main_menu()
